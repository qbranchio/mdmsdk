package mdmsdk

import (
	"context"
	"errors"
	"net/http"
	"strings"
	"time"

	"golang.org/x/oauth2"
	"golang.org/x/oauth2/clientcredentials"

	"github.com/qbranchio/mdmsdk/api"
)

// Production defaults, from the published contract.
const (
	DefaultBaseURL  = "https://enroll.dev"
	DefaultTokenURL = "https://id.enroll.dev/oauth/token"
	DefaultAudience = "https://enroll.dev/api"
)

// Client calls the mdm API. Build it with New; it is safe for concurrent use.
type Client struct {
	baseURL   string
	tokens    oauth2.TokenSource
	actor     string
	userAgent string
	http      *http.Client
	retry     retryPolicy
	low       *api.ClientWithResponses

	services
}

// Option configures a Client.
type Option func(*config) error

type config struct {
	baseURL, actor, userAgent string
	tokens                    oauth2.TokenSource
	http                      *http.Client
	retry                     retryPolicy
	clientID, clientSecret    string
	tokenURL, audience        string
}

// WithBaseURL points the client at another server (a staging or local one).
func WithBaseURL(url string) Option {
	return func(c *config) error { c.baseURL = strings.TrimRight(url, "/"); return nil }
}

// WithClientCredentials authenticates as an account client. Tokens are
// fetched, cached, and refreshed before they expire.
func WithClientCredentials(clientID, clientSecret string) Option {
	return func(c *config) error { c.clientID, c.clientSecret = clientID, clientSecret; return nil }
}

// WithTokenURL and WithAudience override the client-credentials defaults.
func WithTokenURL(url string) Option { return func(c *config) error { c.tokenURL = url; return nil } }

// WithAudience sets the access token audience for client credentials.
func WithAudience(aud string) Option { return func(c *config) error { c.audience = aud; return nil } }

// WithToken uses a fixed bearer token: a delegated token, or a test token.
func WithToken(token string) Option {
	return func(c *config) error {
		c.tokens = oauth2.StaticTokenSource(&oauth2.Token{AccessToken: token, TokenType: "Bearer"})
		return nil
	}
}

// WithTokenSource uses tokens from ts.
func WithTokenSource(ts oauth2.TokenSource) Option {
	return func(c *config) error { c.tokens = ts; return nil }
}

// WithActor records, for an account client, the user it acts for (Mdm-Actor).
func WithActor(actor string) Option { return func(c *config) error { c.actor = actor; return nil } }

// WithHTTPClient sends requests with h (its Transport is used; retries are the SDK's).
func WithHTTPClient(h *http.Client) Option { return func(c *config) error { c.http = h; return nil } }

// WithUserAgent prefixes the User-Agent.
func WithUserAgent(ua string) Option { return func(c *config) error { c.userAgent = ua; return nil } }

// New builds a Client. It needs credentials: WithClientCredentials,
// WithToken, or WithTokenSource.
func New(opts ...Option) (*Client, error) {
	cfg := config{baseURL: DefaultBaseURL, tokenURL: DefaultTokenURL, audience: DefaultAudience, retry: defaultRetry, http: &http.Client{Timeout: 60 * time.Second}}
	for _, o := range opts {
		if err := o(&cfg); err != nil {
			return nil, err
		}
	}
	if cfg.tokens == nil && cfg.clientID != "" {
		cc := clientcredentials.Config{ClientID: cfg.clientID, ClientSecret: cfg.clientSecret, TokenURL: cfg.tokenURL,
			EndpointParams: map[string][]string{"audience": {cfg.audience}}}
		cfg.tokens = oauth2.ReuseTokenSourceWithExpiry(nil, cc.TokenSource(context.WithValue(context.Background(), oauth2.HTTPClient, cfg.http)), time.Minute)
	}
	if cfg.tokens == nil {
		return nil, errors.New("mdmsdk: no credentials: use WithClientCredentials, WithToken, or WithTokenSource")
	}
	c := &Client{baseURL: cfg.baseURL, tokens: cfg.tokens, actor: cfg.actor, userAgent: cfg.userAgent, http: cfg.http, retry: cfg.retry}
	low, err := api.NewClientWithResponses(c.baseURL, api.WithHTTPClient(doer{c}))
	if err != nil {
		return nil, err
	}
	c.low = low
	c.services = newServices(c)
	return c, nil
}
