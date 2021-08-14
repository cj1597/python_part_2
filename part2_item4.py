class Person:
    """Contains method for returning gender"""
    gender = ''

    def get_gender(self):
        """Returns person's gender"""
        return self.gender


class Male(Person):
    """A Male person"""
    gender = 'Male'


class Female(Person):
    """A Female person"""
    gender = 'Female'


if __name__ == '__main__':
    print(Male().get_gender())
    print(Female().get_gender())
