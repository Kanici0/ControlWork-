def is_vowel(char):
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return  char in vowels



while True:
    word = input("Введите слово : ")

    if word.lower() == 'stop':
        print('stop!!')
        break

    a = len(word)
    b = sum(1 for char in word if is_vowel(char))
    d =a - b
    c =round ((b / a) * 100,1)
    f = round((d / a) * 100,1)
    print(f"количество букв : {a} ")
    print(f" количество гласных :{b}")
    print(f" количество согласных:{d}")
    print(f" количество согластных и гласных  :{d }  and {b}")
    print(f'просент гласных : {c :} %')
    print(f'просент согластных  : {f :} %')
