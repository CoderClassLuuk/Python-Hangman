#Gemaakt door Luuk Noverraz

##
# Tips voor je code schrijf ik in dit soort commentaarblokken
# Leuk spel, doet het goed! Wel wat zaken zijn nodig om de code beter te maken.
##

import random
import time
import math

goede_letters = []
fout = 0
geraden = 0

#variabele waarin staat hoevaak je het fout geraden hebt
#5 ifs voor de galg

ggl = ""
fgl = ""
#"goed/fout geraden lijst" voor alle letters goed/fout geraden door de speler


lijst = ["strijder", "humanisme", "communisme", "zimbabwe", "sinaasappel", "ananas", "dimensie", "nebula", "beeldscherm", "bilderdijkstraat", "luidspreker", "andromeda"]
fout_zinnen = ["Maar dit is ook een kans om een aflaat te kopen.", "But dont forget to enter my free gift card giveaway.", "Maar vergeet niet te subscribbelen op Dabie Bab.", "Hopelijk lukt het volgende keer.", "Hakan is teleurgesteld."]
goed_zinnen = ["Koop trouwens ook een aflaat.", "Jurjen is blij :)!", "Pret en plezier voor de complete, volledige, sociaaldemocratische familie!", "Toppie!", "Ga zo door!", "Trouwens... babdup?", ":)"]
#de lijst met woorden waaruit gekozen kan worden

geheimwoord = random.choice(lijst)
gw_lijst = list(geheimwoord)

#het geheime woord dat uit de lijst gekozen wordt

#Als geheimwoord zelf bepaald mag worden :
#geheimwoord = input("Typ hier het geheime woord in: ")

lengte = len(geheimwoord)
#Lengte is de lengte van het geheime woord

for i in range(lengte):
  goede_letters.append("_")

print("Welkom bij Galgje! Als je wilt stoppen, typ dan QQ.")

while True:
    if fout == 1:
        print("                  ")
        print("                  ")
        print("                  ")
        print("                  ")
        print("                  ")
        print("                  ")
        print("     ___          ")
        print("                  ")
    if fout == 2:
        print("                  ")
        print("    |             ")
        print("    |             ")
        print("    |             ")
        print("    |             ")
        print("    |             ")
        print("    |___          ")
        print("                  ")
    if fout == 3:
        print("     _________    ")
        print("    |/            ")
        print("    |             ")
        print("    |             ")
        print("    |             ")
        print("    |             ")
        print("    |___          ")
        print("                  ")
    if fout == 4:
        print("     _________    ")
        print("    |/        |   ")
        print("    |         0   ")
        print("    |         |   ")
        print("    |             ")
        print("    |             ")
        print("    |___          ")
        print("                  ")
    if fout == 5:
        print("     _________    ")
        print("    |/        |   ")
        print("    |         0   ")
        print("    |        /|\  ")
        print("    |        / \  ")
        print("    |             ")
        print("    |___          ")
        print("                  ")
        print("")
        print("Je bent gestorven.")
        time.sleep(2)
        break
  
    for i in range(lengte):
        print (goede_letters[i], end=" ")
    print("")
    kies = input("Kies een letter of kies ? om het geheime woord te raden. ")
    
    if kies == "?":
        time.sleep(1.5)
        raad = input("Ok, typ hier in wat je denkt dat het woord is : ")
        if raad == geheimwoord:
            time.sleep(2)
            print("")
            print("Gefeliciteerd, je hebt gewonnen! Het woord was inderdaad " + raad + "!")
            time.sleep(1)
            print("")
            print("Het programma sluit af in 10 seconden.")
            time.sleep(10)
            while True:
                break
        elif raad != geheimwoord:
            time.sleep(2)
            print("Helaas! Je heb het woord fout geraden, en je krijgt nu een strafpunt.")
            time.sleep(1)
            print("")
            fout += 1
    elif kies.upper() == "QQ":
        time.sleep(0.5)
        print("")
        print("Oh.")
        time.sleep(1)
        print("")
        print("Ok.")
        time.sleep(1)
        print("")
        print("Vaarwel. :(")
        time.sleep(1.5)
        break

    elif not kies.isalpha():
        time.sleep(1)
        print("")
        print("Kies alstjeblieft een letter uit het alfabet. (Je krijgt nu een strafpunt)")
        time.sleep(1.5)
        print("")
        fout += 1        

    else:
        if kies in ggl:
            print("")
            print("Deze letter heb je al eerder gekozen, probeer alsjeblieft een andere letter.")
            print("")
        else:
          lettergoed = False
          for i in range(lengte):
            if kies == geheimwoord[i]:
              lettergoed = True
              goede_letters[i] = kies
              geraden = 1
          if geraden == 1:
              print("")              
              print("Goed geraden! " + random.choice(goed_zinnen))
              ggl = ggl + kies
              print("") 
              print("Deze heb je al goed geraden: ", ggl, " / Deze heb je fout geraden : ", fgl)
              print("")
              geraden = 0

          if lettergoed == False:
              fout += 1
              print("")
              print("Jammer. " + random.choice(fout_zinnen))
              print("")
              time.sleep(0.5)
              fgl = fgl + kies
              print("Deze heb je al goed geraden: ", ggl, " / Deze heb je fout geraden : ", fgl)

          if goede_letters == gw_lijst:
              time.sleep(1)
              print("")
              print("Gefeliciteerd, je hebt gewonnen! Het programma sluit af in 10 seconden.")
              time.sleep(10)
              while True:
                  break

           
           
