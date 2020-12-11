
def expl(line_one, line_two):
    if type(line_one) and type(line_two) is not str:
        return('0')
    elif line_one == line_two:
        return '1'
    elif line_one != line_two and len(line_one) > len(line_two):
        return '2'
    elif line_one != line_two and line_two == 'learn':
        return '3'
    

print(expl('Hello', 1))
print(expl('Hello', 'Hello'))
print(expl('Hello', 'world'))
print(expl('Hello my', 'world'))
print(expl('Python', 'learn')) # не разобрался как исправить
print(expl('My', 'learn'))

