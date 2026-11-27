package mdmsdk

import (
	"encoding/json"
	"errors"
	"fmt"
	"mime"
	"net/http"
)

// Kind classifies an Error by its HTTP status.
type Kind string

// Error kinds.
const (
	KindBadRequest   Kind = "BadRequest"
	KindUnauthorized Kind = "Unauthorized"
	KindForbidden    Kind = "Forbidden"
	KindNotFound     Kind = "NotFound"
	KindConflict     Kind = "Conflict"
	KindValidation   Kind = "Validation"
	KindRateLimited  Kind = "RateLimited"
	KindUnavailable  Kind = "Unavailable"
	KindServer       Kind = "Server"
	KindUnexpected   Kind = "Unexpected"
)

// Sentinels for errors.Is, one per Kind.
var (
	ErrBadRequest   = &Error{Kind: KindBadRequest}
	ErrUnauthorized = &Error{Kind: KindUnauthorized}
	ErrForbidden    = &Error{Kind: KindForbidden}
	ErrNotFound     = &Error{Kind: KindNotFound}
	ErrConflict     = &Error{Kind: KindConflict}
	ErrValidation   = &Error{Kind: KindValidation}
	ErrRateLimited  = &Error{Kind: KindRateLimited}
	ErrUnavailable  = &Error{Kind: KindUnavailable}
	ErrServer       = &Error{Kind: KindServer}
	ErrUnexpected   = &Error{Kind: KindUnexpected}
)

// FieldError is one invalid field of a request.
type FieldError struct {
	Field  string `json:"field"`
	Detail string `json:"detail"`
}

// Error is an API error: an RFC 9457 problem, or a response that was not one.
// Branch on Code; quote Instance when reporting a problem.
type Error struct {
	Kind     Kind
	Status   int
	Code     string
	Title    string
	Detail   string
	Instance string
	Fields   []FieldError
	// Body is the raw response body.
	Body []byte
}

func (e *Error) Error() string {
	msg := fmt.Sprintf("mdm: %d", e.Status)
	if e.Code != "" {
		msg += " " + e.Code
	}
	if e.Detail != "" {
		msg += ": " + e.Detail
	} else if e.Title != "" {
		msg += ": " + e.Title
	}
	if e.Instance != "" {
		msg += " (" + e.Instance + ")"
	}
	return msg
}

// Is matches the sentinel of the same Kind.
func (e *Error) Is(target error) bool {
	var t *Error
	return errors.As(target, &t) && t.Status == 0 && t.Code == "" && t.Kind == e.Kind
}

func kindOf(status int) Kind {
	switch status {
	case http.StatusBadRequest:
		return KindBadRequest
	case http.StatusUnauthorized:
		return KindUnauthorized
	case http.StatusForbidden:
		return KindForbidden
	case http.StatusNotFound:
		return KindNotFound
	case http.StatusConflict:
		return KindConflict
	case http.StatusUnprocessableEntity:
		return KindValidation
	case http.StatusTooManyRequests:
		return KindRateLimited
	case http.StatusServiceUnavailable:
		return KindUnavailable
	}
	if status >= 500 {
		return KindServer
	}
	return KindUnexpected
}

// decodeError builds the Error for a non-success response. A body that is
// not problem+json (a proxy during a deploy) gives the kind for its status
// with no code.
func decodeError(resp *http.Response, body []byte) *Error {
	e := &Error{Kind: kindOf(resp.StatusCode), Status: resp.StatusCode, Body: body}
	if mt, _, err := mime.ParseMediaType(resp.Header.Get("Content-Type")); err == nil && (mt == "application/problem+json" || mt == "application/json") {
		var p struct {
			Title    string       `json:"title"`
			Detail   string       `json:"detail"`
			Instance string       `json:"instance"`
			Code     string       `json:"code"`
			Errors   []FieldError `json:"errors"`
		}
		if json.Unmarshal(body, &p) == nil {
			e.Code, e.Title, e.Detail, e.Instance, e.Fields = p.Code, p.Title, p.Detail, p.Instance, p.Errors
		}
	}
	return e
}
