def crossword(words):
    word_list =[]
    word = '' 
    word_space =''
    words_cross = ''

    for  i in words:
        word += i
        if i == ' ':
            word_space = word
            word = ''
            word_list.append(word_space)
            
    word_list.append(word+' ')
    words_cross_list = (word_list[::-1]) 

    for one in (words_cross_list):
        words_cross += one
    print(words_cross)
#words = input('''Please input english sentences, press enter, 
    #you will find out the words in sentences' positon are inverted:''')
#crossword(words)
#crossword('this is a testing function .')