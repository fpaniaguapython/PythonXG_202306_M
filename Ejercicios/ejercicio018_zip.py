#zip 'normal'
ciudades = ["Vigo","Pontevedra","Santiago de Compostela"]
poblaciones = [300_000, 80_000, 100_000]

info_zip = zip(ciudades, poblaciones)
info_list = list(info_zip)

print(info_list) # [('Vigo', 300000), ('Pontevedra', 80000), ('Santiago de Compostela', 100000)]

#zip con distintos tamaños de lista - usando 3 listas - sin detectar el error
ciudades = ["Vigo","Pontevedra","Santiago de Compostela","A Coruña"]
poblaciones = [300_000, 80_000, 100_000]
provincia = ["Pontevedra","Pontevedra","A Coruña", "A Coruña"]

info_zip = zip(ciudades, poblaciones, provincia)
info_list = list(info_zip)

print(info_list) # [('Vigo', 300000, 'Pontevedra'), ('Pontevedra', 80000, 'Pontevedra'), ('Santiago de Compostela', 100000, 'A Coruña')]

#zip con distintos tamaños de lista - detectando el error mediante le parámetro strict
ciudades = ["Vigo","Pontevedra","Santiago de Compostela","A Coruña"]
poblaciones = [300_000, 80_000, 100_000]

info_zip = zip(ciudades, poblaciones, strict=True)
info_list = list(info_zip)

print(info_list)



