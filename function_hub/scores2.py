dicts = {'张虹': {'语文': 97, '数学': 87, '英语': 89},
                   '李希': {'语文': 86, '数学': 91, '英语': 93},
                   '王京': {'语文': 89, '数学': 89, '英语': 91}
                   }

#定义函数，计算总成绩并增添到字典中，最后打印字典
def scores_sum(students_scores):
    for name in students_scores:
        #按名字作为键，提取某个学生的成绩字典并赋值给临时变量；
        student_info = students_scores[name]
        #在临时变量上增添一个新键值对，新的键值对的值由该学生的三个科目成绩相加得到
        student_info['总成绩'] = student_info['语文'] + student_info['数学'] + student_info['英语']
    #把整个字典打印出来看看
    print(students_scores)


#传入参数，调用函数
scores_sum(dicts)
