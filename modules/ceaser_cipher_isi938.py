def cipher(message, rotation, option):
    
    result = ''
    for char in message:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            ciphered_char = chr((ord(char) - ascii_offset + rotation * option) % 26 + ascii_offset)
            result += ciphered_char
        else:
            result += char
    return result
