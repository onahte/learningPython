alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    final_text = ""
    if direction == "decode":
        shift = -shift
    for char in text:
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            position += shift
            if position > 26:
                position -= 26
            final_text += alphabet[position]

    print(f"Here's the {direction}d result: {final_text}")

def info():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text, shift=shift, direction=direction)

info()
response = input('Do you want to encode/decode another message?(y/n) ').lower()
while response == 'y':
    info()