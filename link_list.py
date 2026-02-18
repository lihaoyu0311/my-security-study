# 这是我的第一个链表节点
class Node:#定义一个node类
  def _init_(self, data):
    self.data=data#将传入的data参数保持到self.data
    self.next=None#设置next属性为none空值
node1=Node("我的第一个安全节点")#将我的第一个安全节点作为node的data参数并让node1引用这个新创建的节点
print(f"节点数据:{node1.data}")
print(f"下一个节点:{node1.text}")
    
