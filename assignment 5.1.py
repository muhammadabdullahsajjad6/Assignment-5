#Q2: Singleton Metaclass
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            print(f"Creating new instance of {cls.__name__}")
        return cls._instances[cls]

# Example usage:
class SingletonClass(metaclass=SingletonMeta):
    pass

obj1 = SingletonClass()  # Output: Creating new instance of SingletonClass
obj2 = SingletonClass()  # No output, as the instance already exists

