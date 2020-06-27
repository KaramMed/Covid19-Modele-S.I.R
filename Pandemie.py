import matplotlib.pyplot as plt

# definir les constantes
population_totale = 40000000
contacts_quotidien = 40
probabilite_transmission = 0.0025
duree_maladie = 30
taux_gerison = 0.7344 # au maroc
taux_morts = 0.0185 # au maroc

# calcul de R0
def R0() :
    return (contacts_quotidien*duree_maladie*probabilite_transmission)

# calcul du taux de transmission
def taux_transmission():
    return contacts_quotidien*probabilite_transmission;

# calcul le nombre de malades du jour suivant
def nouveau_malades(malades,sains,remis,morts):
    # prends le nombre de malades et les sains du jour precedent
    # ainsi que les remis et morts du meme jour
    return malades +  malades * taux_transmission() * (sains/population_totale) - (malades*(taux_gerison/duree_maladie)) - (malades*(taux_morts/duree_maladie))


# calcul le nombre de morts du jour suivant
def nouveau_morts(morts,malades) :
    # prends le nombre de morts et malades du jour precedent
    return morts + (taux_morts/duree_maladie) * malades


# calcul le nombre de guerisons du jour suivant
def nouveau_geurisons(gerisons,malades):
    # prends le nombre de morts et gerisons du jour precedent
    return gerisons + (taux_gerison/duree_maladie) * malades


# Simualation de la propagation pour 30 jours

malades = 4047
morts = 160
gueris = 557
sains = population_totale - malades
jour = 1

# init des listes
jours_malades = list()
jours_morts = list()
jours_guerisons = list()
jours = list()

while (jour<30) :
    malades = int(nouveau_malades(malades,sains,gueris,morts))
    morts = int(nouveau_morts(morts,malades))
    gueris = int(nouveau_geurisons(gueris,malades))
    jours_malades.append(malades)
    jours_morts.append(morts)
    jours_guerisons.append(gueris)
    jours.append(jour)
    #print(jour,' : ',malades,' : ',morts,' : ',gueris)
    jour = jour + 1



# affichage sous matplotlib
plt.plot(jours,jours_malades)
plt.plot(jours,jours_morts)
plt.plot(jours,jours_guerisons)

plt.legend(['Malades', 'Morts', 'Guerisons'], loc='upper left')

plt.show()
