text = input("Введите текст, который хотите зашифровавать: ")
k = int(input("Укажите ключ: "))
language = input("На каком языке текст, который вы ввели (русский, английский): ")


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
                    res.append(n[(1 - j - key) % (len(n) - 1)])
                elif j + key < 0 and user[i] == n[j]:
                    res.append(n[(j + key) % len(n)])

    return ''.join(res)


print(ceaser_cipher(text, k, language))