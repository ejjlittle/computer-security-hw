import sys

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

#I wrote this simple script to calculate phi's of the 1-grams and pick the maximum one.

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

max_phi = 0
max_cipher = None
max_key = 0

for i in range(26):
    cipher = caesar_cipher(sys.argv[1], i)
    phi = calc_phi(cipher)
    if phi > max_phi:
        max_phi = phi
        max_cipher = cipher
        max_key = i

    print(f"{cipher} {phi:.3f}")

print()
print(f"Maximum likelihood: {max_phi:.3f} - {max_cipher} - key: {max_key}")

#Usage: python ./caesaer_cipher <encoded>
#Answer: COMPUTERSCIENCE, key = 19
