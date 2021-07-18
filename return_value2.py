def proposal (name, age):
    if age >= 18:
        return f'恭喜你，{name} 你{age}岁了，可以嫁人了，准备好嫁妆，明天去接你回家'
    else:
        return '对不起，{}你才{}岁,你还太小，我不能娶你。'.format(name,age)
print(proposal('王小姐', 14))
print(proposal('王小姐', 19))