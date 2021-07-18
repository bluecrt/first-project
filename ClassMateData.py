
print('欢迎进入同学录小程序')
students_info = {}
student_single = {}
students_list = []
number = 0
start = input('现在可以开始录入同学录么？（回答y开始录入，输入q退出程序):')
while start == 'y':
    number += 1
    name = input('请输入同学的姓名：')
    city = input('请输入同学所在城市：')
    phone = input('请输入同学联系方式：')
    student_single['姓名'] = name
    student_single['所在城市'] = city
    student_single['联系方式'] = phone
     
    #print(students_info)
    students_info[number] = student_single
    start = input('还录入同学录么？（回答y继续录入，回答t显示目前同学录，回答其它退出录入：')
    if start == 'y':
        continue
    elif start == 't':
        print(students_info)
    else:
        print('录入结束')
    
#elif start == 'q':
print('欢迎使用同学录，下次见!')
