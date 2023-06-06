#split --> Parte una cadena en tokens
texto = 'Ucrania se trasladó hoy al 18 de agosto de 1941. Ese día, las tropas soviéticas que se retiraban de la ciudad de Zaporiyia ante el avance de las tropas nazis volaron la presa de esa ciudad sureña. "Hemos volado la presa del (río) Dnipro para no permitir que este primer hijo (la presa) de nuestro plan quinquenal cayera en manos de los bandidos de Hitler", afirmaron los soviéticos en aquel entonces.'
lista_palabras = texto.replace('.','').replace(',','').replace('(','').replace(')','').split()
print(lista_palabras)

texto = '2023#06#06#13#15'
componentes = texto.split('#')
print(componentes)#['2023', '06', '06', '13', '15']

#join
nuevo_texto = ":".join(componentes) #2023:06:06:13:15
print(nuevo_texto)

nuevo_texto = "RAMÓN".join(componentes) #2023RAMÓN06RAMÓN06RAMÓN13RAMÓN15
print(nuevo_texto)


#HTML
#Utilizando lo que sea necesario, la lista de aplicaciones móviles de la XUNTA
#Aplicacións móbiles
html = '''
<div class="repText eq" style="height: 60px;"><span class="titulo">DOG</span></div>
<div class="repText eq" style="height: 60px;"><span class="titulo">Tradutor Gaio</span></div>
<div class="repText eq" style="height: 60px;"><span class="titulo">Mobem</span></div>
<div class="repText eq" style="height: 60px;"><span class="titulo">MeteoGalicia</span></div>
'''
prefijo = '<div class="repText eq" style="height: 60px;"><span class="titulo">'
sufijo = '</span></div>'
html_modificado = html.replace(prefijo,'*').replace(sufijo,'').replace('\n','')
lista_apps = html_modificado[1:].split('*')
print(lista_apps)