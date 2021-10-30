board = [
    [7,0,0,2,0,0,0,0,0],
    [0,1,0,4,0,6,8,0,0],
    [2,6,0,0,0,0,0,4,0],
    [3,0,0,9,0,0,2,1,0],
    [0,0,0,0,0,0,4,7,0],
    [8,0,0,0,0,5,0,0,0],
    [0,3,0,0,4,0,0,0,0],
    [6,0,0,0,9,0,0,0,0],
    [0,0,5,3,1,7,0,2,0]
]

def solve(bo):









def valid(bo,num,pos):
    #for row
    for i in range(len(bo[0])):
        if bo[pos[0],[i]] == num and pos[i] != i: #We gona check each row in column and we gona check that it is same as the numbe  we added in and also if we insent then it dosent bother checking the same number in the same possition  
            return False # while checking if it as the same number we added in then we return false
    #for column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    
    #To figure out which box we are in
    box_x =pos[1] // 3
    box_y =pos[0] // 3
    
    for i in range(box_y*3 , box_x * 3 + 3):
        for j in range(box_x * 3,box_x *3 + 1):
            return False
    return True



def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])): #len of each row
            if j % 3 == 0 and j != 0 :
             print(" | ", end = "")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ",end="")

#Looping through the board to find 0 or empty spaces
def find_empty(bo):
    for i in range(len(bo)): # its len of coloumn
        for j in range(len(bo[0])): #bo[0] represents coloumn
            if bo[i][j] == 0: 
                return(i,j) #i represents row j represents coloumn 
