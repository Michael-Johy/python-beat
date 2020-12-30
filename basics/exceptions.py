try:
    print('try...')
    r = 10 / 0
    int('1')
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('end')
