scores = {'小李': [95, 98, 90], '小花': [96, 90, 94],
          '小华': [85, 80, 90], '小胖': [87, 94, 89],
          '小红': [79, 85, 90], '小吴': [99,100,101]}
#print (scores)

for name in scores:
    #print(name)
    scores_list = scores[name]
    #print(name+ str(scores_list))
    scores_sum = 0
    i= 0
    for i in scores_list:
        scores_sum += i
    print('{}同学的总分是:{}分,平均分是{}。'.format(name,scores_sum, int(scores_sum/3)))

ch_sum =0
ma_sum =0
en_sum =0
count =0
for name in scores:
    ch_sum += scores[name][0]
    ma_sum += scores[name][1]
    en_sum += scores[name][2]
    count += 1
print('语文的平均分是{}分'.format(int(ch_sum/count)))
print('数学的平均分是{}分'.format(int(ma_sum/count)))
print('英语的平均分是{}分'.format(int(en_sum/count)))