# TODO-1: Add Supervisor class Here
# TODO-1: Add .sample() classmethod for Supervisor which returns an instance:

class Supervisor:
    def __init__(self, name, password, phone_number, *args, **kwargs):
        self.name = name
        self.password = password
        self.phone_number = phone_number
        super().__init__(*args, **kwargs)

    @classmethod
    def sample(cls, name='pemi', password='125521', phone_number='9351254664'):
        return cls(name=name, password=password, phone_number=phone_number)
