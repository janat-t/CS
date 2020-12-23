code_a = ord('a')                       # compute the char code of 'a' (=97)
nb_letters = 26

msg = input("Enter a string: ")         # User can choose a string
cc = list(msg.encode("ascii"))          # cc means Character Codes here

for i in range(len(msg)):               # Iterate for the length of the msg
    char = msg[i]                       # Get the i-th character from msg
    code = cc[i]                        # Get the i-th char code
    offset = code - code_a
    if 0 <= offset < nb_letters:        # Check if the char is a lowercase letter
        print(f"{char} : {code} , {offset}")
    else:
        print(f"{char} : {code}")
