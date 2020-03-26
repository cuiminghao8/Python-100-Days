from abc import ABCMeta , abstractclassmethod
from random import randint, randrange
from clock import sleep

class Fighter(object, metaclass=ABCMeta):
    """Fighter"""

    # 通过__slots__限定对象可以绑定的成员变量
    __slots__ = ('_name' , '_hp')

    def __init__(self , name , hp):
        """初始化方法
        :param name: 名字
        :param hp: 生命值
        """
        self._name = name
        self._hp = hp
    
    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self,hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0
    
    @abstractclassmethod
    def attack(self, other):
        """攻击 

        :param other: 被攻击对象
        """
        pass

class Ultraman(Fighter):
    """奥特曼"""

    __slots__ = ('_name' , '_hp' , '_mp')

    def __init__(self, name, hp, mp):
        """初始化方法
        :param name:名字
        :param hp: 生命值
        :param mp: 魔法值
        """
        super().__init__(name, hp)
        self._mp = mp
    
    def attack(self, other):
        other.hp -= randint(15, 25)
    
    def huge_attack(self, other):
        """究极必杀技(打掉对方至少50点或四分之三的血)

        :param other: 被攻击的对象

        :return: 使用成功返回True否则返回False
        """        
        
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False
    
    def magic_attack(self, others):
        """魔法攻击

        :param others: 被攻击的群体

        :return: 使用魔法成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        """恢复魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return ('~~~%s Untraman ~~~\n' % self._name + 'HP: %d\n' % self._hp + 'MP: %d\n' % self._mp)


class Monster(Fighter):
    """小怪兽"""
    __slots__ = ('_name', '_hp')

    def attack(self,other):
        other.hp -= randint(10,20)

    def __str__(self):
        return '~~~%s Monster~~~\n' % self._name + 'HP: %d\n ' %self._hp

def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive > 0:
            return True
        else:
            return False
def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster
def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end='')

def main():
    u = Ultraman('cuiminghao', 1000, 120)
    m1 = Monster('direnjie', 250)
    m2 = Monster('baiyuanfang', 500)
    m3 = Monster('wangdachui', 750)
    ms = [m1,m2,m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========round %02d========' % fight_round)
        sleep(1)
        m = select_alive_one(ms)  # 选中一只小怪兽
        skill = randint(1, 10)# 通过随机数选择使用哪种技能
        if skill <= 6: # 60%的概率使用普通攻击
            print('%s used normal attack to %s.' % (u.name , m.name))
            sleep(1)
            u.attack(m)
            print('%s resumed MP for %d points' % (u.name , u.resume()))
            sleep(1)
        elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
            if u.magic_attack(ms):
                print('%s used magic attack ' % u.name)
                sleep(1)
            else:
                print('%s magic failed' % u.name)
                sleep(1)
        else: # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.huge_attack(m):
                print('%s used huge attack to %s' % (u.name , m.name))
                sleep(1)
            else:
                print('%s used normal attack to %s.' % (u.name , m.name))
                sleep(1)
                print('%s resumed MP for %d points' % (u.name , u.resume()))
                sleep(1)
        if m.alive > 0:   # 如果选中的小怪兽没有死就回击奥特曼
            print('%s returned to attack %s' % (m.name , u.name))
            sleep(1)
            m.attack(u)
        display_info(u,ms) # 每个回合结束后显示奥特曼和小怪兽的信息
        sleep(5)
        fight_round += 1
    print('\n=============fight over!==========\n')
    sleep(1)
    if u.alive > 0:
        print('%s Ultraman win' % u.name)
        sleep(1)
    else:
        print('Monsters win')
        sleep(1)

if __name__ == '__main__':
    main()