books_dic = {'82年生的金智英': 3, '了不起的盖茨比': 6,
             '乌合之众': 5, '活着': 8, '小王子': 6, '设计的意义': 2}
print(books_dic)
for book in books_dic:
    book_sum = books_dic[book]
    if book_sum > 5:
        print(book)
        books_dic[book] = '分配'
    else:
        books_dic[book] = '自留'
print(books_dic)