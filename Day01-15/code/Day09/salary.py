from abc import ABCMeta, abstractclassmethod

class Employee(object, metaclass=ABCMeta):
    """ 员工"""

    def __init__(self, name):
        """初始化方法
        :param name: 姓名
        """
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractclassmethod
    def get_salary(self):
        """
        获得月薪

        :return: 月薪
        """
        pass

class Manager(Employee):
    """部门经理"""
    
    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour
    
    @working_hour.setter
    def working_hour(self,working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 150 * self._working_hour

class Saleman(Employee):
    """销售"""

    def __init__(self,name,sales=0):
        super().__init__(name)
        self._sales = sales
    
    @property
    def sales(self):
        return self._sales
    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05

def main():
    emps = [
        Manager('刘备'), Programmer('诸葛亮'),
        Manager('曹操'), Saleman('荀彧'),
        Saleman('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input('请输入%s本月工作时间: ' % emp.name))
        elif isinstance(emp, Saleman):
            emp.sales = float(input('请输入%s本月销售额： ' % emp.name))
        print('%s本月工资为： ￥%s元' % (emp.name , emp.get_salary()))

if __name__ == '__main__':
    main()