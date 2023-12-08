from string import ascii_uppercase

# Rotores de la máquina Enigma
rotor_I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor_II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

reflector_B = {
    'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q', 'F': 'S', 'G': 'L', 'H': 'D',
    'I': 'P', 'J': 'X', 'K': 'N', 'L': 'G', 'M': 'O', 'N': 'K', 'O': 'M', 'P': 'I',
    'Q': 'E', 'R': 'B', 'S': 'F', 'T': 'Z', 'U': 'C', 'V': 'W', 'W': 'V', 'X': 'J',
    'Y': 'A', 'Z': 'T'
}

def rotor_shift(rotor, shift):
    return rotor[shift:] + rotor[:shift]

def enigma(text, rotor1, rotor2, rotor3, reflector, rotor1_pos, rotor2_pos, rotor3_pos):
    encrypted_text = ""
    for letter in text:
        if letter in ascii_uppercase:
            # Avanzar los rotores
            rotor1 = rotor_shift(rotor1, 1)
            if rotor1_pos % 26 == 0:
                rotor2 = rotor_shift(rotor2, 1)
                if rotor2_pos % 26 == 0:
                    rotor3 = rotor_shift(rotor3, 1)
            
            # Paso a través del rotor 1
            index = (ascii_uppercase.index(letter) + rotor1_pos) % 26
            letter = rotor1[index]

            # Paso a través del rotor 2
            index = (ascii_uppercase.index(letter) + rotor2_pos - rotor1_pos) % 26
            letter = rotor2[index]

            # Paso a través del rotor 3
            index = (ascii_uppercase.index(letter) + rotor3_pos - rotor2_pos) % 26
            letter = rotor3[index]

            # Reflector
            letter = reflector[letter]

            # Paso a través de los rotores en reversa
            index = (rotor3.index(letter) - rotor3_pos + rotor2_pos) % 26
            letter = ascii_uppercase[index]

            index = (rotor2.index(letter) - rotor2_pos + rotor1_pos) % 26
            letter = ascii_uppercase[index]

            index = (rotor1.index(letter) - rotor1_pos) % 26
            letter = ascii_uppercase[index]

            encrypted_text += letter

            rotor1_pos += 1
            rotor2_pos += 1
            rotor3_pos += 1
    return encrypted_text

# Ejemplo de uso:
mensaje = "HELLO MY NAME IS JOSE"
posicion_rotor1 = 0
posicion_rotor2 = 0
posicion_rotor3 = 0

mensaje_cifrado = enigma(mensaje, rotor_I, rotor_II, rotor_III, reflector_B, posicion_rotor1, posicion_rotor2, posicion_rotor3)
print("Mensaje cifrado:", mensaje_cifrado)
