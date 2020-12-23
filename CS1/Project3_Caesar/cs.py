import sys # Needed to access the arguments given in command line

def enc(k, plaintext):
    """Encode the given plaintext
    with Caesar cipher and shift key k.
    Change only lowercase characters,
    Keep other characters.
    Return the corresponding ciphertext.
    """
    c = list(plaintext.encode("ascii"))
    k %= 26
    for i in range(len(c)):
        if 97 <= c[i] <= 122:
            c[i] = (c[i] - 97 + k) % 26 + 97
        elif 65 <= c[i] <= 90:
            c[i] = (c[i] - 65 + k) % 26 + 65
        elif 48 <= c[i] <= 57:
            c[i] = (c[i] - 48 + k) % 10 + 48
    return bytes(c).decode("ascii")         # If a letter is a lowercase, shift it k letters.

def dec(k, ciphertext):
    """Decode the given ciphertext
    with Caesar cipher and shift key k.
    Change only lowercase characters,
    Keep other characters.
    Return the corresponding plaintext.
    """
    return enc(-k, ciphertext)              # I used encrypt function with key = -k

n = [i for i in range(1,27)]
freq = [0] * 26                             # array of frequency, initial vale = 0

def countFreq(ciphertext):                  # Function used for count the frequency of each letter.
    c = list(ciphertext.encode("ascii"))
    for a in c:
        if 97 <= a <= 122:
            freq[a - 97] += 1
        if 65 <= a <= 90:
            freq[a - 65] += 1

def findKey():                              # find the index of the max frequency letter
    key = 0
    for i in range(26):
        if freq[key] < freq[i]:
            key = i
    return (key - letter) % 26 

def isNotInt(s):
    l = list(s.encode('ascii'))
    for ch in l:
        if not 48 <= ch <= 57:
            return True
    return False

def usage():
    print("Name:")
    print(f"    {_filename} -- Caesar Cryptography")
    print("Usage:")
    print(f"    python {_filename} [enc [key] | dec [key] | anl [attempt]]")
    print("Description:")
    print("    enc       Encrypt input text with caesar method")
    print("    dec       Dencrypt input text with caesar method")
    print("    anl       Run cryptanalysis on input text ")
    print("    key       Key for Encrypt and Decrypt the input text (0 - 25) (default: 3)")
    print("    attempt   Attempt of cryptanalysis (in case 'e' doesn't work) (0 - 25) (default: 0)")

def analysis():

####################
### MAIN PROGRAM ###
####################
# You do not need to modify anything below
# But (of course) you could/should try to understand it.

# To read arguments given in command lines
# sys.argv is an array (list) of arguments
# ex: typing "python caesar.py enc 3" gives the following
#     sys.argv = ["caesar.py", "enc", "3"]
# We can check the length of sys.argv to detect the commands
_filename = sys.argv[0]
if len(sys.argv) > 1:
    command = sys.argv[1]
else:  # give a default value
    command = "help" 

if len(sys.argv) > 2:
    if isNotInt(sys.argv[2]):
        print(f"{_filename}: illegal option -- {sys.argv[2]}")
        command = 'help'
    else:
        key = int(sys.argv[2])
else:  # give a default value
    key = 3
# Execute the appropriate command
if command == "help":
    usage()

elif command == "dec" or command == "enc":
    # Read the input text, either the plaintext or the ciphertext
    # sys.stdin is the STandarD INput: everything which is typed in the terminal
    # it can be also given using the '<' symbol in command line
    input_text = [ line.rstrip() for line in sys.stdin ]
    
    for line in input_text:
        if command == "dec":
            print( dec(key, line) )
        else:
            print( enc(key, line) )
elif command == 'anl':

else:
    print("{_filename}: unknown command")
    usage()
