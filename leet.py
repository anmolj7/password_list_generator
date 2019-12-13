from itertools import combinations as pmt 

with open('text.txt') as f:
    lines = f.readlines()

Leet_Dict = {}
for line in lines:
    char, char_leet = line.split(' = ')
    Leet_Dict[char] = char_leet.strip('\n').strip()

def replace_char(text: str, indices: list, replace_dict: dict):
    #Indices contains the list of the indexes that need to be replaced. Whereas replace_dict
    #is a hash map which contains the conversion values.
    
    text = list(text) #beacause string is immutable.

    for index in indices:
        if text[index].upper() in replace_dict:
            text[index] = replace_dict[text[index].upper()]
    
    return ''.join(text)


def text_to_leet(text, leet_dict=Leet_Dict):
    #Now, 
    #The thing is, it's not necessary that every text is converted to leet, 
    #it's possible that words are like this: 4nm0L or A|\|M0L, so, what we gotta do 
    #in order to cover every possible permutation is, loop from 1 to len(text) and then, select 
    #That number of letters, and convert them into leet, for example, if i == 1, we'll just convert one letter to leet.

    Permutations = [text] #When we don't convert anything into leet.
    
    for i in range(1, len(text)+1):
        possible_Is = list(pmt(range(len(text)), i))
        #Possible Is is the list of all the indexs that are leet-ed at a certain point if that makes sense
        #For example, 
        #If possible_Is = [(1, 2), (3, 4)] what it means is, the possiblities are that at a certain time, 1 is leeted along with 2 or the second time, 3 is leet-ed with 4th character.
        for curr_possible in possible_Is:
            temp =  replace_char(text, curr_possible, leet_dict)
            Permutations.append(temp)

    return list(set(Permutations))

def main():


    print(text_to_leet('text', Leet_Dict))

if __name__ == "__main__":
    main()