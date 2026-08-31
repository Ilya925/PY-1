with open('code.txt', encoding='utf-8') as f:
    s = f.read()
    key = input('ВВедите ключ шифрования: ')
    secret = ''
    for symbol in s:
        code = ord(symbol) - int(key)
        decode = chr(code)
        secret += decode
print('текст расшифрован!')
with open('decode.txt', 'w', encoding='utf-8') as f:
    f.write(f'{secret}')
    print('Файл code.txt к прочтению готов!')