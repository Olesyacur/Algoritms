"""
Помогите Васе понять, будет ли фраза палиндромом‎.
Учитываются только буквы и цифры, заглавные и строчные буквы считаются
одинаковыми.

Решение должно работать за O(N), где N — длина строки на входе.

Формат ввода
В единственной строке записана фраза или слово.
Буквы могут быть только латинские.
Длина текста не превосходит 20000 символов.

Фраза может состоять из строчных и прописных латинских букв,
цифр, знаков препинания.

Формат вывода
Выведите «True», если фраза является палиндромом, и «False»,
если не является."""
import string

phrase = input().lower()
for p in string.punctuation:
    if p in phrase:
        phrase = phrase.replace(p, '')
if ' ' in phrase:
    phrase = phrase.replace(" ", "")

if list(phrase) == list(phrase[::-1]):
    print('True')
else:
    print('False')
