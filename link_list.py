# 这是我的第一个链表节点
class Node:  # 定义一个node类
    def __init__(self, data):
        self.data = data  # 将传入的data参数保持到self.data
        self.next = None  # 设置next属性为none空值
class Linkedlist:  #定义一个类
    def __init__(self): #将头节点设置为空值
        self.head=None
    def append(self,data): #添加append方法
        new_node=Node(data) #只有node中的数据才是data属性
        if self.head is None:  
            self.head=new_node
        else:
            current =self.head
            while current.next:
                current =current.next
            current.next =new_node
node1 = Node("我的第一个安全节点")  # 将我的第一个安全节点作为node的data参数并让node1引用这个新创建的节点
print(f"节点数据:{node1.data}")
print(f"下一个节点:{node1.next}")
llist=Linkedlist()
print("Linkedlist头节点:",llist.head)
llist.append(1)
llist.append(2)
llist.append(3)
print(f"{llist.head.data}")
print(f"{llist.head.next.data}")

