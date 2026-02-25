class FINEqueuq:
  def __init__(self):
    self.queue=[]  #将self.queue定义为列表
  def enqueue(self,item): #创建入队
    self.queue.append(item)
  def dequeue(self):  #创建出队，先判断队伍是否为空
    if self.is_empty():
      return 0
    return self.queue.pop(0)
  def is_empty(self):  #判断队伍是否为空
    return len(self.queue) == 0
q=FINEqueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.queue)

  
    
  
