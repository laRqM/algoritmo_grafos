import random # Se utiliza para elegir de forma aleatoria el nodo que tenga el mismo número de vecinos

def obtener_nodo(grafo): # Definimos la función 
    numero_maximo_nodos_vecinos_encontrados = -1 # Contador. Lleva la cuenta del número máximo de vecinos encontrados
    numero_maximo_nodos_vecinos = [] # Lista vacía. Aquí vamos a guardar el número máximo de vecinos.

    for nodo, vecinos in grafo.items(): # Iteramos cada nodo en "grafo". Cada iteración se guarda en "nodo" y la lista de vecinos en "vecinos"
        numero_vecinos = len(vecinos) # Obtenemos el número de vecinos del nodo y lo guardamos en "numero_vecinos"
        if numero_vecinos > numero_maximo_nodos_vecinos_encontrados: # Si el número de vecinos es mayor que el máximo de nodos vecinos encontrados...
            numero_maximo_nodos_vecinos_encontrados = numero_vecinos # Actualizamos el valor en numero_maximo_nodos_vecinos_encontrados
            numero_maximo_nodos_vecinos = [nodo] # Entonces reiniciamos la lista con el nodo actual en la iteraciòn
        elif numero_vecinos == numero_maximo_nodos_vecinos_encontrados: # Si el numero de vecinos es igual al numero maximo de nodos vecinos encontrados hasta el momento...
            numero_maximo_nodos_vecinos.append(nodo) # Agregamos el nodo actual a la lista

    nodo_random = random.choice(numero_maximo_nodos_vecinos) # Utilizamos random.choice para elegir de forma aleatoria la lista de numero máximo de nodos vecinos.
    return nodo_random # Retornamos nodo_elegido

grafo = { # Diccionario. Este es nuestro grafo
    1: [2, 3],
    2: [],
    3: [4, 5, 6],
    4: [],
    5: [],
    6: []
}

nodo_max_vecinos = obtener_nodo(grafo) # Creamos la variable nodo_max_vecinos que será igual a la llamada de la función obtener_nodo, a la cual le pasamos el grafo. 
print("EL nodo con mayor número de vecinos es:", nodo_max_vecinos) # Imprimimos el resultado