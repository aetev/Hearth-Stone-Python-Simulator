"""
Chain of Responsibility Design Pattern
"""

from abc import ABC  # Abstract Base Class


class Handler(ABC):
    """
    Abstract class for handling requests.
    """

    def __init__(self, successor=None) -> None:
        """
        Constructor for the Handler class.
        args:
        """
        self._successor = successor

    def handle_request(self, request) -> None:
        """
        Abstract method for handling requests.
        """


class ValidationEngine(ABC):
    """
    Abstract class for the validation engine.
    """

    def __init__(self) -> None:
        """
        Constructor for the ValidationEngine class.
        """
        self.handlers = []

    def validate(self, request) -> None:
        """
        Method for validating requests.
        """
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
