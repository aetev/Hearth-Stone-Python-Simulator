from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        pass


class ValidationEngine(ABC):
    def __init__(self):
        self.handlers = []

    def validate(self, request):
        for handler in self.handlers:
            handler.handle_request(request)


class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if request == "request1":
            print("ConcreteHandler1 handles the request.")
        elif self._successor is not None:
            self._successor.handle_request(request)


class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if request == "request2":
            print("ConcreteHandler2 handles the request.")
        elif self._successor is not None:
            self._successor.handle_request(request)


class ConcreteHandler3(Handler):
    def handle_request(self, request):
        if request == "request3":
            print("ConcreteHandler3 handles the request.")
        elif self._successor is not None:
            self._successor.handle_request(request)


class ConcreteHandler4(Handler):
    def handle_request(self, request):
        if request == "request3":
            print("ConcreteHandler3 handles the request.")
        elif self._successor is not None:
            self._successor.handle_request(request)


class handValidator(ValidationEngine):
    def __init__(self):
        self.handlers = [
            ConcreteHandler1(),
            ConcreteHandler2(),
            ConcreteHandler3(),
            ConcreteHandler4(),
        ]


# Usage example
engine = handValidator()
engine.validate("request1")
engine.validate("request2")
engine.validate("request3")
