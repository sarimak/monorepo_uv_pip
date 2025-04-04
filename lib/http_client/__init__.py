import httpx


class HTTPClient:
    def __init__(self) -> None:
        self.client = httpx.Client(timeout=1)
