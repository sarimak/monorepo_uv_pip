# Python Monorepo based on uv pip

Example of monorepo structure and internal dependency management using `uv pip`.

Services in `svc` may import from libraries in `lib` or from up to one cross-service shared folder in `shared`.
Libraries can import from other libraries. Shared folder can import from libraries.

Source code of (domain-agnostic, highly reusable) libraries in `lib` is copied into Docker images of all services.
3rd-party dependencies of those libraries are however installed only when needed.

## Development Setup

```bash
uv venv
source .venv/bin/activate
uv pip sync constraints.txt
```

## Run a Service

```bash
source .venv/bin/activate
./run.py my_web_service
```

## Run Tests

```bash
source .venv/bin/activate
py.test
```

## Upgrade Packages

```bash
rm -rf .venv
uv venv
source .venv/bin/activate
uv pip install -r requirements.in
uv pip compile --generate-hashes --emit-index-url --universal requirements.in > constraints.txt
find svc -type d -exec sh -c 'for req in "$0"/*/requirements.in; do [ -f "$req" ] && uv pip compile --generate-hashes --emit-index-url --universal "$req" > "${req%.in}.txt"; done' {} \;
```

## Build Docker Images

```bash
docker build --build-arg service_name=my_web_service --build-arg shared_folder=my_models -t my_web_service .
docker build --build-arg service_name=my_kafka_consumer --build-arg shared_folder=my_models -t my_kafka_consumer .
```
