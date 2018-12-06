
import numpy as np
from funktioner import *


import math
import time


lindString = False

while True:
    ##Mulige udvidelser:
    ##Lad brugeren definere sit eget system
    ##Beregn egenskaber af systemerne, så som f.eks. kurvelængde afhængigt af iteration-antal

    print('''Hej med dig, her er dine muligheder:
        1. Vælg en type af Lindenmayer system og et antal iterationer.
        2. Generer diagrammer.
        3. Info om tråden
        4. Se Lindenmayersteng
        5. Afslut. 
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
        
        print('''Tiden for generation af valgte sting: 
            String generation: {}
            Graph generation: {}
            Plot generation: {}
        '''.format(t5s, t5g, time.time() - t5p))


    if svar == "2":
        if not lindString:
            print("Du har endnu ikke genereret et system")
            continue
        
        
        if system=="1":
             plt.title("Kock-kurven. Iterationer: "+ N)
             plt.xlim([0,1])
             plt.ylim([-0.25,0.55])
             turtlePlot(turtleGraph(lindString))
            
        if system=="2":
             plt.title("Sierpinski-kurven. Iterationer: "+ N)
             plt.xlim([0,1])
             plt.ylim([-0.1,1])
             turtlePlot(turtleGraph(lindString))


    if svar == "3":
        if not lindString:
            print("Du har endnu ikke genereret et system")
            continue
        t5s = time.time()
        t5s = time.time() - t5s
        t5g = time.time()
        graph = turtleGraph(lindString)
        t5g = time.time() - t5g
        t5p = time.time()
        print(N + " Iterationer af valgt system"''' 
            String generation: {}
            Graph generation: {}
            Plot generation: {}
        '''.format(t5s, t5g, time.time() - t5p))

        print("Længden af tråden er: ",np.sum(graph[::2]))
        
    if svar=="4" :
        if not lindString:
            print("Du har endnu ikke genereret et system")
            continue
        if system=="1":
            print(LindIter("Koch", int(N)))
    
        elif system=="2":
            print(LindIter("Sierpinski", int(N)))

        
    
    if svar=="5" :
        print("Du har valgt at afslutte. Tak for denne gang.")
        break
    '''
    if svar != "":
        print("skriv noget fister") 
    '''

    if svar == "Q":
        break

