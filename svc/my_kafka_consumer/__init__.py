import pydantic

from lib.kafka_consumer import KafkaConsumerService


class MyMessage(pydantic.BaseModel):
    name: str


class MyConsumerService(KafkaConsumerService):
    def __init__(self, name: str) -> None:
        super().__init__(name)

        self.handlers[name] = self.handler

    def handler(self, message: dict) -> None:
        print(message)


def run() -> None:
    MyConsumerService("my_message").run()
