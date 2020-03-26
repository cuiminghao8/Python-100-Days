class Person(object):

    def __init__(self,name,age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        self._age = age
    
    def play(self):
        print('%s is playing.' % self._name)
    
    def watch_av(self):
        if self._age >= 18:
            print('%s is watching av' % self._name)
        else:
            print('%s is watching cartoon' % self._name)

class Student(Person):
    
    def __init__(self , name , age , grade):
        super().__init__(name,age)
        self._grade = grade
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self,grade):
        self._grade = grade

    def study(self,course):
        print('%s of %s is studying %s'  % (self._name , self._grade , course))

class Teacher(Person):
    def __init__(self , name , age , title):
        super().__init__(name, age)
        self._title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self , title):
        self._title = title

    def teach(self, course):
        print('%s %s is teaching %s' % (self._name , self._title , course))


def main():
    stu = Student('wangdachui' , 15 , 'grade 3')
    stu.study('math')
    stu.watch_av()
    t = Teacher('cuiminghao' , 38 , 'professor')
    t.teach('python')
    t.watch_av()
    
if __name__ == '__main__':
    main()