import sys

print(sys.path) #Tiene las rutas de búsqueda de módulos
sys.path.append("F:/borrar")#Se puede modificar la variable path para incluir nuevas rutas

import fernando #Incluye el módulo 'fernando' que se encuentra en 'f:/borrar
fernando.saludar()

sys.path.append("F:/borrar/funciones_comprimidas.zip")#Importar un zip directamente
import funciones#Este módulo está en el zip
funciones.f1()#Función dentro del módulo funciones, dentro del zip



