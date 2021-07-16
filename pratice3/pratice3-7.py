scores = {'小李': [95, 98, 90], '小花': [96, 90, 94],
          '小华': [85, 80, 90], '小胖': [87, 94, 89],
          '小红': [79, 85, 90]}

for name in scores:
    ones_score = scores[name]
    ones_sum= 0

    for sums in ones_score:
        ones_sum =   ones_sum+ sums

    print(name+'同学的总分是{}'.format( ones_sum))
count =0
ch_score =0
ma_score =0
en_score =0
for name in scores:
    ch_score += scores[name][0]
    ma_score += scores[name][1]
    en_score += scores[name][2]
    count += 1
# 打印班级平均分，平均分为总分/人数
print('语文的平均分为{}分\n数学的平均分为{}分\n英语的平均分为{}分'.format(
    ch_score/count, ma_score/count, en_score/count))

         