def descifrar(mensaje_cifrado):
    
    # Lista de todas las posibles combinaciones de rotores y cableado
    rotores = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "BCDEFGHIJKLMNOPQRSTUVWXYZA", "CDEFGHIJKLMNOPQRSTUVWXYZAB"]
    cableado = [(a, b) for a in range(26) for b in range(26)]

    # Lista de todas las posibles posiciones de los rotores
    posiciones = [(a, b, c) for a in range(26) for b in range(26) for c in range(26)]

    # Bucle sobre todas las posibles combinaciones de rotores, cableado y posiciones
    for rotor1 in rotores:
        for rotor2 in rotores:
        for rotor3 in rotores:
            for posicion1 in posiciones:
            for posicion2 in posiciones:
                for posicion3 in posiciones:

                # Descifrar el mensaje cifrado
                mensaje_descifrado = ""
                for letra in mensaje_cifrado:
                    letra_cifrada = letra
                    for i in range(3):
                    letra_cifrada = rotores[i][letra_cifrada]
                    letra_cifrada = cableado[posicion1[i]][letra_cifrada]
                    letra_cifrada = rotores[i + 1][letra_cifrada]
                    letra_cifrada = cableado[posicion2[i]][letra_cifrada]
                    letra_cifrada = rotores[i + 2][letra_cifrada]
                    letra_cifrada = cableado[posicion3[i]][letra_cifrada]
                    mensaje_descifrado += letra_cifrada

                # Comprobar si las dos últimas palabras son "heil hitler"
                if mensaje_descifrado[-8:] == "heil hitler":
                    return mensaje_descifrado

    # Si no se ha encontrado ninguna coincidencia, devolver None
    return None


mensaje_cifrado = "qwertyuioasdfghjklzxcvbnm heil hitler"
mensaje_descifrado = descifrar(mensaje_cifrado)

print(mensaje_descifrado)