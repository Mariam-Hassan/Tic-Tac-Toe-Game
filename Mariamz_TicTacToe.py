def display_board(board):
            print(" |{}|{}|{}| \n |{}|{}|{}| \n |{}|{}|{}|".format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8]))

def player_input():
        print ("you are player 1 please insert X or O")
        global P1
        global P2
        P1=input()
        while P1 !="x"  and P1 != "X" and P1 != "o" and P1 != "O":
            from IPython.display import clear_output
            clear_output()
            print ("you are player 1 please insert X or O")
            P1=input()
        else:
            while P1 =="x"  or P1 == "X": 
                from IPython.display import clear_output
                clear_output()
                print ("You are Palyer2 \n Please insert O")
                P2=input()
                if P2 == "o" or P2 ==  "O":
                    break

            while P1 == "o" or P1 == "O":
                from IPython.display import clear_output
                clear_output()
                print ("You are Palyer2 \n Please insert X")
                P2=input()
                if P2 == "x" or P2 ==  "X":
                    break  
                    
def game_intro():
    from IPython.display import clear_output
    clear_output()
    print('Welcome to Tic Tac Toe!')
    P1=""
    P2=""
    global board
    board=[1,2,3,4,5,6,7,8,9]
    player_input()

    
def player_choice1(board):
    print ("Please choose a number from the board")    
    global choice
    z=input()
    while z != "1" and z != "2" and z != "3" and z != "4" and z != "5" and z != "6" and z != "7" and z != "8" and z != "9" :
        from IPython.display import clear_output
        clear_output()
        display_board(board)
        print ("Please choose a number from the board")
        z=input()            
    else:
        choice=int(z)       
        while  board[int(z)-1]!=P1  and board[int(z)-1]!=P2:
            board[choice-1]=P1
            break                            
        else:
            from IPython.display import clear_output
            clear_output()
            display_board(board)
            player_choice1(board)
        
                     
def player_choice2(board):
    print ("Please choose a number from the board")    
    global choice
    z=input()
    while z != "1" and z != "2" and z != "3" and z != "4" and z != "5" and z != "6" and z != "7" and z != "8" and z != "9" :
        from IPython.display import clear_output
        clear_output()
        display_board(board)
        print ("Please choose a number from the board")    
        z=input()            
    else:
        choice=int(z)       
        while  board[int(z)-1]!=P1  and board[int(z)-1]!=P2:
            board[choice-1]=P2
            break                            
        else:
            from IPython.display import clear_output
            clear_output()
            display_board(board)
            player_choice2(board)
                        
def win_check(board):
    lst1=[]
    lst2=[]
    lst3=[]
    lst4=[]
    lst5=[]
    lst6=[]
    lst7=[]
    lst8=[]
    lst9=[]
    lst10=[]
    lst11=[]
    lst22=[]
    lst33=[]
    lst44=[]
    lst55=[]
    lst66=[]
    for i in board[0:3]:
        if i ==P1:
            lst1.append(1)
            if len(lst1)==3:
                return 1
                break
            else:
                pass
        elif i==P2:
            lst2.append(1)
            if len(lst2)==3:
                return 2
                break
            else:
                pass

    for i in board[3:6]:

        if i ==P1:
            lst3.append(1)
            if len(lst3)==3:
                return 1
                break
            else:
                pass

        elif i==P2:
            lst4.append(1)
            if len(lst4)==3:
                return 2
                break
            else:
                pass

    for i in board[6:9]:

        if i ==P1:
            lst5.append(1)
            if len(lst5)==3:
                return 1
                break
            else:
                pass
        elif i==P2:
            lst6.append(1)
            if len(lst6)==3:
                return 2
                break
            else:
                pass

    for i in board[0::3]:

        if i ==P1:
            lst7.append(1)
            if len(lst7)==3:
                return 1
                break
            else:
                pass

        elif i==P2:
            lst8.append(1)
            if len(lst8)==3:
                return 2
                break
            else:
                pass

    for i in board[1::3]:

        if i ==P1:
            lst9.append(1)
            if len(lst9)==3:
                return 1
                break
            else:
                pass

        elif i==P2:
            lst10.append(1)
            if len(lst10)==3:
                return 2
                break
            else:
                pass

    for i in board[2::3]:

        if i ==P1:
            lst11.append(1)
            if len(lst11)==3:
                return 1
                break
            else:
                pass

        elif i==P2:
            lst22.append(1)
            if len(lst22)==3:
                return 2
                break
            else:
                pass

    for i in board[0::4]:

        if i ==P1:
            lst33.append(1)
            if len(lst33)==3:
                return 1
                break
            else:
                pass

        elif i==P2:
            lst44.append(1)
            if len(lst44)==3:
                return 2
                break
            else:
                pass

    for i in board[2::2]:

        if i ==P1:
            lst55.append(1)
            if len(lst55)==3:
                return 1
                break
            else:
                pass

        elif i==P2:
            lst66.append(1)
            if len(lst66)==3:
                return 2
                break
            else:
                pass
                                               
def full_board_check(board):
    full_board=[]
    for i in board:
        if i==P1 or i==P2:
            full_board.append(1)
            if len(full_board)==9:
                return 1
    
    
def replay():
    print('if you want to replay  isert 1 in the box  \n if you want to end insert any other charachter')
    if input()=="1":
        return True

    
def Mariamz_Game():   
    
    game_intro()
    while win_check(board)!=1 and full_board_check(board)!=1 and win_check(board)!=2:
               
        while win_check(board)!=2: 
            from IPython.display import clear_output
            clear_output()
            display_board(board)
            player_choice1(board)
            break     
        while win_check(board)!=1 and full_board_check(board)!=1: 
            from IPython.display import clear_output
            clear_output()
            display_board(board)
            player_choice2(board)
            break
        
         
        
            
    else:
        if win_check(board)==1:
            clear_output()
            print ("**********************************")
            print ("***Congratulations Player 1 win***") 
            print ("**********************************")
            print("             GAME OVER")
            if replay():
                Mariamz_Game()
            else:
                clear_output()
                print("Good Bye")

        
        elif full_board_check(board)==1 :
            clear_output()
            print ("**********************************")
            print ("***Congratulations Player 1 win***") 
            print ("**********************************")
            print("             GAME OVER")
            
            if replay():
                Mariamz_Game()
            else:
                clear_output()
                print("Good Bye") 
            
        elif win_check(board)==2:
            clear_output()
            print ("**********************************")
            print ("***Congratulations Player 2 win***") 
            print ("**********************************")
            print("             GAME OVER")
            if replay():
                Mariamz_Game()
            else:
                clear_output()
                print("Good Bye")
            
Mariamz_Game()
