import sys
from collections import defaultdict
LETTER_FREQS = {
    'a': 0.080,
    'b': 0.015,
    'c': 0.030,
    'd': 0.040,
    'e': 0.130,
    'f': 0.020,
    'g': 0.015,
    'h': 0.060,
    'i': 0.065,
    'j': 0.005,
    'k': 0.005,
    'l': 0.035,
    'm': 0.030,
    'n': 0.070,
    'o': 0.080,
    'p': 0.020,
    'q': 0.002,
    'r': 0.065,
    's': 0.060,
    't': 0.090,
    'u': 0.030,
    'v': 0.010,
    'w': 0.015,
    'x': 0.005,
    'y': 0.020,
    'z': 0.002
}

#I wrote this script to calculate the average IC of different periods

def clean_letters(s):
    return "".join(c for c in s.upper() if c.isalpha())

def IC(s):
    letters = clean_letters(s)
    N = len(letters)
    freqs = defaultdict(int)
    for letter in letters:
        freqs[letter] += 1

    return sum(f * (f - 1) for f in freqs.values()) / (N * (N - 1))

def make_columns(s, period):
    columns = ["" for i in range(period)]
    letters = clean_letters(s)
    for i in range(len(letters)):
        columns[i % period] += letters[i]
    
    return columns

def caesar_cipher(s, shift):
    result = ""
    for letter in s:
        if letter.isalpha():
            start = ord('A') if letter.isupper() else ord('a')
            shifted = (ord(letter) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            result += letter.upper()
    return result

def calc_phi(s):
    total_freq = 0
    for letter in s:
        total_freq += LETTER_FREQS[letter.lower()]

    return total_freq

STRING = clean_letters(sys.argv[1])
MAX_PERIOD = int(sys.argv[2])
PERIOD = int(sys.argv[3])

for period in range(1, MAX_PERIOD + 1):
    columns = make_columns(STRING, period)
    total_IC = 0
    for col in columns:
        total_IC += IC(col)
    
    avg_IC = total_IC / period
    print(f"period: {period} - average IC: {avg_IC:.3f}")

#Then using the specified period to do a frequency analysis for each of the alphabets
print()
columns = make_columns(STRING, PERIOD)
best_keys_decoded = []

for i in range(PERIOD):
    ciphers = []
    for j in range(26):
        cipher = caesar_cipher(columns[i], j)
        phi = calc_phi(cipher)
        ciphers.append((phi, cipher, j)) #phi, decoded, key

        #print(f"{cipher} {phi:.3f}")

    print(f"Top 3 column {i} frequencies:")
    ciphers.sort(reverse=True)
    for k in range(3):
        cipher = ciphers[k]
        key_letter = chr(ord('A') + (26 - cipher[2]) % 26)
        print(f"{k + 1} - {cipher[0]:.3f} - {cipher[1]} - key: {key_letter}")

        if k == 0:
            best_keys_decoded.append(cipher[1])

#Finally deciphering using the most likely keys

result = ""

for i in range(len(STRING)):
    result += best_keys_decoded[i % PERIOD][i // PERIOD]

print()
print(f"Final result: {result}")

#Usage: python ./vigenere_cipher.py <encoded_text> <max_periods_to_test> <period_to_test>
#To get the correct answer: set period to test to 5
#Answer: THE VIGENERE CIPHER IS A METHOD OF ENCRYPTING ALPHABETIC TEXT BY USING A SERIES
#OF INTERWOVEN CAESAR CIPHERS BASED ON THE LETTERS OF A KEYWORD IT EMPLOYS A FORM OF 
#POLYALPHABETIC SUBSTITUTION