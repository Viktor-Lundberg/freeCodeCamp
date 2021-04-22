import copy
import random


class Hat:
    # Skapar Hat. **kwargs tar emot så många argument som användaren skriver in. Lägger detta i en variabel "balls" och skapar en lista "ballist"
    def __init__(self, **kwargs):
        balls = kwargs
        ballist = []

        # Loopar igenom dicten balls och lägger till key-attributet så många gånger som värdet value visar i listan ballist och sätter instansvaribeln "contents" till samma som ballist
        for key, values in balls.items():
            ballist.extend([key for iterator in range(values)])
        self.contents = ballist

    # Skapar draw-metoden som tar ett nummer för antalet bollar som ska dras som argument.
    def draw(self, numberofballstodraw):
        # Skapar en lista att lägga de dragna bollarna i som kan returneras. Samt skapar en lista utifrån self.contents med urvalet av bollar som kan dras
        drawnballs = []
        ballist = self.contents
        ballstodrawiterator = numberofballstodraw

        # Om det är fler eller lika många bollar som ska dras som i bollistan returneras alla bollar
        if numberofballstodraw >= len(ballist):
            return ballist

        # Drar en random-boll och lägger till i listan över dragna bollar och plockar bort den från bollistan så länge antalet bollar som ska dras är högre än 0.
        while ballstodrawiterator > 0:
            ball = random.choice(ballist)
            ballist.remove(ball)
            drawnballs.append(ball)
            ballstodrawiterator = ballstodrawiterator - 1
        self.contents = ballist # Gör om self.contents till den nya Bollistan för att antalet bollar ska minska i self contents
        # Returnerar de dragna bollarna
        return drawnballs


# Skapar en experimentfunktion som tar ett hatobjekt, bollar som ska dras, dragna bollar och antalet upprepningar av experimentet
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Skapar lista att lägga i de bollar man "vill dra" och ska kolla sannolikheten för, samt två variabler en för antalet misslyckade experiment och en som itereringsvariabel för antalet exp.
    expected_balls_list = []
    failedexperiments = 0
    num_experiments_iterator = num_experiments

    # Lägger till bollarna som matats in i listan "expected_balls_list"
    for key, values in expected_balls.items():
        print(key,values)
        expected_balls_list.extend([key for iterator in range(values)])

    # Loop som genomför experimenten så länge antalet kvarvarande experiment är högre än 0
    while num_experiments_iterator > 0:
        # Gör en kopia på "Hatt-objektet" varje iterering då med draw-metoden minskar antalet bollar i self.content och på detta sätt säkras att man börjar varje iterering med alla bollar i hatten.
        hatlist = copy.deepcopy(hat)
        # Anropar draw-metoden och gör en "dragning" som retunerar en lista på dragna bollar.
        drawnballist = hatlist.draw(num_balls_drawn)
        # Loopar igenom listan med "expected balls" och kontrollerar, boll för boll, om dessa finns bland de dragna bollarna i "drawnball list" finns inte alla med sätts variabeln failedexperiments till +1
        for ball in expected_balls_list:
            if ball in drawnballist:
                drawnballist.remove(ball)
            else:
                failedexperiments +=1
                break
        num_experiments_iterator = num_experiments_iterator - 1

    # Räknar ut antalet lyckade experiment genom att ta antalet experiment - antalet misslyckade.
    succesfulexperiments = num_experiments - failedexperiments
    # Räknar ut sannolikheten genom att ta antalet lyckade experiment / antalet experiment
    return succesfulexperiments / num_experiments


