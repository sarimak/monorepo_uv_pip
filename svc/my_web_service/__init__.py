import fastapi

from lib.http_client import HTTPClient
from lib.web_service import WebService
from shared.my_models import MyMessage


class MyWebService(WebService):
    def __init__(self, name: str) -> None:
        super().__init__(name)

        self.client = HTTPClient()

        router = fastapi.APIRouter()
        router.add_api_route(self.name, self.root, methods=["GET"])
        self.app.include_router(router)

    def root(self, request: MyMessage) -> fastapi.Response:
        return request.name, 200


def run() -> None:
    MyWebService("/").run()
