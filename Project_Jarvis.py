"""
robot che si presenta, dice la sua età, chiede nome e età dell'interlocutore
interagendo con lui. Alla fine farà il confrontò delle età, dando riscontro se 
l'interlocutore è più grande, più piccolo di lui o hanno la stessà età.
"""

import random

nome_robot = "Jarvis"
età_robot = random.randint(1,50) #estrae un numero random intero da 1 a 50
#esiste anche la funzione che sceglie il passo    

print("Ciao! Io sono ",nome_robot," e ho ",str(età_robot)) #si deve trasformare
#età_robot in str perche non si possono concatenare variabili di tipo diverso

nome_utente = input("Tu come ti chiami? ") #input accoglie sempre una stringa
print ("Ciao " + nome_utente + "! Piacere di conoscerti!")
età_user = int(input ("Quanti anni hai, " + nome_utente + "?")) #aggiungo int all'inizio
#perchè anche se inserisco la mia età come numero, input la prende come str: 
#dopo con l'if non riescirei a fare la comparazione tra variabili di tipo diverso

if età_user > età_robot:
 print ("Sei più grande di me!")
elif età_user < età_robot:
  print ("Sei più piccolo di me!")
else: 
    print("Abbiamo la stessa età!")

