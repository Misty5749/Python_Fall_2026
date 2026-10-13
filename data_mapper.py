"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION B - EMOJI CIPHER
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. EMOJI_CIPHER constant maps every letter (A-Z) to an emoji.
[ ] 3. Program takes a word or phrase from the user.
[ ] 4. Program loops through characters and prints emojis.
[ ] 5. A 'try/except' block handles spaces or punctuation.
-----------------------------------------------------------------------
"""

EMOJI_CIPHER = {
    "A": "🍎",
    "B": "🍌",
    "C": "🐱",  # ...COMPLETE A-Z
    "D": "🐬",
    "E": "🌟",
    "F": "🦊",
    "G": "🍇",
    "H": "🏠",
    "I": "🍦",
    "J": "🪼",
    "K": "🔑",
    "L": "🦁",
    "M": "🌙",
    "N": "🎵",
    "O": "🐙",
    "P": "🍕",
    "Q": "👑",
    "R": "🌈",
    "S": "🐍",
    "T": "🌮",
    "U": "☂️",
    "V": "🎻",
    "W": "🐳",
    "X": "❌",
    "Y": "🪀",
    "Z": "🦓",
    " ": "💫",
}  # made by AI

message = input("Enter secret message: ").upper()
emoji_message = ""
for character in message:
    try:
        # goes through every line until it matches with the letter and changes the cipher
        print(EMOJI_CIPHER[character], end="")
        # asked AI on how to have print on one line instead of multiple lines
    except KeyError:
        print(character, end="")


# TODO: Loop through each character
# TODO: try to print the emoji, except if it's a space or symbol
