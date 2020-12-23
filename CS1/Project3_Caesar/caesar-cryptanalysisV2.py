import sys                                  # Needed to access the arguments given in command line
import matplotlib.pyplot as plt

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

# Input from STanDard INput
input_text = [ line.rstrip() for line in sys.stdin ]

# Count frequency of each letter in every line in input_text
for line in input_text:
	countFreq(line)

plt.plot(n, freq)
plt.show()

# Find key for decryption
key = findKey()
print(f"key : {key}")

# Print out decrypted text
for line in input_text:
    print(dec(key, line))