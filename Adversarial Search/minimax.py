# import numpy as np


# class TicTacToeGame:
#     def __init__(self, game:str) -> None:
#         self.state = game
    
#     def robo_game(self, state:str, player:int, depth:int, alpha:float, beta:float) -> None:
#         self.minimax(state, player, depth, alpha, beta)
    
#     def user_put(self, addr:int) -> None:
#         temp = self.state.split(",")
#         temp[addr-1] = "OO"
#         s = ",".join(temp) 
#         self.state = s
        
#     def str_to_int(self, string) -> int:
#         if string == "XX":
#             return 2

#         elif string == "OO":
#             return 1
        
#         else:
#             return 0
        
#     def equal(self, a, b, c) -> int:
    
#         if a == b == c == 1:
#             return -1

#         elif a == b == c == 2:
#             return 1
        
#         return 0 
    
#     def utility(self):
#         # there is three dimension: Horizontal, Vertical, Dioganl
#         s = self.state.split(",")
#         # Horizontal and Vertical
#         h = 0
#         while h < 3:
#             index = (h * 3) + 3
#             # print(self.str_to_int(s[index-3]), self.str_to_int(s[index-2]), self.str_to_int(s[index-1]))
#             score_v = self.equal(self.str_to_int(s[index-3]), self.str_to_int(s[index-2]), self.str_to_int(s[index-1]))
#             score_h = self.equal(self.str_to_int(s[h]), self.str_to_int(s[h + 3]), self.str_to_int(s[h + 6]))
            
#             h += 1
#             if score_v != 0:
#                 return score_v
            
#             elif score_h != 0:
#                 return score_h
            

#         # main Diagnoal and then subdiagnoal
        
#         score = self.equal(self.str_to_int(s[0]), self.str_to_int(s[4]), self.str_to_int(s[8]))
#         if score != 0:
#             return score
            
#         score = self.equal(self.str_to_int(s[2]), self.str_to_int(s[4]), self.str_to_int(s[6]))
        
#         if score != 0:
#             return score
            
#         # if none of them is win:
#         return 0
    
#     def player_decode(self, player) ->int:
#         if player == 1:
#             return "XX"
        
#         else:
#             return "OO"
    
    
#     def is_terminal(self):
#         s = self.state.split(",")

#         for i in range(3):
#             h = (i * 3) + 3

#             if self.equal(self.str_to_int(s[h - 3]), self.str_to_int(s[h - 2]), self.str_to_int(s[h - 1])) != 0:
#                 return True 
            
#             if self.equal(self.str_to_int(s[i]), self.str_to_int(s[i + 3]), self.str_to_int(s[i + 6])) != 0:
#                 return True
              
#         if self.equal(self.str_to_int(s[0]), self.str_to_int(s[4]), self.str_to_int(s[8])) != 0:
#             return True

#         if self.equal(self.str_to_int(s[2]), self.str_to_int(s[4]), self.str_to_int(s[6])) != 0:
#             return True
        
#         if all(self.str_to_int(cell) != 0 for cell in s):
#             return True
        
#         return False

        
    
#     def minimax(self, player:int, alpha:float=-np.inf, beta:float=np.inf):
#         if self.is_terminal():
#             return self.utility()

#         if player:
#             a = 0
#             maxeval = -np.inf
#             # print(self.state, "max")
#             while a < 9:
#                 player_dec = self.player_decode(player)
#                 temp = self.state.split(",")
#                 temp = temp[a]
                
#                 if self.str_to_int(temp) == 0:
#                     old_state = self.state
#                     s = self.state.split(",")
#                     s[a] = player_dec 
#                     self.state = ",".join(s) 
#                     eval = self.minimax(0, alpha, beta)
#                     self.state = old_state
                 
#                     maxeval = max(maxeval,eval)
#                     alpha = max(alpha, eval)
#                     if beta <= alpha:
#                         break
#                 a += 1
           
#             return maxeval 

#         else:
#             a = 0
#             mineval = np.inf
#             # print(self.state, "min")
#             while a < 9:
#                 player_dec = self.player_decode(player)
#                 temp = self.state.split(",")
#                 temp = temp[a]
#                 if self.str_to_int(temp) == 0:
#                     old_state = self.state
#                     s = self.state.split(",")
#                     s[a] = player_dec 
#                     self.state = ",".join(s)
#                     eval = self.minimax(1, alpha, beta)
#                     self.state = old_state

#                     mineval = min(mineval, eval)
#                     beta = min(beta, eval)
#                     if beta <= alpha:
#                         break
#                 a += 1
#             return mineval


# # game tic-tac-toe it has 9 dimension and max player=0 is cross and min player=1 is circle
# #            1 | 2 | 1
# #           ------------
# #            0 | 2 | 1
# #           -------------
# #            0 | 2 | 0
# # 00 = 0 OO = 1 XX = 2
# # we convert the tic-tac-toe to bitwise representation each row has 6 bits e.g for above it will
# #     1 2 3    4 5 6   7 8 9
# # be XXOOXX / 00OOXX / 00OO00 and for finding position of player 0 as we know in thses direction
# # -> +1  down = +3 main_diognal = +4 and non_main_diognal = +2 

# initial_game = "00,00,00,00,00,00,00,00,00"


# def play_game():
#     game = TicTacToeGame(initial_game)     
#     player = 0
#     while not game.is_terminal():
#         if player == 0: # OO = 0 or human
#             move = input("Your Turn: ")
#             game.user_put(int(move))
            
#         else:
#             # XX = 1 or robot
#             best_move = None
#             best_value = float('-inf')
#             a = 0
#             while a < 9:

#                 player_dec = game.player_decode(player)
#                 temp = game.state.split(",")
#                 temp = temp[a]
#                 if game.str_to_int(temp) == 0:
#                     old_state = game.state
#                     s = game.state.split(",")
#                     s[a] = player_dec 
#                     s = ",".join(s) 
#                     game.state = s
                    
#                     move_value = game.minimax(1)
                    
#                     game.state = old_state

#                     if move_value > best_value :
#                         best_value = move_value
#                         best_move = a
#                 a += 1
            
#             s = game.state.split(",")
#             s[best_move] = "10"
#             s = ",".join(s)
#             game.state = s
#             player = 1
            
#         player = 1

#     print(game.state)
#     if game.utility(game.state) == 1:
#         print("Human wins! :)")
#     elif game.utility(game.state) == -1:
#         print("Robot wins! :( ")
#     else:
#         print("It's a draw! :( :( ")

# play_game()



#Tic-Tac-Toe using Mini-Max Algorithm
#Vineet Joshi
#GEU,Dehradun
"""-----------------------"""

#This function is used to draw the board's current state every time the user turn arrives. 
def ConstBoard(board):
    print("Current State Of Board : \n\n");
    for i in range (0,9):
        if((i>0) and (i%3)==0):
            print("\n");
        if(board[i]==0):
            print("- ",end=" ");
        if (board[i]==1):
            print("O ",end=" ");
        if(board[i]==-1):    
            print("X ",end=" ");
    print("\n\n");

#This function takes the user move as input and make the required changes on the board.
def User1Turn(board):
    pos=input("Enter X's position from [1...9]: ");
    pos=int(pos);
    if(board[pos-1]!=0):
        print("Wrong Move!!!");
        exit(0) ;
    board[pos-1]=-1;

def User2Turn(board):
    pos=input("Enter O's position from [1...9]: ");
    pos=int(pos);
    if(board[pos-1]!=0):
        print("Wrong Move!!!");
        exit(0);
    board[pos-1]=1;

#MinMax function.
def minimax(board,player):
    x=analyzeboard(board);
    if(x!=0):
        return (x*player);
    pos=-1;
    value=-2;
    for i in range(0,9):
        if(board[i]==0):
            board[i]=player;
            score=-minimax(board,(player*-1));
            if(score>value):
                value=score;
                pos=i;
            board[i]=0;

    if(pos==-1):
        return 0;
    return value;
    
#This function makes the computer's move using minmax algorithm.
def CompTurn(board):
    pos=-1;
    value=-2;
    for i in range(0,9):
        if(board[i]==0):
            board[i]=1;
            score=-minimax(board, -1);
            board[i]=0;
            if(score>value):
                value=score;
                pos=i;
 
    board[pos]=1;


#This function is used to analyze a game.
def analyzeboard(board):
    cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];

    for i in range(0,8):
        if(board[cb[i][0]] != 0 and
           board[cb[i][0]] == board[cb[i][1]] and
           board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][2]];
    return 0;

#Main Function.
def main():
    choice=input("Enter 1 for single player, 2 for multiplayer: ");
    choice=int(choice);
    #The broad is considered in the form of a single dimentional array.
    #One player moves 1 and other move -1.
    board=[0,0,0,0,0,0,0,0,0];
    if(choice==1):
        print("Computer : O Vs. You : X");
        player= input("Enter to play 1(st) or 2(nd) :");
        player = int(player);
        for i in range (0,9):
            if(analyzeboard(board)!=0):
                break;
            if((i+player)%2==0):
                CompTurn(board);
            else:
                ConstBoard(board);
                User1Turn(board);
    else:
        for i in range (0,9):
            if(analyzeboard(board)!=0):
                break;
            if((i)%2==0):
                ConstBoard(board);
                User1Turn(board);
            else:
                ConstBoard(board);
                User2Turn(board);
         

    x=analyzeboard(board);
    if(x==0):
         ConstBoard(board);
         print("Draw!!!")
    if(x==-1):
         ConstBoard(board);
         print("X Wins!!! Y Loose !!!")
    if(x==1):
         ConstBoard(board);
         print("X Loose!!! O Wins !!!!")
       

main()


