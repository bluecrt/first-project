left_chance = 5
while True:
    key_password = input('请输入密码以结束循环,你还有' + str(left_chance)+'次机会：')
    if key_password == '198764':
        print('密码正确，门已打开')
        break
    else:
        left_chance -= 1
        if left_chance == 0:
            print('5次循环你都错过了！')
            break
