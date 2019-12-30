# Note that you can change the structure of the function.
# For example, you can change the type of loop.
def enc(k, m):
    """Encode the message m (aka plaintext)
    with Caesar cipher and shift key k.
    Change only lowercase characters,
    Keep other characters.
    Return the ciphertext.
    """
    
    # Convert the message in a list of character codes
    cc_plaintext = list(m.encode("ascii"))
    
    # Duplicate the list, to store character codes of the ciphertex
    cc_ciphertext = cc_plaintext.copy()
    
    for i in range(len(m)):
        if 97 <= cc_ciphertext[i] <= 122:
            cc_ciphertext[i] = 97 + ((cc_ciphertext[i] - 97 + k) % 26)
    c = bytes(cc_ciphertext).decode("ascii")
    return c

# Main program
k = int(input("Key: "))
plaintext = input("Plaintext: ")
ciphertext = enc(k, plaintext)
print(ciphertext)
