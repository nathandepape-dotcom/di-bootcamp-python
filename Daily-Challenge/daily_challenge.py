import random


word = input("Type any word and try to find the perfect length !")
if len(word) > 10:
    print("String too long")
elif len(word) < 10:
    print("String is not long enough")
else :
    print("Perfect string !")
    print(word[0], word[-1])
    chaine = ""
    for n in word :
        chaine += n
        print(chaine)
    lettres = list(word)
    random.shuffle(lettres)
    print("".join(lettres)) 





