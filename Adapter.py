# Interface esperada pelo cliente
class Target:
    def request(self):
        pass


# Classe existente que precisa ser adaptada
class Adaptee:
    def specific_request(self):
        return "Requisição específica."


# Adaptador que converte a interface do Adaptee para a interface do Target
class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()


# Uso do adaptador
adaptee = Adaptee()
adapter = Adapter(adaptee)
print(adapter.request())
