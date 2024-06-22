import csv
def obtener_fichero_calificaciones():
    lista = []
    with open(r"C:\Users\sebastian\Downloads\calificaciones.csv", "r", newline="") as archivo:
        lector_csv = csv.reader(archivo, delimiter=";")
        pos = 0
        for linea in lector_csv:
            if pos != 0:
                for i in range(2,len(linea)):
                    if linea[i] == '':
                        linea[i] = '0,0'
                
                Apellidos = linea[0]
                nombre    = linea[1]
                Asistencia = float(linea[2].replace('%',''))
                Parcial1 = float(linea[3].replace(',','.'))
                Parcial2 = float(linea[4].replace(',','.'))
                Ordinario1 = float(linea[5].replace(',','.'))
                Ordinario2 = float(linea[6].replace(',','.'))
                Practicas = float(linea[7].replace(',','.'))
                OrdinarioPracticas = float(linea[8].replace(',','.'))
                lista.append({
                                 'Apellidos':Apellidos,
                                 'nombre':nombre,
                                 'Asistencia': Asistencia,
                                 'Parcial1': Parcial1,
                                 'Parcial2': Parcial2,
                                 'Ordinario1': Ordinario1,
                                 'Ordinario2': Ordinario2,
                                 'Practicas': Practicas,
                                 'OrdinarioPracticas': OrdinarioPracticas,
                            })    
            else:
                pos = 1
    return lista

def añadir_nota_final(calificaciones):
        lista = []
        for alumno in calificaciones:

            if alumno['Ordinario1'] > 0: #Si el alumno se ha presentado al examen de repesca del primer parcial tomamos esa nota como la nota del primer parcial
               parcial1 = alumno['Ordinario1']
            else:
                parcial1 = alumno['Parcial1']
            if alumno['Ordinario2'] > 0: #Si el alumno se ha presentado al examen de repesca del segundo parcial tomamos esa nota como la nota del segundo parcial
               parcial2 = alumno['Ordinario2']
            else:
                parcial2 = alumno['Parcial2']
            
            if alumno['OrdinarioPracticas'] > 0: #Si el alumno se ha presentado al examen de repesca de prácticas tomamos esa nota como la nota de prácticas
               practicas = alumno['OrdinarioPracticas']
            else:
                practicas = alumno['Practicas']

            alumno_Final1 = parcial1
            alumno_Final2 = parcial2
            alumno_FinalPracticas = practicas
            alumno_NotaFinal = parcial1 * 0.3 + parcial2 * 0.3 + practicas * 0.4
            alumno_Apellidos = alumno['Apellidos']
            alumno_nombre = alumno['nombre']
            alumno_asistencia = alumno['Asistencia']
            lista.append({
                   'Apellidos':alumno_Apellidos,
                   'nombre':alumno_nombre,
                   'Asistencia': alumno_asistencia,
                   'Parcial1': alumno_Final1,
                   'Parcial2': alumno_Final2,
                   'Practicas': alumno_FinalPracticas,
                   'NotaFinal': alumno_NotaFinal,
                })    
        return lista

def aprobar_curso(calificaciones):
        lista_ap = []
        lista_rp = []
        for alumno in calificaciones:
            aprobado = False
            if alumno['Asistencia'] >= 75 and alumno['Parcial1'] >= 4 and alumno['Parcial2'] >= 4 and alumno['Practicas'] >= 4 and alumno['NotaFinal'] >= 5:
               aprobado = True

            if aprobado:
                lista_ap.append(alumno)
            else: 
                lista_rp.append(alumno)

        return lista_ap, lista_rp

def imprimir_alumnos_aprobados(calificaciones):
    with open(r"C:\Users\sebastian\Downloads\alumnos_aprobados.csv", "w", newline="") as archivo:
        escritor_csv = csv.writer(archivo, delimiter=";")
        escritor_csv.writerow([' Apellidos', 'nombre', 'Asistencia','Parcial1','Parcial2','Practicas','Nota Final'])
        for alumno in calificaciones:
            lista_imp = [] 
            lista_imp.append(alumno['Apellidos'])
            lista_imp.append(alumno['nombre'])
            lista_imp.append(alumno['Asistencia'])
            lista_imp.append(alumno['Parcial1'])
            lista_imp.append(alumno['Parcial2'])
            lista_imp.append( alumno['Practicas'])
            lista_imp.append(alumno['NotaFinal'])
            escritor_csv.writerow(lista_imp)
        
    return 



lista_alumnos = obtener_fichero_calificaciones()
lista_final_alumnos =  añadir_nota_final(lista_alumnos)
alumnos_aprobados, alumnos_reprobados = aprobar_curso(lista_final_alumnos)
imprimir_alumnos_aprobados(alumnos_aprobados)