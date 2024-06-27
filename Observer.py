# Interface do Observador
class Observer:
    def update(self, message: str):
        raise NotImplementedError()


# Interface do Sujeito
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, message: str):
        for observer in self.observers:
            observer.update(message)


# Implementação concreta do Sujeito
class ConcreteSubject(Subject):
    def some_business_logic(self):
        # Lógica de negócio
        self.notify("Estado mudou!")


# Implementação concreta do Observador
class ConcreteObserverA(Observer):
    def update(self, message: str):
        print(f"Observer A: {message}")


class ConcreteObserverB(Observer):
    def update(self, message: str):
        print(f"Observer B: {message}")


# Uso do padrão Observador
subject = ConcreteSubject()
observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()

subject.attach(observer_a)
subject.attach(observer_b)

subject.some_business_logic()
