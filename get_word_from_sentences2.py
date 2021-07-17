words = 'I have money.'
ws = ''
words_list = list(words)
words_list2 = words.split(' ')
print(words_list)
print(words_list)
for i in words_list2[:: -1]:
    ws += i+' '
print(ws)