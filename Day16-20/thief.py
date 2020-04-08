"""

     贪婪法例子：假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品。

     |  名称  | 价格（美元） | 重量（kg） |
     | :----: | :----------: | :--------: |
     电脑 200 20    
     收音机 20 4     
     钟 175 10    
     花瓶 50 2     
      书 10 1     
      油画 90 9      |

"""

class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self._name = name
        self._price = price
        self._weight = weight
    
    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def weight(self):
        return self._price

    @property
    def value(self):
        return self._price / self._weight
    
def input_thing():
    """输入物品信息"""
    print('请输入物品信息: ')
    name_str , price_str , weight_str = input().split()
    return name_str, int(price_str) , int(weight_str)
True
def main():
    """主函数"""
    print('请输入最大重量，物品数量')
    max_weight , num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x : x.value , reverse = False)
    for thing in all_things:
        print(thing.name)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值: {total_price}美元')
         
if __name__ == '__main__':
     main()