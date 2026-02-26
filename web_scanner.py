import requests
from bs4 import BeautifulSoup
def get_page_title_bs(url):
  headers=("User-Agent":'Mozila/5.0(windows NT 10.0 ;win64;x64)Applewebkit/537.36')#模拟浏览器访问防止反爬虫
  response=requests.get(url,timeout=5) #使用get方法发送请求，设置超时时间为五秒，5秒没响应就报错
  response.raise_for_status() #检查状态码如果不为200则报错
  soup=BeautifulSoup(response.content,'html.parser') #创建BeautifulSoup对象解析返回的HTML，response.content服务器返回的原始二进制内容，html.parser使用python内置的html解释器
  title_tag=soup.find('title')  #查找第一个title标签，如果没有返回NONE
  if tatle_tag:#如果找到了title
    title=title_tag.text.strip()  #。text是获取标签内的文本内容，strip是去掉文本首尾的空格和换行
    title=''.join(title.split())   #去掉所有空格
    return title
  return None
  title_url=""https://www.google.com"
  title=get_page_title_bs(title_url)
  print(f"网页标题为：{title}")
  
