import math
import numpy as np

import matplotlib.pyplot as plt


def LindIter(System, N):
    # Insert your code here
    if System=="Koch":
        LindenmayerString = "S"
        for i in range(N):
            LindenmayerString = LindenmayerString.replace("S", "SLSRSLS")


    elif System=="Sierpinski":
        LindenmayerString = "A"
        for i in range(N):
            
            newString = ""
            for b in LindenmayerString:
                if b == "A":
                    newString += "BRARB"
                elif b == "B":
                    newString += "ALBLA"
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

    turtleCommands = np.array([])

    
    if LindenmayerString.count("S"):
        #Koch
        c =  LindenmayerString.count("SLSRSLS")
        skalering = 1/3 if c>0 else 1

        while c > 1:
            c = c/4
            skalering *= 1/3

        for b in LindenmayerString:
            if b=="L":
                turtleCommands = np.append(turtleCommands, math.pi/3)
            elif b=="R":
                turtleCommands = np.append(turtleCommands, -2*math.pi/3)
            else:
                turtleCommands = np.append(turtleCommands, skalering)

    else:
        #Sierpiniski:
        c = len(LindenmayerString)
        skalering = 1
        while c > 3:
            c = c/3
            skalering *= 1/2

        for b in LindenmayerString:
            if b=="L":
                turtleCommands = np.append(turtleCommands, math.pi/3)
            elif b=="R":
                turtleCommands = np.append(turtleCommands, -math.pi/3)
            else:
                turtleCommands = np.append(turtleCommands, skalering)        

    
    #L fortolkes som en venstre-drejning med vinklen 1/3*Pi
    #R fortolkes som en højre-drening med vinklen -2/3*Pi(Koch) eller -1/3*Pi(Sierpinski)
    #længden af linjesegmentet skaleres med en faktor 1/3(Koch) og 1/2(Sierpinski) efter hver iteration

    #outputtet burde se sådan her ud: [l1,v1,l2,v2,...,ln,vn]


    return turtleCommands

def turtlePlot(turtleCommands):

    vectors = np.array([0, 0])
    vectors.shape = (1,2)
    rotation = np.array([1, 0])
    rotation.shape = (1,2)
    index = 0
    for index in range(len(turtleCommands)):
        if index%2==0:
            #linjesigment
            newVector = np.add(vectors[len(vectors)-1], np.multiply(turtleCommands[index], rotation[len(rotation)-1]))

            vectors = np.vstack((vectors, newVector))
        else:
            matrix = np.array([math.cos(turtleCommands[index]), -math.sin(turtleCommands[index]), math.sin(turtleCommands[index]), math.cos(turtleCommands[index])])
            matrix.shape = (2,2)
            rotation = np.vstack((rotation, np.dot(rotation[len(rotation)-1], matrix)))
        index+=1

    plt.show()
    for index, vector in enumerate(vectors):
        if(index==0):
            continue
            
        plt.plot([vectors[index-1][0], vector[0]], [vectors[index-1][1], vector[1]], 'ro-')

    plt.show()



turtlePlot(turtleGraph(LindIter("Sierpinski", 8)))