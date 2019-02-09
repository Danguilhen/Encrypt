import os
os.chdir("c:/Users/User/Desktop 2") #Choose the location in your computer

reponse = input("Do you want to encrypt (c) or decrypt (d)?\n")
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','à','é','è','.',',','1','2','3','4','5','6','7','8','9','0',' ','!','?',':','/','\'',')','(','*']
if reponse == 'c':
    mon_fichier = open("Journal.txt", "r") #Choose the notepad you want to open
    contenu = mon_fichier.read()
    contenu = contenu.lower()
    i = 0
    a = 0
    m = 1
    n = 1
    newContenu = str()
    while i < len(contenu):
        try:
            newContenu = alphabet[(n + alphabet.index(contenu[i:i+1])) % len(alphabet)] + newContenu
            a = m
            m = n
            n = (n + a) % len(alphabet)
        except:
            newContenu = contenu[i:i+1] + newContenu
        i = i + 1
    mon_fichier.close()
    mon_fichier = open("journal.txt", "w")
    mon_fichier.write(newContenu)
    mon_fichier.close()
elif reponse == 'd':
    mon_fichier = open("Journal.txt", "r")
    contenu = mon_fichier.read()
    contenu = contenu.lower()
    i = 0
    a = 0
    b = 0
    c = 0
    m = 1
    n = 1
    newContenu = str()
    while i < len(contenu):
        try:
            c = alphabet.index(contenu[i:i+1])
            b = b + 1
        except:
            pass
        i = i + 1
    i = 0
    while i < b - 1:
        a = m
        m = n
        n = n + a
        i = i + 1
    i = 0
    while i < len(contenu):
        try:
            newContenu = alphabet[(alphabet.index(contenu[i:i+1]) - n) % len(alphabet)] + newContenu
            a = n
            n = m
            m = a - m
        except:
            newContenu = contenu[i:i+1] + newContenu
        i = i + 1
    mon_fichier.close()
    mon_fichier = open("journal.txt", "w")
    mon_fichier.write(newContenu)
    mon_fichier.close()
