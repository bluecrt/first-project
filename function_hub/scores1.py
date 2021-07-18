students_scores = {
    '张虹': {'语文': 97, '数学': 87, '英语': 89},
    '李希': {'语文': 86, '数学': 91, '英语': 93},
    '王京': {'语文': 89, '数学': 89, '英语': 91},
}

for name in students_scores:
    scores_info = students_scores[name]
    scores_info['总成绩'] = scores_info['语文'] + scores_info['数学'] + scores_info['英语']
    print(name + ':',scores_info)
print (students_scores)    