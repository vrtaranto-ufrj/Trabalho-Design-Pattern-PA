# Interface do manipulador
class Handler:
    def set_next(self, handler):
        pass

    def handle(self, request):
        pass


# Implementação base do manipulador
class AbstractHandler(Handler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


# Manipuladores concretos
class MonkeyHandler(AbstractHandler):
    def handle(self, request):
        if request == "Banana":
            return f"Monkey: I'll eat the {request}."
        return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request):
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}."
        return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request):
        if request == "Bone":
            return f"Dog: I'll eat the {request}."
        return super().handle(request)


# Uso da cadeia de responsabilidade
monkey = MonkeyHandler()
squirrel = SquirrelHandler()
dog = DogHandler()

monkey.set_next(squirrel).set_next(dog)

requests = ["Nut", "Banana", "Bone"]

for request in requests:
    result = monkey.handle(request)
    if result:
        print(result)
    else:
        print(f"{request} was left untouched.")
