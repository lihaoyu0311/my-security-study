attack_db={"sqli":"sql注入","xxs":"跨站脚本攻击"}#建造一个字典其有对应的键值对
a=input("\n请输入正确的缩写：")#用户输入对对应的键
if a in attack_db:#判断输入的是否在字典中
  b=attack_db[a]
  print(f"{b}")
else :
  print(f"请输入正确的缩写")
