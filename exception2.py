def discounted(price, discount, max_dicsount=20, name=''):
    while True:
     try:
         price = abs(float(price))
         discount = abs(float(discount))
         max_dicsount = abs(float(max_dicsount))
         if max_dicsount > 99:
             raise ValueError("Слишком большая скидка")
         if discount >= max_dicsount or 'iphone' in name.lower() or not name:
             return price
         else:
             return price - (price * discount / 100)
     except (ValueError, TypeError):
         print('Ошибка ввода данных числа')
         break

print(discounted(500, 10))
print(discounted(500, "10"))
print(discounted("500", "15.5"))
print(discounted("пятьсот", "десять"))
print(discounted("пятьсот", 5))