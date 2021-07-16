for i  in range (1,9):
    for j in range (1,i+1):
        #sums = j*i
        print(str(j) + 'X'+ str(i)+ '=' + str(j*i), end= '\t')
    print()