# Go and Python SDKs for the mdm API.

default:
    @just --list

# Regenerate both SDKs from openapi/openapi.yaml and methods.yaml.
gen:
    go generate ./api
    go run ./internal/cmd/gen
    cd python && python contract.py
    cd python && openapi-python-client generate --path .contract.yaml --config openapi-python-client.yaml --meta none --output-path src/mdmsdk/_gen --overwrite
    cd python && python gen.py

# Run every test.
test:
    go test -race -count=1 ./...
    cd python && python -m pytest -q

# Lint Go and Python.
lint:
    gofmt -l . | (! grep .)
    go vet ./...
    golangci-lint run ./...
    cd python && ruff check . && pyright
