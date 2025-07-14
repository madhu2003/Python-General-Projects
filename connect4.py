import random
turn=0
def check_move (board,turn,col,pop):
    row= int(len(board)/7)
    temp=board.copy()
    if turn==1:
        if temp[col]==1 and pop==True:
            return True
        elif pop==False:
            for i in range(0,row):
                if temp[col+7*i]==0 and pop==False:
                    return True
        else:
            return False
    if turn==2:
        if temp[col]==2 and pop==True:
            return True
        elif pop==False:
            for i in range(0,row):
                if temp[col+7*i]==0 and pop==False:
                    return True
        else:
            return False
    
def apply_move(board,turn,col,pop):
    temp=board.copy()
    row= int(len(board)/7)
    if pop== True:
        temp[col]=0
        for i in range(1,row):  
                temp[col+7*(i-1)]=temp[col+7*i]
        temp[col+7*(row-1)]=0
        
    elif pop==False:
            for i in range(0,row):
                input_col=col+7*i
                if temp[col+7*i]==0:
                    temp[input_col]=turn
                    break
                else:
                    continue
    return temp
        
    
def check_victory(board, who_played):
    temp=board.copy()
    row= int(len(board)/7)
    victory_list=[]
    if who_played==1:
        #horizontal win for player 1
        for c in range(0,4):
            for i in range (0,row): 
                if temp[c+7*i]==who_played and temp[c+7*i+1]==who_played and temp[c+7*i+2]==who_played and temp[c+7*i+3]==who_played:
                    victory_list.append(1)
        #vertical win for player 1
        for c in range(0,7):
            for i in range(0,row-3): 
                if temp[c+7*i]==who_played and temp[c+7*(i+1)]==who_played and temp[c+7*(i+2)]==who_played and temp [c+7*(i+3)]==who_played:
                    victory_list.append(1)
        #diagonal win for postive slope for player 1
        for c in range(0,4): #for c in [0,1,2,3,7,8,9,10,14,15,16,17]
            for i in range(0,row-3): 
                if temp[c+7*i]==who_played and temp[c+7*i+8]==who_played and temp[c+7*i+16]==who_played and temp[c+7*i+24]==who_played:
                # if temp[c]==who_played and temp[c+8]==who_played and temp[c+16]==who_played and temp[c+24]==who_played:
                    victory_list.append(1)
        #diagonal win for negative slope for player 1
        for c in range(0,4): #[21,22,23,24,28,29,30,31,35,36,37,38]
            for i in range(0,row-3):
                if temp[21+c+7*i]==who_played and temp[21+c+7*i-6]==who_played and temp[21+c+7*i-12]==who_played and temp[21+c+7*i-18]==who_played:
                    victory_list.append(1)
        #horizontal win for player 2/computer
        for c in range(0,4):
            for i in range (0,row): 
                if temp[c+7*i]==2 and temp[c+7*i+1]==2 and temp[c+7*i+2]==2 and temp[c+7*i+3]==2:
                    victory_list.append(2)
        #vertical win for player 2/computer
        for c in range(0,7):
            for i in range(0,row-3): 
                if temp[c+7*i]==2 and temp[c+7*(i+1)]==2 and temp[c+7*(i+2)]==2 and temp [c+7*(i+3)]==2:
                    victory_list.append(2)
        #diagonal win for postive slope for 2/computer
        for c in range(0,4): #for c in [0,1,2,3,7,8,9,10,14,15,16,17]
            for i in range(0,row-3): 
                if temp[c+7*i]==2 and temp[c+7*i+8]==2 and temp[c+7*i+16]==2 and temp[c+7*i+24]==2:
        # for c in [0,1,2,3,7,8,9,10,14,15,16,17]:
        #     if temp[c]==2 and temp[c+8]==2 and temp[c+16]==2 and temp[c+24]==2:
                    victory_list.append(2)
         
        #diagonal win for negative slope for 2/computer
        for c in range(0,4): #[21,22,23,24,28,29,30,31,35,36,37,38]
            for i in range(0,row-3):
                if temp[21+c+7*i]==2 and temp[21+c+7*i-6]==2 and temp[21+c+7*i-12]==2 and temp[21+c+7*i-18]==2:
        # for c in [21,22,23,24,28,29,30,31,35,36,37,38]:
        #     if temp[c]==2 and temp[c-6]==2 and temp[c-12]==2 and temp[c-18]==2:
                    victory_list.append(2)  
        if 1 in victory_list and not 2 in victory_list:
            return 1
        elif 1 in victory_list and 2 in victory_list:
            return 2
        elif not 1 in victory_list and 2 in victory_list:
            return 2
        else:
            return 0
    
    else:
        #horizontal win for player 2/computer
        for c in range(0,4):
            for i in range (0,row):
                if temp[c+7*i]==who_played and temp[c+7*i+1]==who_played and temp[c+7*i+2]==who_played and temp[c+7*i+3]==who_played:
                    victory_list.append(2)
        #vertical win for player 2/computer
        for c in range(0,7):
            for i in range(0,row-3):
                if temp[c+7*i]==who_played and temp[c+7*(i+1)]==who_played and temp[c+7*(i+2)]==who_played and temp [c+7*(i+3)]==who_played:
                    victory_list.append(2)
        #diagonal win for postive slope for 2/computer
        for c in range(0,4): #for c in [0,1,2,3,7,8,9,10,14,15,16,17]
           for i in range(0,row-3): #row-3
               if temp[c+7*i]==who_played and temp[c+7*i+8]==who_played and temp[c+7*i+16]==who_played and temp[c+7*i+24]==who_played: 
        # for c in [0,1,2,3,7,8,9,10,14,15,16,17]:
        #     if temp[c]==who_played and temp[c+8]==who_played and temp[c+16]==who_played and temp[c+24]==who_played:
                    victory_list.append(2)
         
        #diagonal win for negative slope for 2/computer
        for c in range(0,4): #[21,22,23,24,28,29,30,31,35,36,37,38]
            for i in range(0,row-3):#row-3
                if temp[21+c+7*i]==who_played and temp[21+c+7*i-6]==who_played and temp[21+c+7*i-12]==who_played and temp[21+c+7*i-18]==who_played:
        # for c in [21,22,23,24,28,29,30,31,35,36,37,38]:
        #     if temp[c]==who_played and temp[c-6]==who_played and temp[c-12]==who_played and temp[c-18]==who_played:
                    victory_list.append(2)
        #horizontal win for player 1
        for c in range(0,4):
            for i in range (0,row):
                if temp[c+7*i]==1 and temp[c+7*i+1]==1 and temp[c+7*i+2]==1 and temp[c+7*i+3]==1:
                    victory_list.append(1)
        #vertical win for player 1
        for c in range(0,7):
            for i in range(0,row-3):
                if temp[c+7*i]==1 and temp[c+7*(i+1)]==1 and temp[c+7*(i+2)]==1 and temp [c+7*(i+3)]==1:
                    victory_list.append(1)
        #diagonal win for postive slope for player 1
        for c in range(0,4): #for c in [0,1,2,3,7,8,9,10,14,15,16,17]
            for i in range(0,row-3): #row-3
                if temp[c+7*i]==1 and temp[c+7*i+8]==1 and temp[c+7*i+16]==1 and temp[c+7*i+24]==1:
        # for c in [0,1,2,3,7,8,9,10,14,15,16,17]:
        #     if temp[c]==1 and temp[c+8]==1 and temp[c+16]==1 and temp[c+24]==1:
                    victory_list.append(1)
        #diagonal win for negative slope for player 1
        for c in range(0,4): #[21,22,23,24,28,29,30,31,35,36,37,38]
            for i in range(0,row-3):#row-3
                if temp[21+c+7*i]==1 and temp[21+c+7*i-6]==1 and temp[21+c+7*i-12]==1 and temp[21+c+7*i-18]==1:

        # for c in [21,22,23,24,28,29,30,31,35,36,37,38]:
        #     if temp[c]==1 and temp[c-6]==1 and temp[c-12]==1 and temp[c-18]==1:
                    victory_list.append(1)
        if 1 in victory_list and not 2 in victory_list:
            return 1
        elif 1 in victory_list and 2 in victory_list:
            return 1
        elif 2 in victory_list and not 1 in victory_list:
            return 2
        else:
            return 0
        
       

def computer_move(board,turn,level):   
    if level==1: 
        col=random.randint(0,6) 
        pop=bool(random.getrandbits(1))
        if check_move(board,turn,col,pop)==True: 
            return (col, pop)
        while check_move(board,turn,col,pop)==False:
            col=random.randint(0,6) 
            pop=bool(random.getrandbits(1))
            if check_move(board,turn,col,pop)==True: 
                return (col, pop)
    if level==2: 
        #check for victory
        if turn==1:
            for pop in [True,False]:
                for col in range(0,7):  
                    if check_move(board,turn,col,pop)==True:
                        temp=apply_move(board,turn,col,pop)
                        if check_victory(temp,turn)==turn:
                            return (col,pop)
     
            for col in range(0,7):  
                if check_move(board,turn,col,False)==True: #checking if player wins next round and prevent him from winning by inserting a disk column
                    temp=apply_move(board,2,col,False)
                    if check_victory(temp,2)==2:
                        return (col,pop)
     
            while True: #random move
                col=random.randint(0,7) 
                pop=bool(random.getrandbits(1))
                if check_move(board,turn,col,pop)==True: 
                    (Aicol,Aipop) = (col,pop)
                    if Aipop == True:
                        temp=apply_move(board,turn,Aicol,True)
                        if check_victory(temp,2)==2:
                            continue
                        else:
                            break
                    else:
                        break
     
            return (Aicol,Aipop)
        else:
           for pop in [True,False]:
               for col in range(0,7):  
                   if check_move(board,turn,col,pop)==True:
                       temp=apply_move(board,turn,col,pop)
                       if check_victory(temp,turn)==turn:
                           return (col,pop)
    
           for col in range(0,7):  
               if check_move(board,turn,col,False)==True:
                   temp=apply_move(board,1,col,False)
                   if check_victory(temp,1)==1:
                       return (col,pop)
    
           while True:
               col=random.randint(0,6) 
               pop=bool(random.getrandbits(1))
               if check_move(board,turn,col,pop)==True: 
                   (Aicol,Aipop) = (col,pop)
                   if Aipop == True:
                       temp=apply_move(board,turn,Aicol,True)
                       if check_victory(temp,1)==1:
                           continue
                       else:
                           break
                   else:
                       break
    
           return (Aicol,Aipop) 
    # if level==2: #still wrong
    #     moves_computer=[]
    #     moves_player=[]
    #     valid_moves_player=[]
    #     checkvictorynotturn=[]
    #     allpossiblecombi=[]
    #     for pop in [True,False]:
    #         for col in range(0,7):  
    #             if check_move(board,turn,col,pop)==True:
    #                 temp=apply_move(board,turn,col,pop)
    #                 if check_victory(temp,turn)==turn:
    #                     return (col,pop)

    #     for col in range(0,7): 
    #         for pop in [True,False]:
    #             moves_computer.append((col,pop))
    #     for col1 in range(0,7): 
    #         for pop1 in [True,False]:
    #             moves_player.append((col1,pop1))

    #     # need to ensure that computer move works for turn 1 and 2
    #     if turn==1:
    #         for col,pop in moves_computer:
    #                 for col1,pop1 in moves_player:
    #                     if check_move(board,turn,col,pop)==True: #computer turn
    #                         board2=apply_move(board,turn,col,pop)
    #                         if check_move(board2,2,col1,pop1)==True: #player turn
    #                             board1=apply_move(board2,2,col1,pop1)
    #                             valid_moves_player.append(1) #indication so that later the len of the list can be calculated to be the no. of valid player moves
    #                             if check_victory(board1,2)==2:#if player wins
    #                                 moves_computer.remove((col,pop))
    #                             else: 
    #                                 checkvictorynotturn.append(2)
    #                                 while len(checkvictorynotturn)==len(valid_moves_player):
    #                                     allpossiblecombi.append((col,pop))
    #                                     col,pop=random.choice(allpossiblecombi)
    #                                     return (col,pop)    
    #         # ensure indention same as level 1
    #         col=random.randint(0,7) 
    #         pop=bool(random.getrandbits(1))
    #         if check_move(board,turn,col,pop)==True:
    #               return (col, pop)
    #         while check_move(board,turn,col,pop)==False: #
    #             col=random.randint(0,7) 
    #             pop=bool(random.getrandbits(1))
    #             if check_move(board,turn,col,pop)==True: 
    #                 return (col,pop)
    #     else:
    #         for col,pop in moves_computer:
    #                 for col1,pop1 in moves_player:
    #                     if check_move(board,turn,col,pop)==True: #computer turn
    #                         board2=apply_move(board,turn,col,pop)
    #                         if check_move(board2,1,col1,pop1)==True: #player turn
    #                             board1=apply_move(board2,2,col1,pop1)
    #                             valid_moves_player.append(1) #indication so that later the len of the list can be calculated to be the no. of valid player moves
    #                             if check_victory(board1,1)==1:#if player wins
    #                                 moves_computer.remove((col,pop))
    #                             else: 
    #                                 checkvictorynotturn.append(2)
    #                                 while len(checkvictorynotturn)==len(valid_moves_player):
    #                                     allpossiblecombi.append((col,pop))
    #                                     col,pop=random.choice(allpossiblecombi)
    #                                     return (col,pop)    
    #         # ensure indention same as level 1
    #         col=random.randint(0,7) 
    #         pop=bool(random.getrandbits(1))
    #         if check_move(board,turn,col,pop)==True:
    #               return (col, pop)
    #         while check_move(board,turn,col,pop)==False: #
    #             col=random.randint(0,7) 
    #             pop=bool(random.getrandbits(1))
    #             if check_move(board,turn,col,pop)==True: 
    #                 return (col,pop)
        
    
def display_board(board): 
    row= int(len(board)/7)
    for i in range(row-1,-1,-1): 
        print(board[7*i],board[7*i+1],board[7*i+2],board[7*i+3],board[7*i+4],board[7*i+5],board[7*i+6])
    pass

def menu():
    while True:
    # display options in menu
        print("Welcome to Connect 4!")
        print("1. Controls")
        print("2. How to play?")
        print("3. How to win?")
        print("4. Multiplayer")
        print("5. Player vs Computer")
        print("6. Exit")
        option = input("Enter your option:")
        play=False
        computer=False
        level=0
        
        if option== "1":
            print("Row Numbers (>=4)."
                "Column (0 to 6)."
                  "Pop (True or False).")
            continue
        elif option== "2":
            print("Players first select the number of rows for their playing board."
                  "Each player then take turns to enter column (0 to 6) to place the disk in for that round."
                  "Afterwards, if player wants to pop disk, input True. Otherwise, input False to add disk."
                  "Column 0 will indicate the bottom column, and Column 6 will indicate the top column.")
            continue
        elif option== "3":
            print("A player wins by getting four of their disks in a vertical, horizontal or diagonal row. If a player gets four of the opponent's disks in a vertical, horizontal or diagonal row during his turn, the player loses.")
            continue
        elif option== "4":
            print("The game will start now!")
            play = True
        elif option== "5":
            print("The game will start now!")
            computer = True
        elif option== "6":
            print("You will exit the game now.")
            break
        else:
            #warn player if they entered any number that is not between 1 to 6
            print("Invalid input. Please re-enter your option that is between 1 to 6.")
            continue
     
          
        if play == True: 
            board= []
            while True:
                try:
                    row= int(input("Please input the number of rows for your board."))
                    break
                except ValueError:
                    print("Error! Please ensure that your input is an integer.")
                    continue
            while int(row)<4:
                print("Please input an integer value for the number of rows that is >=4.")
                try:
                    row= int(input("Please input the number of rows for your board."))
                    break
                except ValueError:
                    print("Error! Please ensure that your input is an integer.")
                    continue
            for i in range(0,7*row):
                board.append(0)
            display_board(board)
            x=1
            while True: 
                if x%2==1:
                    turn=1
                    who_played=turn
                    pop= str(input("Please input True to pop disc. Otherwise, input False to add disc."))
                    x+=1
                    while pop!= "False" and pop!="True":
                        print("Please enter True or False!")
                        pop= str(input("Please input True to pop disc. Otherwise, input False to add disc."))
                        continue
                    if pop=="True":
                        pop=True
                    elif pop=="False":
                        pop=False
                    while True:
                        try:
                            col= int(input("Please input which column(0-6) for your move."))
                            break
                        except ValueError:
                            print("Error! Please ensure that your input is an integer.")
                            continue
                            
                    while int(col)>6 or int(col)<0:
                            print("Column is in range 0-6!")
                            col= int(input("Please input which column(0-6) for your move."))
                            continue
                    while check_move(board,turn,col,pop) == False:
                            print("Your move is not possible. Note that you can only pop the disc from the bottom column or add disc to a column that is not filled.")
                            pop= str(input("Please input True to pop disc. Otherwise, input False to add disc."))
                            if pop=="True":
                                pop=True
                            elif pop=="False":
                                pop=False
                            while True:
                                try:
                                   col= int(input("Please input which column(0-6) for your move."))
                                   break
                                except ValueError:
                                   print("Error! Please ensure that your input is an integer.")
                                   continue
                    else:
                        board=apply_move(board,turn,col,pop)
                        display_board(board)
                        if pop==True:
                            move= "popped"
                        else:
                            move="added"
                        print("Player 1 has",move,"disk at Column",col,".")
                        victory = check_victory(board, who_played)
                        if victory==1:
                            print ("Congratulations! Player 1 won!")
                            break
                        elif victory==2:
                            print ("Congratulations! Player 2 won!")
                            break
                        elif victory==0:
                            print ("The game continues with Player 2 next!")
                            
                else:
                    turn=2
                    who_played=turn
                    x+=1
                    pop= str(input("Please input True to pop disc. Otherwise, input False to add disc."))
                    while pop!= "False" and pop!="True": 
                            print("Please enter True or False!")
                            pop= str(input("Please input True to pop disc. Otherwise, input False to add disc."))
                            continue
                    if pop=="True":
                        pop=True
                    elif pop=="False":
                        pop=False
                    while True:
                        try:
                           col= int(input("Please input which column(0-6) for your move."))
                           break
                        except ValueError:
                           print("Error! Please ensure that your input is an integer.")
                           continue
                    while int(col)>6 or int(col)<0:
                            print("Column is in range 0-6!")
                            col= int(input("Please input which column(0-6) for your move."))
                            continue
                    while check_move(board,turn,col,pop) == False:
                            print("Your move is not possible. Note that you can only pop the disc from the bottom column or add disc to a column that is not filled.")
                            pop= str(input("Please input True to pop disc. Otherwise, input False to add disc."))
                            if pop=="True":
                                pop=True
                            elif pop=="False":
                                pop=False
                            while True:
                                try:
                                   col= int(input("Please input which column(0-6) for your move."))
                                   break
                                except ValueError:
                                   print("Error! Please ensure that your input is an integer.")
                                   continue
                    
                    else:
                        board=apply_move(board,turn,col,pop)
                        display_board(board)
                        if pop==True:
                            move= "popped"
                        else:
                            move="added"
                        print("Player 2 has",move,"disk at Column",col)
                        victory = check_victory(board, who_played)
                        if victory==1:
                            print ("Congratulations! Player 1 won!")
                            break
                        elif victory==2:
                            print ("Congratulations! Player 2 won!")
                            break
                        elif victory==0:
                            print ("The game continues with Player 1 next!") 
            else:               
                print ("End of game! Thank you for playing Connect 4!")
                return play== False      
        
        elif computer == True: 
            board= []
            while True:
                try:
                    row= int(input("Please input the number of rows for your board."))
                    break
                except ValueError:
                    print("Error! Please ensure that your input is an integer.")
                    continue
            while int(row)<4:
                print("Please input an integer value for the number of rows that is >=4.")
                while True:
                    try:
                        row= int(input("Please input the number of rows for your board."))
                        break
                    except ValueError:
                        print("Error! Please ensure that your input is an integer.")
                        continue
            for i in range(0,7*row):
                board.append(0)
            display_board(board)
            while True:
                try:
                    level = int(input("Difficulty Level: 1 or 2?"))
                    break
                except ValueError:
                    print("Error! Please ensure that your input is 1 or 2.")
                    continue
            while int(level) < 0 or int(level) > 2 :                
                print ("Input Level 1 or 2:")
                level = int(input("Difficulty Level: 1 or 2?"))
                continue
            x=1
            while True:
                if x%2==1:
                   turn=1
                   x+=1
                   who_played= turn
                   pop= str(input("Please input True to pop disc. Otherwise, input False to add disc."))
                   while pop!= "False" and pop!="True":
                           print("Please enter True or False!")
                           pop= str(input("Please input True to pop disc. Otherwise, input False to add disc."))     
                   if pop=="True":
                       pop=True
                   elif pop=="False":
                       pop=False
                   
                   while True:
                       try:
                           col= int(input("Please input which column(0-6) for your move."))
                           break
                       except ValueError:
                           print("Error! Please ensure that your input is an integer.")
                           continue
                   while int(col)>6 or int(col)<0: 
                       print("Column is in range 0-6!")
                       col= int(input("Please input which column(0-6) for your move."))
                       continue
                   while check_move(board,turn,col,pop) == False:
                        print("Your move is not possible. Note that you can only pop the disc from the bottom column or add disc to a column that is not filled.")
                        pop= str(input("Please input True to pop disc. Otherwise, input False to add disc."))
                        while pop!= "False" and pop!="True":
                                print("Please enter True or False!")
                                pop= str(input("Please input True to pop disc. Otherwise, input False to add disc."))     
                        if pop=="True":
                            pop=True
                        elif pop=="False":
                            pop=False
                        while True:
                            try:
                                col= int(input("Please input which column(0-6) for your move."))
                                break
                            except ValueError:
                                print("Error! Please ensure that your input is an integer.")
                                continue
                            while int(col)>6 or int(col)<0:
                                print("Column is in range 0-6!")
                                col= int(input("Please input which column(0-6) for your move."))
                        continue
                   else:
                        board=apply_move(board,turn,col,pop)
                        display_board(board)
                        if pop==True:
                            move= "popped"
                        else:
                            move="added"
                        print("Player 1 has",move,"disk at Column",col)
                        victory = check_victory(board, who_played)
                        if victory==1:
                            print ("Congratulations! Player 1 won!")
                            break
                        elif victory==2:
                            print ("Computer Won!")
                            break
                        elif victory==0:
                              print ("The game continues with Computer next!") 
                              
                else:
                    turn=2
                    who_played=turn
                    x+=1
                    print("Computer is making a move.")
                    col, pop= computer_move(board, turn, level) 
                    board=apply_move(board,turn,col,pop)
                    display_board(board)
                    if pop==True:
                        move= "popped"
                    else:
                        move="added"
                    print("Computer has",move,"disk at Column",col)
                    victory = check_victory(board, who_played)
                    if victory==1:
                        print ("Congratulations! Player 1 won!")
                        break
                    elif victory==2:
                        print ("Computer Won!")
                        break
                    elif victory==0:
                        print ("The game continues with Player 1 next!")
            else:                
              print ("End of game!" "\nThank you for playing Connect 4!")
              return computer == False          
    

if __name__ == "__main__":
    menu()

