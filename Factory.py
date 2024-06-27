# Interface do produto
class Product:
    def operation(self):
        raise NotImplementedError()


# Implementações concretas do produto
class ConcreteProductA(Product):
    def operation(self):
        return "Resultado do ConcreteProductA."


class ConcreteProductB(Product):
    def operation(self):
        return "Resultado do ConcreteProductB."


# Fábrica
class Creator:
    def factory_method(self):
        raise NotImplementedError()

    def some_operation(self):
        product = self.factory_method()
        return product.operation()


class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()


# Uso da fábrica
creator = ConcreteCreatorA()
print(creator.some_operation())

creator = ConcreteCreatorB()
print(creator.some_operation())
