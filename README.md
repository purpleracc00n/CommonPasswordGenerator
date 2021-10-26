# CommonPasswordGenerator
(Silly) tool to aid in generating common passwords for spraying based on lists of words.

## Usage

### Generate a short list based on one word
$ pspray_gen.py words -w password -s

### Generate a short list based on a list of words
$ pspray_gen.py words -f wordlist.txt -s

### Generate a list based on a list of words, where passwords have minimum length of 12 and include all of the following: uppercase, lowercase, digits, special characters.
$ pspray_gen.py words -f wordlist.txt -c ulds -l 12


## ToDo
Integrate with leaks / take leaks as input
