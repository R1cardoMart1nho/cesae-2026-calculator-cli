FROM python:3.14-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:0.11.24 /uv /uvx /bin/

COPY . /app

ENV UV_NO_DEV=1

WORKDIR /app
RUN uv sync --locked

CMD ["uv", "run", "calculator"]
