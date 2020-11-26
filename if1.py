age = int(input('Ваш возраст: '))

def profile(age):
    if  1 <= age <= 5:
        return 'Должен ходить в садик'
    elif 6 <= age <= 17:
        return 'Должен учиться в школе'
    elif 18 <= age <= 65:
        return 'Должен учиться в ВУЗе или работать'

print(profile(age))
