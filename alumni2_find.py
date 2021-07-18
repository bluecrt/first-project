import time
# 定义同学录
alumni = {}

# 输入个人信息的函数
def input_alumni():
    name = input('请输入同学的姓名：')
    live = input('请输入同学所在城市：')
    telephone = input('请输入同学联系方式：')
    # 以元组的形式返回
    return name, live, telephone

# 同步个人信息到同学录的函数
def create_alumni(result):
    # 添加新的个人信息到同学录字典中
    alumni[result[0]] = result[1:]

# 定义查询功能的函数
def find():
    find_name = input('你要找哪位同学的信息呢：')
    print('-'*40 + '\n正在查找···\n')
    time.sleep(1)
    if find_name in alumni:
        print('同学名称：{} 所在地：{}   联系方式：{}'.format(find_name, alumni[find_name][0], alumni[find_name][1]))
    else:
        print('查无此人')
    print('-' * 40)

# 定义展示同学录信息的函数
def show_info():
    print('现在有{}位同学在同学录中'.format(len(alumni)))
    print('-' * 40 + '风变同学录' + '-' * 40)
    for i in alumni:
        print('同学名称：{} 所在地：{} 联系方式：{}'.format(i, alumni[i][0], alumni[i][1]))

# 进入主程序，欢迎界面，循环询问是否录入同学录
def main():
    print('欢迎进入同学录小程序')
    answer = input('现在可以开始录入同学录么？（回答y开始录入，回答t显示目前同学录，回答f寻找个人信息，输入q退出程序）：')

    while True:
        if answer == 'y':
            result = input_alumni()
            create_alumni(result)
        elif answer == 't':
            show_info()
        elif answer == 'f':
            find()
        elif answer == 'q':
            break
        answer = input('还录入同学录么？（回答y继续录入，回答t显示目前同学录，回答f寻找个人信息，回答q退出录入）：')
    print('\n录入结束\n')

# 调用函数
main()