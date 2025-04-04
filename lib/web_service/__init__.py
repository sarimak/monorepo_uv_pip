import fastapi
import uvicorn

from lib.common import Service


class WebService(Service):
    def __init__(self, name: str) -> None:
        super().__init__(name)

        self.app = fastapi.FastAPI()

    def run(self) -> None:
        uvicorn.run(self.app, host="0.0.0.0", port=8000)
