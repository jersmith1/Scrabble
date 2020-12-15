#Jeremy Smith - 260948914 - COMP202 A3 - board_utils
def create_board(m,n):
    """(int, int) -> list
    Constructs and returns a two dimensional list of strings that represents the empty scrabble board
    >>>create_board(5,5)
    [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
    >>>create_board(1,6)
    [[' ', ' ', ' ', ' ', ' ', ' ']]
    >>>create_board(-4,3)
    Traceback (most recent call last):
    ValueError: Inputs must be positive
    """
    #create empty lists representing b (board) and rows
    rows = []
    b = []
    if m<=0 or n<=0:
        #it is impossible to have a negative number of rows or columns so if the inputs given are negative this ValueError is raised
        raise ValueError("Inputs must be positive")
    while len(rows)<n:
        #builds a list that represents a row with n number of columns, displayed as ' '
        rows.append(' ')
    while len(b)<m:
        #keeps adding rows of the same length until the inputed amount is reached
        b.append(rows)
    return b

def display_board(b):
    '''(list) -> None
    takes as input a list comprised of sublists that correspond to the rows of the scrabble boards and returns nothing
    >>>b = [[' ', ' ', ' ', ' ', ' '], [' ', 'J', 'E', 'R', ' '], [' ', ' ', ' ', ' ', ' '],\
    ['S', 'M', 'I', 'T', 'H'], [' ', ' ', ' ', ' ', ' ']]
    >>>display_board()
        0   1   2   3   4
      +-------------------+
    0 |   |   |   |   |   |
      +-------------------+
    1 |   | J | E | R |   |
      +-------------------+
    2 |   |   |   |   |   |
      +-------------------+
    3 | S | M | I | T | H |
      +-------------------+
    4 |   |   |   |   |   |
      +-------------------+
    >>>b = [[' ',' '],[' ',' ',' ']]
    >>>display_board(b)
        0   1   2
      +-----------+
    0 |   |   |
      +-----------+
    1 |   |   |   |
      +-----------+
    >>>b =[[' ','W','H','A','T','S'],[' ',' ',' ',' '],[' ',' '],[' ',' ','U','P','?']]
    >>>display_board(b)
        0   1   2   3   4   5
      +-----------------------+
    0 |   | W | H | A | T | S |
      +-----------------------+
    1 |   |   |   |   |
      +-----------------------+
    2 |   |   |
      +-----------------------+
    3 |   |   | U | P | ? |
      +-----------------------+
    '''
    r = 1
    #will be used to indicate the number of the col on the top row, starts at 1 since 0 is printed out earlier and formatted differently to account for the spaces ahead of it
    print('    0',end='')
    x = 0
    for i in range(len(b)):
        if len(b[i])>x:
            #allows us to find the longest row so that we ensure it'll be reached by the division between rows
            x = len(b[i])
        while r<x:
            print('  ',r,end='')
            #prints the top line of integers indication the number of column
            r+=1
        print('\n  +---'+'----'*(x-1)+'+')
        print(i,'|',end='')
        for element in b[i]:
            print('',element,'|',end='')
            #prints each element in the correct space, essentially giving the empty board a grid interior 
    print('\n  +---'+'----'*(x-1)+'+')

def get_vertical_axis(b,x):
    '''(list, int) -> list
    takes a two dimensional list representing the board and an integer indicating which column is to be chosen and then returns the desired column
    >>>b=[[' ','H','E','Y',' '],['T','H','E','R','E'],['G','U','Y',' ',' ']]
    >>>get_vertical_axis(b,2)
    ['E', 'E', 'Y']
    >>>b=[[' ',' '],[' ',' ']]
    >>>get_vertical_axis(b,5)
    Traceback (most recent call last):
    IndexError: list index out of range
    >>>b=[['T',' ',' '],['H','E','Y'],['E',' ',' '],['R',' ',' '],['E',' ',' ']]
    >>>get_vertical_axis(b,0)
    ['T', 'H', 'E', 'R', 'E']
    '''
    col = []
    #an empty list which will represent the column at the inputed integer
    for i in range(len(b)):
        col.append(b[i][x])
    return col

def find_word(l,x):
    '''(list, int) -> str
    Takes a list of strings and and integer as input and returns only the word made up of consecutive single character strings that contains the input integer if the character at the integer is a space char, an empty string is returned
    >>>find_word([' ',' ','A'],0)
    ''
    >>>find_word(['J','E','R',' ','S','M','I','T','H'],6)
    'SMITH'
    >>>find_word([' ','H','','E','L','L','O',' ','T','H','E','R','E'],3)
    'HELLO'
    '''
    list_1=[]
    s=''
    y=x+1
    while x>=0:
        if l[x]==' ':
            break
        else:
            list_1.append(l[x])
        x-=1
        #starting from the input integer we move backwards and append all characters before the one at the input int, once a space char is reached, we break.If no space is reached we break at the start of the list
    list_1=list_1[::-1]
    #since at the moment the list is flipped we have to flip it back
    while y<=(len(l)-1):
        if l[y]==' ':
            break
        else:
            list_1.append(l[y])
        y+=1
        #we pick up from y which is one spot t the right of x (since x is already included in the list, the we keep appending chars until a space is reached, then we break. If no space is reached we break at the end of the list
    for i in range(len(list_1)):
        s+=list_1[i]
        #adds each element of the list into the empty string s
    return s

def available_space(r,i):
    '''(list, int) -> int
    takes a list of char strings (a row) and an integer representing the starting position. The function counts the number of empty squared to the right of and including the integer given in the input
    >>>available_space(['J','E',' ',' ','R',' ',' ','S'],1)
    4
    >>>available_space(['H','I'],0)
    0
    >>>available_space(['H','I'],7)
    0
    '''
    c=0 #counter representing the number of spaces
    while i<=(len(r)-1):
        if r[i]==' ':
            #when the char in position i in r is a space char, we increment the counter and i
            c+=1
            i+=1
        else:
            #otherwise we only increment i and keep the counter at its current position and continue the loop
            i+=1
            continue
    return c

def fit_on_board(a, letters, i):
    '''(list, str, int) -> bool
    Takes as input a list of character strings, a string representing the word you would like to place and an integer starting point. The function conts the available spaces and returns True if the word you would like to place fits on the board
    >>>a=['w', 'x', ' ', 'y', ' ', ' ', 'z', ' ', ' ']
    >>>fit_on_board(a, 'SWIM', 1)
    True
    >>>a=['a', 'b', ' ', 'c', ' ']
    >>>fit_on_board(a, 'DOG', 3)
    False
    >>>a=['a', 'b', ' ', 'c', ' ']
    >>>fit_on_board(a, 'SWIM', 8)
    False
    '''
    if available_space(a,i)>=len(letters):
        return True
    else:
        return False