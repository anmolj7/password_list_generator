import itertools
from leet import text_to_leet 
import os

def clear():
    os.system('clear')

def breakline():
    print('-'*27)

class GenerateList:
    def __init__(self, N:int):
        self.vars = []
        self.min_len = 1
        self.max_len = 999999
        self.take_input(N)
    
    def take_input(self, N=6):
        done = False 
        i = 0 
        while i < N and not done:
            if i < N:
                temp = input(f'Text {i+1}: ')
                self.vars.append(temp)
            else:
                temp = input(f'Press enter to start generating wordlist, else text {i+1}: ')
                if len(temp) > 0:
                    self.vars.append(temp)
                else:
                    done = True 
            i += 1
        temp = input('Enter the minimum length of password (Press enter to keep the default 1): ')
        if len(temp) > 0:
            self.min_len = int(temp)

        temp = input('Enter the maximum length of password (Press enter to keep it variable): ')
        if len(temp) > 0:
            self.max_len = int(temp)

    def product_dict(self, **kwargs):
        keys = kwargs.keys()
        vals = kwargs.values()

        for instance in itertools.product(*vals):
            yield instance 
        
    def create_list(self, List: list):
        Dict = {str(x):List[x] for x in range(len(List))}
        return list(set(self.product_dict(**Dict)))

    def generate(self):
        for i in range(len(self.vars)):
            self.vars[i] = [self.vars[i].capitalize(), self.vars[i]]+text_to_leet(self.vars[i])
            self.vars[i] = list(set(self.vars[i]))

        Words = self.create_list(self.vars)
        N = len(Words)
        clear()
        
        word_list = []

        fName = input('File Name you wanna store the word list in: ')

        with open(fName, 'w') as f:
            for i, words in enumerate(Words):
                i += 1 
                clear()
                percent = (i/N)*100
                breakline()
                print('Generating Wordlist')
                breakline()
                print(f'{round(percent, 2)}%')
                breakline()

                for xs in itertools.product(words, repeat=len(words)):
                    temp = []
                    for x in xs:
                        if x not in temp:
                            temp += x 
                    temp = ''.join(temp)
                    if len(temp) in range(self.min_len, self.max_len+1):
                        if temp not in word_list:
                            word_list.append(temp)
                            f.write(temp+'\n')
                            f.flush()

        print(f'Generation Complete, stored in {fName}')

def main():
    GenerateList(int(input('Enter the number of variables you wanna input: '))).generate()

if __name__ == "__main__":
    main()