def scores_sum(name, *scores):
    total_scores = 0
    for score in scores:
        total_scores += score
    print(name+'\'total scores is', total_scores) 
scores_sum('jun', 28)
