from pymilvus import MilvusClient


class MelvisClient:
    def __init__(self) -> None:
        self.client = MilvusClient(uri="http://localhost:19530")

    def client(self):
        return self.client
