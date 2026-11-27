package mdmsdk

import (
	"os"
	"path/filepath"
	"sort"
	"testing"

	"gopkg.in/yaml.v3"
)

// TestMethodsCoverContract: every public operation has an SDK method, and
// every method names a public operation.
func TestMethodsCoverContract(t *testing.T) {
	var doc struct {
		Paths map[string]map[string]yaml.Node `yaml:"paths"`
	}
	read(t, filepath.Join("openapi", "openapi.yaml"), &doc)
	ops := map[string]bool{}
	for _, item := range doc.Paths {
		for method, node := range item {
			if method == "parameters" {
				continue
			}
			var op struct {
				OperationID string `yaml:"operationId"`
			}
			if err := node.Decode(&op); err != nil {
				t.Fatal(err)
			}
			ops[op.OperationID] = true
		}
	}
	var methods map[string]struct {
		Service string `yaml:"service"`
		Method  string `yaml:"method"`
	}
	read(t, "methods.yaml", &methods)
	var missing, extra []string
	for id := range ops {
		if _, ok := methods[id]; !ok {
			missing = append(missing, id)
		}
	}
	seen := map[string]string{}
	for id, m := range methods {
		if !ops[id] {
			extra = append(extra, id)
		}
		key := m.Service + "." + m.Method
		if other, dup := seen[key]; dup {
			t.Errorf("%s and %s both map to %s", id, other, key)
		}
		seen[key] = id
	}
	sort.Strings(missing)
	sort.Strings(extra)
	if len(missing) > 0 {
		t.Errorf("public operations with no methods.yaml entry: %v", missing)
	}
	if len(extra) > 0 {
		t.Errorf("methods.yaml entries with no public operation: %v", extra)
	}
}

// TestScenariosParse: every scenario file is well formed.
func TestScenariosParse(t *testing.T) {
	files, err := filepath.Glob(filepath.Join("scenarios", "*.yaml"))
	if err != nil || len(files) == 0 {
		t.Fatalf("no scenarios: %v", err)
	}
	for _, f := range files {
		var s struct {
			Name string `yaml:"name"`
			Call struct {
				Operation string `yaml:"operation"`
			} `yaml:"call"`
			Responses []struct {
				Status int `yaml:"status"`
			} `yaml:"responses"`
			Expect struct {
				Attempts int `yaml:"attempts"`
			} `yaml:"expect"`
		}
		read(t, f, &s)
		if s.Name == "" || s.Call.Operation == "" || len(s.Responses) == 0 || s.Expect.Attempts == 0 {
			t.Errorf("%s: needs name, call.operation, responses, expect.attempts", f)
		}
		if s.Expect.Attempts > len(s.Responses) {
			t.Errorf("%s: expects %d attempts but scripts %d responses", f, s.Expect.Attempts, len(s.Responses))
		}
	}
}

func read(t *testing.T, path string, v any) {
	t.Helper()
	raw, err := os.ReadFile(path) // #nosec G304 -- the repository's own files
	if err != nil {
		t.Fatal(err)
	}
	if err := yaml.Unmarshal(raw, v); err != nil {
		t.Fatalf("%s: %v", path, err)
	}
}
