import random

diccionario = {}

def gen_random(k):
    abe = list("abcdefghijklmnopqrstuvwxyz ")
    todas_tuplas_usadas = []
    
    for conta in abe:    
        num_tuplas = random.randint(1, 3)
        valores_letra = []
    
        for i in range(num_tuplas):
            while True:
                nueva_tupla = tuple(random.choices([0, 1], k=k))
                if nueva_tupla not in todas_tuplas_usadas:
                    valores_letra.append(nueva_tupla)
                    todas_tuplas_usadas.append(nueva_tupla)
                    break

        diccionario[conta] = valores_letra
    
    return diccionario


def encriptar(mensaje):
    ans = ""
    for ch in mensaje:
        if ch.isupper():
            ch = ch.lower()
        if ch in dicc_e:
            tupla_elegida = random.choice(dicc_e[ch])
            ans += ''.join(str(x) for x in tupla_elegida)
        else:
            ans += ch

    return ans

def desencriptar():
    ans = ""
    for i in range(0, len(enc), k):
        segmento = enc[i:i+k]
        tupla_segmento = tuple(int(x) for x in segmento)
    
        letra_encontrada = False
        for ch, valores in dicc_e.items():
            if tupla_segmento in valores:
                ans += ch
                letra_encontrada = True
                break

        if not letra_encontrada:
            ans += segmento
        
    return ans



k = 6
dicc_e = gen_random(k)
print(dicc_e)
hola = "baila sin cesar"
enc = encriptar(hola)

print("\nEl mensaje encriptado es:", enc)
des = desencriptar()
print("\nEl mensaje descifrado es:", des, "\n")

