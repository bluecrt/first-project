import csv

# 输入个人信息的函数
def input_alumni():
    name = input('请输入同学的姓名：')
    live = input('请输入同学所在城市：')
    telephone = input('请输入同学联系方式：')
    # 以元组的形式返回
    return name, live, telephone

# 创建同学录并写入
def csv_writer(file_name, result):
    with open(file_name, 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['同学名称', '所在地', '联系方式'])
        writer.writerow({'同学名称': result[0], '所在地': result[1], '联系方式': result[2]})

# 读取同学录
def csv_reader(file_name):
    f = open(file_name, 'r', encoding='utf-8')
    reader = csv.DictReader(f)
    return reader

# 定义查询功能的函数
def find(file_name):
    find_name = input('你要找哪位同学的信息呢：')
    print('-'*40 + '\n正在查找···\n')
    for row in csv_reader(file_name):
        if find_name == row['同学名称']:
            print('同学名称：{} 所在地：{} 联系方式：{}'.format(row['同学名称'], row['所在地'], row['联系方式']))
            break
    else:
        print('查无此人')
    print('-' * 40)

# 定义展示同学录信息的函数
def show_info(file_name):
    print('现在有{}位同学在同学录中'.format(len(list(csv_reader(file_name)))))
    print('-' * 40 + '风变同学录' + '-' * 40)
    for row in csv_reader(file_name):
        print('同学名称：{} 所在地：{} 联系方式：{}'.format(row['同学名称'], row['所在地'], row['联系方式']))

# 进入主程序，欢迎界面，循环询问是否录入同学录
def main():
    print('欢迎进入同学录小程序')
    start = input('请问是要创建新csv文件，还是打开已有csv文件？（回答创建或打开）：')
    file_name = input('请输入csv文件名（以文件名.csv的格式写入）：')

    with open(file_name, 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['同学名称', '所在地', '联系方式'])
        if start == '创建':
            # 写入列标题，即DictWriter构造方法的fieldnames参数
            writer.writeheader()
        elif start == '打开':
            print('已打开{}文件。'.format(file_name))

    answer = input('现在可以开始录入同学录么？（回答y开始录入，回答t显示目前同学录，回答f寻找个人信息，输入q退出程序）：')
    
    while True:
        if answer == 'y':
            result = input_alumni()
            csv_writer(file_name, result)
        elif answer == 't':
            show_info(file_name)
        elif answer == 'f':
            find(file_name)
        elif answer == 'q':
            break
        answer = input('还录入同学录么？（回答y继续录入，回答t显示目前同学录，回答f寻找个人信息，回答q退出录入）：')
    print('\n录入结束\n')

# 调用函数
main()