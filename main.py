
import numpy as np
from funktioner import *


import math
import time


lindString = False

while True:
    ##Mulige udvidelser:
    ##Lad brugeren definere sit eget system
    ##Beregn egenskaber af systemerne, så som f.eks. kurvelængde afhængigt af iterationantal

    print('''Hej med dig, her er dine muligheder:
        1. Vælg en type af Lindenmayer system og et antal iterationer.
        2. Generer diagrammer.
        3. Tiden det tager at generere system-string for Koch systemer
        4. Afslut. 
    ''')
    svar = input("Hvad ønsker du at gøre? ")

    if svar == "1":
        system = input('''Vælg venligst et system:
            1. Koch curve
            2. Sierpinski triangle
        ''')
        
        N = input("Angiv det ønskede antal iterationer ")
        if system=="1":
            lindString = LindIter("Koch", int(N))
        elif system=="2":
            lindString = LindIter("Sierpinski", int(N))
        else:
            print("Vælg venligst et tal mellem 1 & 2")
            continue
        t5s = time.time()
        t5s = time.time() - t5s
        t5g = time.time()
        graph = turtleGraph(lindString)
        t5g = time.time() - t5g
        t5p = time.time()
        turtlePlot(graph)
        print('''Tiden for generation af valgte sting: 
            String generation: {}
            Graph generation: {}
            Plot generation: {}
        '''.format(t5s, t5g, time.time() - t5p))


    if svar == "2":
        if not lindString:
            print("Du har endnu ikke genereret et system")
            continue
        
        turtlePlot(turtleGraph(lindString))


    if svar == "3":

        t5s = time.time()
        lindString = LindIter("Koch", 7)
        t5s = time.time() - t5s
        t5g = time.time()
        graph = turtleGraph(lindString)
        t5g = time.time() - t5g
        t5p = time.time()
        turtlePlot(graph)
        print('''7 it 
            String generation: {}
            Graph generation: {}
            Plot generation: {}
        '''.format(t5s, t5g, time.time() - t5p))
        
    if svar=="4" :
        print("Du har valgt at afslutte. Tak for denne gang.")
        break

    if svar != "":
        print("skriv noget fister")


    if svar == "Q":
        break

