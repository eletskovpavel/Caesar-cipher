from statistics import mode


text = input("Введите текст, который хотите зашифровавать/расшифровать: ")
k = int(input("Укажите ключ: "))
language = input("На каком языке текст, который вы ввели (русский, английский): ")
mode = int(input("Введите режим 1 - шифровка, 2 - дешифровка: "))


def ceaser_cipher(user, key, lang):
    res = []
    n = ""
   
    if lang.lower() in ["русский", "russian"]:
        dictionary, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    elif lang.lower() in ["английский", "english"]:
        dictionary, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        return "Такого языка нет в опции"

    for i in range(len(user)):
        if user[i] in dictionary:
            n = dictionary
        elif user[i] in dictionary_upper:
            n = dictionary_upper
        else:
            res.append(user[i])

        if user[i] in n:
            for j in range(len(n)):
                if 0 <= j + key < len(n) and user[i] == n[j]:
                    res.append(n[j + key])
                elif j + key >= len(n) and user[i] == n[j]:
                    res.append(n[(j+key)-len(n)])
                elif j + key < 0 and user[i] == n[j]:
                    res.append(n[len(n)-(j+key)])

    return ''.join(res)

def ceaser_decipher(user, key, lang):
    res = []
    n = ""
   
    if lang.lower() in ["русский", "russian"]:
        dictionary, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    elif lang.lower() in ["английский", "english"]:
        dictionary, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        return "Такого языка нет в опции"

    for i in range(len(user)):
        if user[i] in dictionary:
            n = dictionary
        elif user[i] in dictionary_upper:
            n = dictionary_upper
        else:
            res.append(user[i])

        if user[i] in n:
            for j in range(len(n)):
                if 0 <= j - key < len(n) and user[i] == n[j]:
                    res.append(n[j - key])
                elif j - key >= len(n) and user[i] == n[j]:
                    res.append(n[abs(j-key)-len(n)])
                elif j - key < 0 and user[i] == n[j]:
                    res.append(n[len(n)-abs(j-key)])

    return ''.join(res)

if mode == 1:
    print(ceaser_cipher(text, k, language))
elif mode == 2:
    print(ceaser_decipher(text, k, language))
else:
    print ("Нет такого режима!")