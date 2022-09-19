class Person:
    def __init__(self, firstname, lastname):
        self.__firstname = firstname
        self.__lastname = lastname

    def get_name(self):
        return f'{self.__firstname.capitalize()} {self.__lastname.capitalize()}'


class Student(Person):

    def __init__(self, firstname, lastname, course):
        super().__init__(firstname, lastname)
        self.__course = course

    def get_course(self):
        print(f'{self.get_name()} studies {self.__course}')


if __name__ == '__main__':
    larry = Student('larry', 'smith', 'BA')
    larry.get_course()
