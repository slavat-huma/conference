from abc import ABC, abstractmethod


class UseCase(ABC):
    def __init__(self):
        self.request_object = None

    async def execute(self, request_object):
        self.request_object = request_object
        await self.process_request(request_object)

    @abstractmethod
    async def process_request(self, request_object):
        raise NotImplementedError
