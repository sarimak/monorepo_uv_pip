FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

ARG service_name
ENV SERVICE_NAME=$service_name
ARG shared_folder=".placeholder"

COPY svc/${SERVICE_NAME}/requirements.txt requirements.txt
RUN uv venv
ENV PATH=.venv/bin:$PATH
ENV VIRTUAL_ENV=.venv
RUN uv pip sync --require-hashes requirements.txt

COPY run.py run.py
COPY shared/$shared_folder shared/$shared_folder
COPY lib lib
COPY svc/$service_name svc/$service_name

CMD ["./run.py"]
