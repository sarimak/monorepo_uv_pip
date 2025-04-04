import kafka  # noqa: F401

from lib.common import Service


class KafkaConsumerService(Service):
    def __init__(self, name: str) -> None:
        super().__init__(name)

        self.consumer = [{"name": "my_message"}]  # Fake KafkaConsumer
        self.handlers = {}

    def run(self) -> None:
        for message in self.consumer:
            handler = self.handlers[message["name"]]
            handler(message)
