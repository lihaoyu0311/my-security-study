import pandas as pd
#加载我们的情报（数据集）
df = pd.read_csv('cybersecurity_intrucsion_data.csv')
#执行侦察：看看数据规模
print("[情报信息]")
print(f"数据总行数（记录数）：{df.shape[0]}")
print(f"数据中总列数（特征数）：{df.shape[1]}")\
print("\n前几条记录预览：")
print(df.head())
tcp_records=df[df['protocol'] == 'tcp']
print(f"tcp的协议记录共有：{tcp_records.shape[0]}")
print(f"tcp_records.head()")
