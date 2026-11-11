""" 
Modulo de gestion de estudiantes
"""
estudiantes = { }

def estudiante_existe(student_id):
    #Verifica si un estudiante existe en el diccionario de estudiantes
    return student_id in estudiantes 

def registrar_estudiante(student_id, nombre, edad):
    #Registra un nuevo estudiante en el diccionario de estudiantes
    if estudiante_existe(student_id):
        return False, f"El estudiante con ID {student_id} ya existe."

    estudiantes[student_id] = {
        "nombre": nombre,
        "edad": edad,
        "calificaciones": []
    }
    return True, f"Estudiante {nombre} registrado con exito."

def actualizar_estudiante(student_id, nombre=None, edad=None):
    #Actualiza la informacion de un estudiante existente
    if not estudiante_existe(student_id):
        return False, f"El estudiande con ID {student_id} no existe."

    if nombre:
        estudiantes[student_id]["nombre"] = nombre
    if edad:
        estudiantes[student_id]["edad"] = edad

    return True, f"Informacion del estudiante con ID {student_id} actualizada con exito."

def eliminar_estudiante(student_id):
    #Elmina un estudiante del diccionario de estudiantes
    if not estudiante_existe(student_id):
        return False, f"El estudiante con ID {student_id} no existe."

    nombre = estudiantes[student_id]["nombre"]
    del estudiantes[student_id]
    return True, f"Estudiante {nombre} eliminado con exito."

def buscar_estudiantes(criterio):
    #Busca estudiantes por id o por nombre

    criterio = criterio.lower().strip()
    resultado = []

    for s_id, datos in estudiantes.items():
        if criterio == s_id.lower() or criterio == datos["nombre"].lower():
            resultado.append((s_id, datos))

    return resultado

def registrar_calificaciones(student_id, lista_notas):
    if not estudiante_existe(student_id):
        return False, f"Estudiante con ID {student_id} no existe"

    estudiantes[student_id]["calificaciones"].extend(lista_notas)
    return True, f"{len(lista_notas)} calificaion(es) agrega(s) correctamente."

def calcular_promedio_y_estado(calificaciones, nota_aprobacion=10.5):
    #calcular  el prmoedio de una lista de notas y determinar si esta o no aprobado
    if not calificaciones:
        return 0.0, "Sin calificaciones"

    promedio = sum(calificaciones) / len(calificaciones)
    estado = "Aprobado" if promedio >= nota_aprobacion else "Desaprobado"
    return promedio, estado

def obtener_reporte_general():
    #genera un resumen general
    reporte = []

    for s_id, datos in estudiantes.items():
        promedio, estado = calcular_promedio_y_estado(datos["calificaciones"])
        reporte.append({
            "id": s_id,
            "nombre": datos["nombre"],
            "edad": datos["edad"],
            "notas": datos["calificaciones"],
            "promedio": promedio,
            "estado": estado
        })

    return reporte