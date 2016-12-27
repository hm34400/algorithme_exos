#retrouver le caractere
#By Hicham
#beWeb

word = "monstrueux"
char = "c"
resultat = 0
i = 0

#tant que i est inferieur a la longueur du mot
while i < len(word) :
    #si la lettre a l'index i est egale a la lettre de la variable char
	if word[i] == char :
        #si a l'index ou je me trouve c'est bien un "n" j'incremente de 1
		result += 1
	i += 1
    #et je passe a l'index suivant
print ("le nombre de caractereRecherche est : " + str(resultat))