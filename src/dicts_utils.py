#Jeremy Smith - 260948914 - COMP202 A3 - dicts_utils
def count_occurrences(s):
    '''(str) -> dict
    Takes as input a string and returns a dictionary where the keys are characters in the input string and those keys map to the number of times the character appears in the string
    >>>count_occurrences('blueberry')
    {'b': 2, 'l': 1, 'u': 1, 'e': 2, 'r': 2, 'y': 1}
    >>>count_occurrences('grown')
    {'g': 1, 'r': 1, 'o': 1, 'w': 1, 'n': 1}
    >>>count_occurences('hello there')
    {'h': 2, 'e': 3, 'l': 2, 'o': 1, ' ': 1, 't': 1, 'r': 1}
    '''
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            #d begins as an empty dict so this creates a key for the each unique letter in the word and maps it to value 1
            d[s[i]]=1
        else:
            #if the key (or letter) is already in the dict its mapped value is incremented by 1
            d[s[i]]+=1
    return d

def flatten_dict(d):
    '''(dict)->list
    takes as input a dictionary where values are non negative integers and returns a list with the keys from the dict are present dict[key] amount of times
    >>>flatten_dict({'g': 1, 'r': 1, 'o': 1, 'w': 1, 'n': 1})
    ['g', 'r', 'o', 'w', 'n']
    >>>flatten_dict({'c': 1, 'a': 1, 't': 1, 'cat': 2, 'dog': 0})
    ['c', 'a', 't', 'cat', 'cat']
    >>>flatten_dict({'c': 0, 'b': 0, 'a': 0})
    []
    '''
    my_list = []
    for key in d:
        #to iterate through each key in d
        c = 0
        while c < d[key]:
            #using a while loop so that they key is appended to the list however many times its value indicates
            my_list.append(key)
            c+=1
    return my_list
        
def get_word_score(s,v):
    '''(str, dict)->int
    takes as input a dict mapping letters to their worth in points and a string for which you would like to know the total point worth. the function returns the amount of points given for the word
    >>>get_word_score('&^%',{'a': 5, 't': 3, 'n': -2})
    0
    >>>get_word_score('jeremy',{'j': 5, 'e': 3, 'r': 1, 'm': 3, 'y': 6})
    21
    >>>get_word_score(' ',{'a': 5, 't': 3, 'n': -2})
    0
    '''
    sum = 0
    for i in range(len(s)):
        if s[i] not in v:
            #if the letter is not in the dictionary we will not increase the word score
            continue
        else:
            #when the letter is in the dict the word score is incremented by the value associated with the key (or letter)
            sum+=v[s[i]]
    return sum

def is_subset(a,b):
    '''(dict, dict)->bool
    takes two dictionaries that map to non-neg ints and checks if the first dict is a subset of the second. if so, the function returns true. Otherwise it returns false
    >>>a={'a': 3, 'b': 4, 'c': 2, 'd': 1, 'e': 5}
    >>>b={'a': 8, 'b': 4, 'c': 6, 'd': 1, 'e': 5}
    >>>c={'a': 2, 'e': 4}
    >>>is_subset(a,b)
    True
    >>>is_subset(b,a)
    False
    >>>is_subset(a,c)
    False
    '''
    for key in a:
        if key in b and a[key]<=b[key]:
            x = True
            #wasnt sure if an if statement can be empty so i threw this in incase
        else:
            #when one of the conditions is not met we immediately return false since otherwise the x of the last item checked is returned
            return False
    return x

def subtract_dicts(d1,d2):
    '''(dict, dict)->bool
    takes two dicts as input and checks if the second is a subset of the first. If that is the case then the smaller dictionary is subtracted from the larger one
    >>>
    >>>
    >>>
    '''
    if is_subset(d2,d1):
        #only subtracts dictionaries that are subsets of the bigger dict
        for key in d2:
            #using the keys in the smaller dictionary since all indices of the smaller dict are in the larger one and we are only subtracting when they are in both
            d1[key] = d1[key] - d2.get(key)
            #suntract the value of the key in d2 from the matching key in d1
            if d1[key] == 0:
                #when the value of a key is 0 after the subtracting we delete the key from d1
                #we'll never have a key map to a negative value since we already check if the d2 is a subset of d1
                del d1[key]
        return True
    else:
        #when d2 isnt a subset of d1 we return false since the subtraction cannot be done
        return False
    
def create_scrabble_dict(w):
    '''(list)->dict
    the function takes as input a list of strings and returns them in a 2D dictionary where the length of string maps to a dictionary where the \
    keys are letters mapping to words where the key is the first letter in th word
    >>> w = ['aa', 'qi', 'za', 'cat', 'can', 'cow', 'dog', 'dad', 'hippo', 'umami', 'uncle']
    >>> d = create_scrabble_dict(w)
    >>> d == {2 : {'a': ['aa'], 'q': ['qi'], 'z': ['za']}, 3 : {'c': ['cat', 'can', 'cow'], \
    'd': ['dog', 'dad']}, 5 : {'h': ['hippo'], 'u' : ['umami', 'uncle'] }}
    True
    >>> w = ['happy', 'sad', 'angry', 'jealous', 'joy', 'disgust', 'greed', 'hate', 'cheerful', 'confused', 'ambiguous']
    >>> d = create_scrabble_dict(w)
    >>> d == {5: {'h': ['happy'], 'a': ['angry'], 'g': ['greed']}, 3: {'s': ['sad'], 'j': ['joy']}, 7: {'j': ['jealous'], 'd': ['disgust']}, \
    4: {'h': ['hate']}, 8: {'c': ['cheerful', 'confused']}, 9: {'a': ['ambiguous']}}
    True
    >>> w = ['$%*(:)', 'runner', 'hel*lo', 'halt', '**', '$$$', '(((', 'hello', 'stop', 'correlate', 'golden']
    >>> d = create_scrabble_dict(w)
    >>> d == {6: {'$': ['$%*(:)'], 'r': ['runner'], 'h': ['hel*lo'], 'g': ['golden']}, 4: {'h': ['halt'], 's': ['stop']}, 2: {'*': ['**']}, \
    3: {'$': ['$$$'], '(': ['(((']}, 5: {'h': ['hello']}, 9: {'c': ['correlate']}}
    True
    '''
    d1={}
    for word in w:
        #iterates through each word in the input list
        if len(word) not in d1:
            #creates a key representing string length for all lengths not already in the dict
            d1[len(word)]={}
            #the value that the key will map to is an empty dict 
    for key in d1:
        #for each key in d1 just restating its an empty dict - not necessary 
        d1[key]={}
        for word in w:
            #iterates through the word list 
            if word[0] not in d1[key]:
                #if the first char in the word is not already a key of the sub dict we create it and it maps to a value which is an empty list
                d1[key][word[0]]=[]
            if word not in d1[key][word[0]] and len(word)==key:
                #all the words that arent already in the list-values of the subdict will be added if they have the correct first letter and word length
                d1[key][word[0]].append(word)
            if len(d1[key][word[0]])==0:
                #removes any occurence of empty lists in the subdict values if they should occur
                del d1[key][word[0]]
    return d1

def is_valid_word(s,d):
    '''(str, dict)->bool
    takes a string and a dictionary formated like the returned dict from create_scrabble_dict as input and returns True if the input string is in the dict. Otherwise returns false
    >>> w = ['happy', 'sad', 'angry', 'jealous', 'joy', 'disgust', 'greed', 'hate', 'cheerful', 'confused', 'ambiguous']
    >>> d = create_scrabble_dict(w)
    >>> is_valid_word('hippo', d)
    False
    >>> is_valid_word('joy', d)
    True
    >>> is_valid_word('%^$#%& fydtdg', d)
    False
    '''
    for key in d:
        #iterates through the keys in d
        for x in d[key]:
            #iterates through the keys in the subdict
            if s in d[key][x[0]]:
                #checks if the string is in list value of the subdict  
                return True
            else:
                continue
    return False