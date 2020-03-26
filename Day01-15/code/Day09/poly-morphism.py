from abc import ABCMeta , abstractclassmethod

class Pet(object, metaclass=ABCMeta):

    def __init__(self, nickname):
        self._nickname = nickname
    
    @abstractclassmethod
    def make_voice(self):
        pass

class Dog(Pet):

    def make_voice(self):
        print('%s: wangwangwang' % self._nickname)

class Cat(Pet):
     
     def make_voice(self):
         print('%s: miaomiaomiao' % self._nickname)
    

def main():
    pets = [Dog('wangcai'), Cat('ketty'), Dog('dahuang')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()