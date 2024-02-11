"""Строка ввода"""
stroka = input()

def zagl(stroka):
    """Строка делает буквы заглавными"""
    stroka1 = stroka.upper()
    """Вывод"""
    return stroka1

def zagl1(stroka):
    """
    Функция делает заглавными первые буквы каждого слова в строке.
    """
    return ' '.join(word.capitalize() for word in stroka.split())

# Вызываем функции с передачей аргумента stroka
print(zagl(stroka))
print(zagl1(stroka))
