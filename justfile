# Go and Python SDKs for the mdm API.

default:
    @just --list

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
