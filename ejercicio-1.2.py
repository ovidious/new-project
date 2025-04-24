# A.
# Pedirle al usuario que ingrese cualquier texto real:
# 1. Caluclar cuanto tardaria en decir esa frase
# 2. Calcular cuandtas palabras dijo
 
# B.
# Si tarda mas de 1 minuto: 
# 1. Decirle: "Para flaco tampoco te pedi un testamento" 

# C.
# Si una persona habla un 30% mas rapido:
# 1. Cuanto tardaria en decir esa frase

clear = lambda: print('\n' * 5)
clear() # Limpia la consola 
persona_promedio_seg_palabra = 1 / 2 
frase = input('Diga cualquier texto real: ')
palabras = frase.split(' ')
cantidad_palabras = len(palabras)
print(f'Cantidad de palabras que tiene el texto: {cantidad_palabras}')
print(f'Tiempo que tardaria en decir esa frase: {cantidad_palabras * persona_promedio_seg_palabra} segundos')
if cantidad_palabras * persona_promedio_seg_palabra > 60:
    print('Para flaco tampoco te pedi un testamento')
print(f'Tiempo que tardaria en decir esa frase si hablara un 30% mas rapido: {cantidad_palabras * persona_promedio_seg_palabra * 0.7} segundos')    



