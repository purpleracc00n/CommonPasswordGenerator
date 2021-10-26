import argparse

parser = argparse.ArgumentParser(description='Generate Small Wordlists for Spraying')
parser.add_argument("mode",type=str,help="Mode to use (supports 'words' or 'leaks')")
parser.add_argument("-w","--baseword",type=str,help="Word based on which to generate the list")
parser.add_argument("-f","--baseword_file",type=str,help="Wordlist file based on which to generate the passwords")
parser.add_argument("-c","--complexity",type=str,help="Complexity requirements for the generated passwords (supports lowercase 'l',uppercase 'u',digits 'd',special 's') (example: 'luds'")
parser.add_argument("-l","--length",type=int,help="Minimum length required for the generated passwords.")
parser.add_argument("-s","--small",action='store_true',default=False,help="Create a shorter version of the list")
args = parser.parse_args()

complex_digits=[48,57]
complex_lowercase=[97,122]
complex_uppercase=[65,90]
complex_special1=[33,47]
complex_special2=[58,64]

numbers_short = ['1','2','9','0','01','02','007','123','12345']
special_short = ['!','@']
years_short = ['2021','2020','2000']

numbers = ['1','2','3','4','5','6','7','8','9','0','10','01','02','03','04','05','06','07','08','09','100','1000','123','007','12345','123456','54321','654321']
special = ['!','.','@','#']
years = ['2000','2021','2020','2019','2018','2017','2016','2015','2010']

wordlist = []

def complexity_approved(word):
    if args.complexity is not None:
        if 'd' in args.complexity:
            for i in range(complex_digits[0],complex_digits[1]+1):
                if chr(i) in word:
                    break
            else:
                return False
        if 'l' in args.complexity:
            for i in range(complex_lowercase[0],complex_lowercase[1]+1):
                if chr(i) in word:
                    break
            else:
                return False
        if 'u' in args.complexity:
            for i in range(complex_uppercase[0],complex_uppercase[1]+1):
                if chr(i) in word:
                    break
            else:
                return False
        if 's' in args.complexity:
            valid = 'test'
            for i in range(complex_special1[0],complex_special1[1]+1):
                if chr(i) in word:
                    valid = True
                    break
            else:
                valid = False
            if not valid:
                for j in range(complex_special2[0],complex_special2[1]+1):
                    if chr(i) in word:
                        break
                    else:
                        return False

    if args.length is not None:
        if len(word)<args.length:
            return False
    return True

def generate(word,numbers,years,special):
    for i in numbers:
        if complexity_approved(word+i):
            wordlist.append(word+i)
        for s in special:
            if complexity_approved(word+i+s):
                wordlist.append(word+i+s)
    for y in years:
        if complexity_approved(word+y):
            wordlist.append(word+y)
        for s in special:
            if complexity_approved(word+y+s):
                wordlist.append(word+y+s)

def process_word(word):
    word_lower = word.lower()
    word_capitalized = word.capitalize()
    if args.small == True:
        # generate using the small list of permutations
        # first the word all lowercase
        generate(word_lower,numbers_short,years_short,special_short)
        # then word with first letter capital
        generate(word_capitalized,numbers_short,years_short,special_short)
    else:
        # generate using the full list of permutations
        # first the word all lowercase
        generate(word_lower,numbers,years,special)
        # then word with first letter capital
        generate(word_capitalized,numbers,years,special)
        

if args.mode == "leaks":
    #todo
    pass

if args.mode == "words":
    # process single word
    if args.baseword is not None:
        process_word(args.baseword)
    # process wordlist
    if args.baseword_file is not None:
        with open(args.baseword_file, "r") as words:
            for word in words:
                word = word.rstrip()
                process_word(word)

for word in wordlist:
    print(word)
