def Lettercases(Word):  # Получаем слово как аргумент
    up = 0
    low = 0
    for i in Word:  # Проходимся по символам слова
        if i.isupper():  
            up += 1
        elif i.islower():  
            low += 1
    return f'Upper case letters = {up}, Lower case letters = {low}'
