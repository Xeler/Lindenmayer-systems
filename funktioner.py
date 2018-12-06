import math
import numpy as np
import matplotlib.pyplot as plt
import time

kochS = "SLSRSLS"
sierpSA = "BRARB"
sierpSB = "ALBLA"

def updateStrings(koch=False, siA=False, siB=False):
    global kochS, sierpSA, sierpSB
    kochS = koch or kochS
    sierpSA = siA or sierpSA
    sierpSB = siB or sierpSB

def LindIter(System, N):
    global kochS, sierpSA, sierpSB
    # Insert your code here
    if System=="Koch":
        LindenmayerString = "S"
        for i in range(N):
            LindenmayerString = LindenmayerString.replace("S", kochS)


    elif System=="Sierpinski":
        LindenmayerString = "A"
        for i in range(N):
            
            newString = ""
            for b in LindenmayerString:
                if b == "A":
                    newString += sierpSA
                elif b == "B":
                    newString += sierpSB
                else:
                    newString += b
            LindenmayerString = newString


#           LindenmayerString = LindenmayerString.replace("B", "ALBLA")
#           LindenmayerString = LindenmayerString.replace("A", "BRARB")

    elif System != "":
        print("Vælg venligst Koch eller Sirpinski")                                

    if N < 0:
        print("Vi går kun i positive iterationer. Vælg et tal lig med eller højere end 0")            
    return LindenmayerString




def turtleGraph(LindenmayerString):
    # Insert your code here

    turtleCommands = np.zeros(len(LindenmayerString))



    l = len(LindenmayerString)
    
    if LindenmayerString.count("S"):
        #Koch
        c =  LindenmayerString.count("SLSRSLS")
        skalering = 1/3 if c>0 else 1

        while c > 1:
            c = c/4
            skalering *= 1/3

        for i, b in enumerate(LindenmayerString):
            if i%1000==0:
                #\r = carriage return. Uden newline overskrives den forgående linje, og giver effekten af en dynamisk loading bar
                print("Progress: [{}{}]".format("=" * int(50 * i/l), " " * (50 - int(50 * i/l))), end="\r")
            if b=="L":
                turtleCommands[i] = math.pi/3
            elif b=="R":
                turtleCommands[i] = -2*math.pi/3
            else:
                turtleCommands[i] = skalering
        print("Progress: [{}]".format("=" * 50))
    else:
        #Sierpiniski:
        c = len(LindenmayerString)
        skalering = 1
        it = 0
        while c > 3:
            it+=1
            c = c/3
            skalering *= 1/2
        
        #######super flot hack :^)
        ##Sætter faktoren for vinklerne til -1 hvis iterationsantallet er 
        it = -1 if it&1 else 1

        for i, b in enumerate(LindenmayerString):
            if i%1000==0:
                #\r = carriage return. Uden newline overskrives den forgående linje, og giver effekten af en dynamisk loading bar
                print("Progress: [{}{}]".format("=" * int(50 * i/l), " " * (50 - int(50 * i/l))), end="\r")
            if b=="L":
                turtleCommands[i] = math.pi/3 * it
            elif b=="R":
                turtleCommands[i] = -math.pi/3 * it
            else:
                turtleCommands[i] = skalering
    
        print("Progress: [{}]".format("=" * 50))
    
    #L fortolkes som en venstre-drejning med vinklen 1/3*Pi
    #R fortolkes som en højre-drening med vinklen -2/3*Pi(Koch) eller -1/3*Pi(Sierpinski)
    #længden af linjesegmentet skaleres med en faktor 1/3(Koch) og 1/2(Sierpinski) efter hver iteration

    #outputtet burde se sådan her ud: [l1,v1,l2,v2,...,ln,vn]

    
    return turtleCommands

def turtlePlot(turtleCommands):

    l = len(turtleCommands)

    vectors = np.zeros((int(l/2)+2,2))
    #rotation = np.zeros((int(l/2)+1,2))
    rotation = np.array([1,0])
    index = 0
    l = len(turtleCommands)
    for index in range(l):
        
        
        if index%1000==0:
            print("Progress: [{}{}]".format("=" * int(50 * index/l), " " * (50 - int(50 * index/l))), end="\r")
        
        if index%2==0:
            #linjesigment
            newVector = np.add(vectors[int(index/2)], np.multiply(turtleCommands[index], rotation))
            ##Det første punkt medregnes ikke!
            vectors[int(index/2)+1] = newVector
        else:
            matrix = np.array([math.cos(turtleCommands[index]), -math.sin(turtleCommands[index]), math.sin(turtleCommands[index]), math.cos(turtleCommands[index])])
            matrix.shape = (2,2)
            rotation = np.dot(matrix, rotation)
        
        #?????
        #index+=1

    print("Progress: [{}]".format("=" * 50))
            
    

    
    plt.plot(vectors[:,0], vectors[:,1], 'r-')
    '''
    if np.isin(1/3, turtleCommands, assume_unique=True):
    #For Kock
        plt.title('Kock-kurven'
                  'Iteration')
    else:
    #For Sierpinski
        plt.title('Sierpinski-trekanten' 
                  'Iteration')
    '''

    plt.show()
    
