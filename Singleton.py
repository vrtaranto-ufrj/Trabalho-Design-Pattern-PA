class SingletonMeta(type):
    _instances = {}

    # Checa se a instância já existe, se não, cria uma nova
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        return "Lógica de negócio do Singleton."


# Uso do Singleton
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # True
print(singleton1.some_business_logic())
