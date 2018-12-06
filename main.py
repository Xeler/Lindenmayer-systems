
from funktioner import LindIter, turtleGraph, turtlePlot, updateStrings, plt, np, time



lindString = False

while True:
    ##Mulige udvidelser:
    ##Lad brugeren definere sit eget system
    ##Beregn egenskaber af systemerne, så som f.eks. kurvelængde afhængigt af iteration-antal

    print('''
        Hello and welcome to our program. You now have the following options:
        1. Choose a type of Lindenmayer system and a number of iterations
        2. Vizualise the Lindenmayer string
        3. Information about the Lindenmayer string
        4. Print the Lindenmayer string
        5. Quit and exit the program
    ''')
    svar = input("What do you wish to do? ")

    if svar == "1":
        system = input('''These are your options:
            1. Koch curve
            2. Sierpinski triangle \n
Please choose a system: ''')
        if system!="1" and system != "2":
            print("Please choose either option 1 or option 2")
            continue

        N = input("How many iterations do you want? ")

        ##11 er max iterationer for koch
        if int(N) > 11 and system=="1":
            confirm = input('''The selected amount of iterations will take a long time to generate. \n
            Do you want to continue anyway? (Y)''')
            if confirm.upper()!="Y":
                continue
            print("Wonderful! Be patient - the visualization will be worth your wait" )
                
        if int(N) > 14 and system=="2":
            confirm = input('''The selected amount of iterations will take a long time to generate. \n
            Do you want to continue anyway? (Y)''')
            if confirm.upper()!="Y":
                continue
        #


        if system=="1":
            lindString = LindIter("Koch", int(N))
        elif system=="2":
            lindString = LindIter("Sierpinski", int(N))
        else:
            continue


    if svar == "2":
        if not lindString:
            print("You have not generated a system yet")
            continue
        
        
        if system=="1":
             plt.title("Kock curven. Iterations: "+ N)
             plt.xlim([0,1])
             plt.ylim([-0.25,0.55])
             turtlePlot(turtleGraph(lindString))
            
        if system=="2":
             plt.title("Sierpinski triangle. Iterations: "+ N)
             plt.xlim([0,1])
             plt.ylim([-0.1,1])
             turtlePlot(turtleGraph(lindString))


    if svar == "3":
        if not lindString:
            print("You have not generated a system yet")
            continue
        t5s = time.time()
        t5s = time.time() - t5s
        t5g = time.time()
        graph = turtleGraph(lindString)
        t5g = time.time() - t5g
        t5p = time.time()
        print("Timetable for " + N + " iteration(s) of the choosen system"'''  
            String generation: {}
            Graph generation: {}
            Plot generation: {}
        '''.format(t5s, t5g, time.time() - t5p))

        print("The length of the string is: ",np.sum(graph[::2]))
        
    if svar=="4" :
        if not lindString:
            print("You have not generated a system yet\n")
            continue
        if system=="1":
            print(LindIter("Koch", int(N)))
    
        elif system=="2":
            print(LindIter("Sierpinski", int(N)))

        
    
    if svar=="5" :
        print("You have chosen to quit and the program will now close itself. Thank you and have a nice day.")
        break
    

        

    if svar == "9":
        #Hemmelig menu til at omdefinere lindIter strenge:
        print('''Velkommen til den hemmelige menu for at bryde reglerne. Vælg et system:''')
        system = input('''1. Koch
        2. Sierpinski
        3. Reset til originalværdier for begge strenge ''')

        if system=="1":
            newS = input("Indskriv din nye regel for koch: (Org er \"SLSRSLS\") ")
            updateStrings(newS)
        elif system=="2":
            newSA = input("Indskriv din nye regel for A: (Org er \"BRARB\") ")
            newSB = input("Indskriv din nye regel for B: (Org er \"ALBLA\") ")
            updateStrings(False, newSA, newSB)
        elif system=="3":
            updateStrings("SLSRSLS", "BRARB", "ALBLA")


