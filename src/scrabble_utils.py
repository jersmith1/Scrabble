#Jeremy Smith - 260948914 - COMP202 A3 - scrabble_utils
import dicts_utils, board_utils, random

def display_rack(r):
    '''(dict)->None
    this function takes as input a dict representing the rack of the player and prints it out (returns nothing)
    >>>display_rack({'a': 3, 'b': 4, 'c': 2, 'd': 1, 'e': 5})
    A A A B B B B C C D E E E E E 
    >>>display_rack({'a': 2, 'x': 1, 't': 2, 'k': 1, 'z': 2})
    A A X T T K Z Z
    '''
    for key in r:
        #prints each key in upper case as many times as its mapped value with a space in between each letter on the rack
        print((key.upper()+' ')*r[key],end='')
        
def has_letters(r,s):
    '''(dict, str)->bool
    the function takes as input the dictionary that represents the player's rack and a string. If the string can be fomed using the the available \
    letters from the rack, the function returns true. (otherwise, false)
    >>>r={'a': 2, 'x': 1, 't': 2, 'k': 1, 'n': 2, 'e': 1}
    >>>has_letters(r, 'taken')
    True
    >>>r=={'a': 1, 'x': 1, 't': 1, 'n': 1}
    True
    >>>r={'a': 2, 'x': 1, 't': 2, 'k': 1, 'n': 2, 'e': 1}
    >>>has_letters(r, 'markers')
    False
    >>>r=={'a': 2, 'x': 1, 't': 2, 'k': 1, 'n': 2, 'e': 1}
    True
    >>>r={'a': 2, 'r': 1, 't': 2, 'q': 1, 'n': 2, 'e': 1}
    >>>has_letters(r, 'treats')
    False
    >>>r=={'a': 2, 'r': 1, 't': 2, 'q': 1, 'n': 2, 'e': 1}
    True
    >>>r={'a': 2, 'r': 1, 't': 2, 's': 1, 'n': 2, 'e': 1}
    >>>has_letters(r, 'treats')
    True
    >>>r=={'a': 1, 'q': 1, 'n': 2}
    True
    '''
    word_dict={}
    #creates an empty dict which will have key representing each letter of s
    for char in s:
        #iterates through each char is s
        word_dict[char]=s.count(char)
        #each char key maps to an int coming from using the count(char) function on the string (i.e. the number of times a specific char is in s)
    if dicts_utils.is_subset(word_dict,r):
        #calling on subratct dicts function
        dicts_utils.subtract_dicts(r,word_dict)
        return True
    else:
        return False
    
def refill_rack(r,b,n):
    '''(dict, dict, int)->None
    the function takes as input two dictionaries which represent the bag of tiles to choose from and the players rack, \
    the int taken as input represents the number of tiles needed on the rack. The function keeps adding a tile from the bag to the rack and adjusting both dicts until that number is reached
    >>> random.seed(6)
    >>> r = {'q': 2, 'r':1}
    >>> b = {'a': 1, 'e': 2, 'h': 1, 'l': 2, 'n': 1, 'p': 2, 's': 3, 't': 2, 'z': 1}
    >>> refill_rack(r, b, 8)
    >>> r == {'q': 2, 'r': 1, 's': 1, 'a': 2, 'e': 2}
    True
    >>> b == {'h': 1, 'l': 2, 'n': 1, 'p': 2, 's': 2, 't': 2, 'z': 1}
    True
    >>> random.seed(7)
    >>> r={'a': 1, 'd':3}
    >>> b={'a':4,'b':3,'c':1,'e':7,'g':4,'f':3,'t':3,'y':2}
    >>> refill_rack(r, b, 12)
    >>> r == {'a': 3, 'd': 3, 'e': 1}
    True
    >>> b == {'a': 2, 'b': 3, 'c': 1, 'e': 6, 'g': 4, 'f': 3, 't': 3, 'y': 2}
    True
    >>> random.seed(9)
    >>> r = 'r': 2, 'y': 1}
    >>> b = {'a':4,'b':3,'c':1,'e':7,'g':4,'f':3,'t':3,'y':2}
    >>> refill_rack(r, b, 9)
    >>> r == {'r': 2, 'y': 1, 'a': 1, 'e': 1}
    True
    >>> b == {'a': 3, 'b': 3, 'c': 1, 'e': 6, 'g': 4, 'f': 3, 't': 3, 'y': 2}
    True
    '''
    current_tiles=0
    for key in r:
            current_tiles+=r[key]
            #to get to the amount of tiles we currently have on the rack were taking the sum of each value in the r dict
    while current_tiles<n:
        #n represents the needed o=amount of tiles on the rack for the begining of the next turn
        bag=dicts_utils.flatten_dict(b)
        #flatten the dict into a list so that random.choice chan be used
        new_tile=random.choice(bag)
        #chooses a random item from the list
        #the player has a higher chance to pick a letter that is in the bag multiple times since the letter is added to the list its value amount of times
        if new_tile in b:
            b[new_tile]-=1
            #subtracts 1 from the value of the key that was added to the rack (removed from the bag)
            #this subtraction from the dict has an effect on the list that is used for random.choice since at the top of the loop the new dict is re-flattened
            if b[new_tile]==0:
                del b[new_tile]
                #if the value of the key is zero it means that we have no more of that letter in the bad so we delete it
        if new_tile not in r:
            r[new_tile]=1
            #when the player's rack doesn't already have the same letter that was picked, the value of that letter (key) is 1
        else:
            r[new_tile]+=1
            #if the player already has that tile. The amount of that same letter is incremented by 1
        current_tiles+=1
        #increment the current tiles so that we end with exactly n tiles (see first comment)

def compute_score(a,v,d):
    '''(list, dict, dict)->int
    >>> v = {'a': 1, 'p': 3, 'h': 2, 'o': 1, 'j': 5, 'r': 3, 'g': 1, 'e': 1, 'd': 2, 'y': 6}
    >>> w = ['happy', 'sad', 'angry', 'jealous', 'joy', 'disgust', 'greed', 'hate', 'cheerful', 'confused', 'ambiguous']
    >>> d = dicts_utils.create_scrabble_dict(w)
    >>> compute_score(['greed', 'joy'], v, d)
    20
    >>> compute_score(['umami', 'zebra'], v, d)
    0
    >>> compute_score(['$$$$$'], v, d)
    0
    '''
    score=0
    for i in range(len(a)):
        if dicts_utils.is_valid_word(a[i],d):
            score+=dicts_utils.get_word_score(a[i],v)
            #verifies that the words in the list are in the dictionary and gets the score of each word
            #the score of each word is added to the starting score (0) until all word scores are calculated
        else:
            score=0
            #as soon as 1 of the words in the list is not in the dict, the score is set to zero and we break the function
            break
    return score

def place_tiles(b, s, row, col, d):
    '''(list, str, int, int, str) -> list
    >>>
    >>>
    >>>
    '''
    i=row
    j=col
    w=[]
    for char in s:
        if d=='right':
            if b[i][j]==' ':
                b[i][j]=char
                j+=1
            else:
                b[i][j]=b[i][j]
                j+=1
        elif d=='down':
            if b[i][j]==' ':
                b[i][j]=char
                i+=1
            else:
                b[i][j]=b[i][j]
                i+=1
    if d=='right':
        w.append(board_utils.find_word(b[i],j))
    elif d=='down':
        c=board_utils.get_vertical_axis(b, j)
        w.append(board_utils.find_word(c,0))
    return w

def make_a_move(b, r, s, row, col, d):
    if d=='right':
        l=b[row]
        x=col
    elif d=='down':
        l=board_utils.get_vertical_axis(b,col)
        x=row
    else:
        return ''
    if board_utils.fit_on_board(l, s, x)==False:
        raise IndexError ("Not enough space on board.")
    if dicts_utils.is_subset(dicts_utils.count_occurrences(s), r)==False:
        raise ValueError ("Not all tiles are present in your rack")
    else:
        dicts_utils.subtract_dicts(r, dicts_utils.count_occurrences(s))
        return place_tiles(b, s, row, col, d)