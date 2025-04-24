# A. 
# Diferencia en porcentaje entre el curso actual y
# 1. El mas rapido de otros cursos
# 2. El mas lento de otros cursos
# 3. El promedio de otros cursos

curso_actual = 90
curso_minimo = 150
curso_maximo = 420
curso_promedio = 240

clear = lambda: print('\n' * 5)
clear() # Limpia la consola
 
# 1. El mas rapido de otros cursos
diff_porcentaje = 100 - curso_actual / curso_minimo * 100
print(f'Diferencia en porcentaje entre el curso actual y el mas rapido de otros cursos: {diff_porcentaje}%')

# 2. El mas lento de otros cursos
diff_porcentaje = 100 - curso_actual * 1000 // curso_maximo / 10
print(f'Diferencia en porcentaje entre el curso actual y el mas lento de otros cursos: {diff_porcentaje}%')

# 3. El promedio de otros cursos
diff_porcentaje = 100 - curso_actual / curso_promedio * 100
print(f'Diferencia en porcentaje entre el curso actual y el mas lento de otros cursos: {diff_porcentaje}%')

# B.
# Porcentaje de material inservible que se reduce en: 
# 1. El promedio de los curso
# 2. El curso actua (este curso)
crudo_curso_actual = 210
crudo_cursos = 300

# 1. El promedio de los curso
material_inservible = 100 - crudo_curso_actual / crudo_cursos * 100
print(f'Porcentaje de material inservible que se reduce en el promedio de los cursos: {material_inservible}%')

# 2. El curso actua (este curso)
material_inservible = 100 - crudo_curso_actual / crudo_cursos * 100
print(f'Porcentaje de material inservible que se reduce en el curso actual: {material_inservible}%')

# C.
# Ver 10 hiras de este curso a cuantas horas de otro curso equivale
cantidad_horas_curso = 600
cantidad_horas_otro_curso = 240
cantidad_horas =  cantidad_horas_otro_curso * 100 / cantidad_horas_curso / 10
print(f'Ver 10 horas de este curso a cuantas horas de otro curso equivale: {cantidad_horas}')

