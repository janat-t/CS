ALPHABET = range(ord('a'), ord('z')+1)  # Create a "list" containing all char codes
                                        # corresponding to lowercase letters

msg = input("Enter a string: ")         # User can choose a string

for char in msg:
    code = ord(char)
    offset = code - ALPHABET[0]
    if code in ALPHABET:                # Check if the char is a lowercase letter
        print(char, ":", code, "," , offset)
    else:
        print(char, ":", code)
