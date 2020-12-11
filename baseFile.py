with open('referat.txt', 'r', encoding='utf-8') as f1, open('referat2.txt', 'w', encoding='utf-8') as f2:
    text = f1.read().replace('.', '!')
    text2 = text.split()
    print(text)
    print(len(text))
    print(len(text2))
    f2.write(text)
