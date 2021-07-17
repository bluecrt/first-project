# 学python的年数
py_years = 0
# 阿拉伯数字与中文数字对应字典
numbers_dict = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七', 8: '八', 9: '九', 10: '十'}
# 循环开始
while True:
    strsum = input('请问今年是318几周年？请输入整数，输入0退出:')
    if strsum.isdigit():
        intsum = int(strsum)
        if 5 < intsum:
            if len(strsum) == 1:
                anniversary = numbers_dict[intsum]
            elif len(strsum) == 2:
                if strsum[1:] == '0':
                    anniversary = numbers_dict[int(strsum[:1])] + '十'
                else:
                    anniversary = numbers_dict[int(strsum[:1])] + '十' + numbers_dict[int(strsum[1:])]
            elif len(strsum) == 3:
                print('好好锻炼身体，争取活到三位数以上再说。')
                continue
            elif len(strsum) > 3:
                print('静静，你需要静静:(')
                continue
            print('1、318 {} 周年，感谢有你们。'.format(anniversary))
            py_years = intsum - 6
            if py_years == 0:
                print('2、今年才开始学python,感觉还挺朦胧的。')
            elif py_years <= 1:
                print('2、学python {} 年了，开始有感觉了。'.format(py_years))
            elif 1 < py_years < 5:
                print('2、学python {} 年了，精通python的感觉真好。'.format(py_years))
            else:
                print('2、学python {} 年了，成为python砖家大棒了！'.format(py_years))
        elif 0 < intsum < 6:
            print('那时候还没学python,无法写出这个程序')
        elif intsum == 0:
            break
    else:
        print('请输入整数，谢谢！')
