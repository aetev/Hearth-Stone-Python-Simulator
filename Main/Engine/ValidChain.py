class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        pass


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


class ValidationEngine:
    def __init__(self):
        handlers = (
            ConcreteHandler1(),
            ConcreteHandler2(),
            ConcreteHandler3(),
        )

        for i in range(len(handlers) - 1):
            handlers[i]._successor = handlers[i+1]

        self._handler = handlers[0]

    def validate(self, request):
        self._handler.handle_request(request)


# Usage example
engine = ValidationEngine()
engine.validate("request1")
engine.validate("request2")
engine.validate("request3")
