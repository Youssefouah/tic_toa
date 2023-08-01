 # Write Python 3 code in this online editor and run it.
tic = [["","",""],
       ["","",""],
       ["","",""]]

final = True
ref = 0


def score ():
       #condition for row player 1
    condition1 = (tic[0][0] == tic[0][1] == tic[0][2] == "X") or (tic[1][0] == tic[1][1] == tic[1][2] == "X") or (tic[2][0] == tic[2][1] == tic[2][2]== "X")
    condition2 = (tic[0][0] == tic[1][0] == tic[2][0]== "X") or (tic[0][1] == tic[1][1] == tic[2][1]== "X") or (tic[0][2] == tic[1][2] == tic[2][2]== "X")
    condition3 = (tic[0][0] == tic[1][1] == tic[2][2]== "X") or (tic[0][2] == tic[1][1] == tic[2][0]== "X")
    
     #condition for row player 2
    condition4 = (tic[0][0] == tic[0][1] == tic[0][2]== "O") or (tic[1][0] == tic[1][1] == tic[1][2]== "O")or (tic[2][0] == tic[2][1] == tic[2][2]== "O")
    condition5 = (tic[0][0] == tic[1][0] == tic[2][0]== "O") or (tic[0][1] == tic[1][1] == tic[2][1]== "O") or (tic[0][2] == tic[1][2] == tic[2][2]== "O")
    condition6 = (tic[0][0] == tic[1][1] == tic[2][2]== "O") or (tic[0][2] == tic[1][1] == tic[2][0]== "O")
    if ( condition1 or condition2 or condition3):
            print("game is over")
            print("player 1 win")
            return 1
    if ( condition4 or condition5 or condition6):
            print("game is over")
            print("player 2 win") 
            return 1
    else:
         return 0 


while final == True:
    
    #verifie if the game is finish
    for j in range(0,3):
        for k in range(0,3):
            if tic[j][k] != "":
                ref = ref +1           
    if ref == 9 :
        print("game is over")
        print("draw")
        break

    #player one play
    print("player 1")
   # print "X"
    #player one choose the place 
    print("place in row")
    move1 = int(input()) # place in axis
    print("place in column")
    move2 = int(input()) #place in column
    #complete the tic for player 1
    tic[move1][move2] = "X"
    print(tic)
    if score() == 1:
         break
    print("#################################################")
    
    #player two play
    print("player 2")
  # print "O"
    #player one choose the place 
    print("place in row")
    move3 = int(input()) # place in axis
    print("place in column")
    move4 = int(input()) #place in column
    #complete the tic for player 2
    tic[move3][move4] = "O"
    print(tic)
    if score() == 1:
         break
    print("#################################################")
    
 
            