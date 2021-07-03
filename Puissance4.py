from tkinter import *
#note le tableau partie commence à 0 et le tableau Hauteur à 1

#####Affichage du plateau
def Initplateau():
    i = 0
    for i in range(0,9):
        plateau.create_line(100*i,0, 100*i, 700, fill="black")
    for i in range(0,9):
        plateau.create_line(0,100*i, 700, 100*i, fill="black")
    print('Initialisation du plateau de jeu')

#####indique quel joueur doit cliquer
def joueur():
    global Tour
    Tour = Tour+1
    Tour = Tour%2
    return Tour

#####Memorise la position du curseur au clic et permet de positioner un pion
def posPion(clic):
    color=['red','blue']
    i = int((clic.x/100))
    j = int((clic.y/100))

    #####Empèche le joueur de perdre un tour en mettant un pion au dessus de la pile 
    if(Hauteur[i]<6):
        Hauteur[i] = Hauteur[i]+1
        resultat = joueur()
        Partie[i][Hauteur[i]] = resultat
    #####Place sur le plateau le pion du joueur
        plateau.create_oval(100 * i, 600-100*Hauteur[i], 100 * i + 100, 700-100*Hauteur[i], fill=color[resultat])

#####Fonction qui permet de déterminer lorsqu'un joueur gagne la partie.
##### Note : On ne peut gagner qu'à partir du 4 coup du premier joueur
#####        Il est inutile de regarder les cases du hauts lorsqu'on cherche les cdts de victoires
#####        Determiner les cdts par rapports à la dernière case posé (C)
#####        Les différents cas horizontaux sont [C,X,X,X], [X,C,X,X], [X,X,C,X] et [X,X,X,C] 
#####        Le cas vertical est de haut en bas  [C,X,X,X]
#####        Les différents cas diagonaux sont [C,X,X,X], [X,C,X,X], [X,X,C,X] et [X,X,X,C] 

######Main
Tour = 0
Hauteur=[0,0,0,0,0,0,0,0]
Partie=[[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[2,2,2,2,2,2,2]]
fenetre = Tk()
plateau = Canvas(fenetre, height=600, width=700, bg="white")

#####Créer une fonction qui affiche un menu avec lancer la partie

Initplateau()
##### Defini le clic souris gauche comme actionneur
plateau.bind("<Button-1>", posPion)
plateau.pack()
fenetre.mainloop()
