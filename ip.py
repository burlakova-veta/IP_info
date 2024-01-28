def Check(ip):
    for i in s:
        if 0 <= int(i) <= 255:
            result = True
        else:
            return False
    return result

def defineMask(mas):
    div = mas // 8
    mod = mas % 8
    ms = '255.'*div
    sum = 0
    for i in range(1, mod+1):
        sum+= pow(2, 8-i)
    ms+= str(sum)
    return ms

def defineClass(s):
    if 0 <= s <= 127:
        return 'A'
    elif 128 <= s <= 191:
        return 'B'
    elif 192 <= s <= 223:
        return 'C'
    elif 224 <= s <= 239:
        return 'D'
    elif 240 <= s <= 255:
        return 'E'

def defineType(s):
    if int(s[0]) == 10:
        return 'Локальный'
    elif int(s[0]) == 172 and 16 <= int(s[1]) <= 31:
        return 'Локальный'
    elif int(s[0]) == 192 and int(s[1]) == 168:
        return 'Локальный'
    else:
        return 'Глобальный'

ip = input("Введите IP адрес: ")
s = ip.split('.')
while not Check(s):
    ip = input("Ошибка в данных\nВведите IP адрес: ")
    s = ip.split('.')
mas = int(input("Введите маску сети: "))

s1 = s[0] + '.' + s[1] + '.' + s[2] + '.'
uz = pow(2, 32-mas) - 2

print('\nIP адрес:', ip)
print('Маска сети:', defineMask(mas))
print('IP адрес сети:', s1+'0')
print('IP адрес широковещания:', s1+'255')
print('Количество узлов:', uz)
print('Класс IP адреса:', defineClass(int(s[0])))
print('Тип IP адреса:', defineType(s))