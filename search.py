


w = 'Иванов'
f = open('date_base\db.csv', encoding='utf-8')
text = f.read()
f.close()
c = text.count(w)
while c > 0:
    print(w)
    c -= 1
