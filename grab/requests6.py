# 结合所学知识，根据代码注释填充代码。
# 导入Requests库
import requests
# 向闪光读书网页的URL发送网络请求，并把响应结果赋值在变量res上
res = requests.get('https://wp.forchange.cn/psychology/11069/')
# 打印响应的状态码
print(res.status_code)
# 使用枚举法先将响应内容的编码格式设置为utf-8
res.encoding = 'utf-8'
# 调用Response对象的text属性，获取响应内容
text = res.text
# 打印响应内容
print(text)