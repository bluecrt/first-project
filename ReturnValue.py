def get_formal_name(first_name, last_name):
    return f'{first_name.title()} {last_name.title()}'#首字母大写str.title()
fullname = get_formal_name('junwang','wu')    
print(fullname)