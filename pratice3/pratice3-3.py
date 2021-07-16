chinese = [55, 60, 95, 90, 88, 87, 61, 59, 78, 90]
math = [66, 77, 90, 99, 58, 69, 77, 88, 82, 95]
english = [100, 98, 66, 43, 66, 47, 91, 67, 89, 59]
scores = [chinese, math, english]
over_sixty = []
over_sixty_sum = 0
for score in scores:
    for score_single in score:
        if score_single >= 60:
            over_sixty.append(score_single)
            over_sixty_sum += 1
print('这就是60分及以上的分数，总共{}个及格分:'.format(str(over_sixty_sum)))
print(over_sixty)


