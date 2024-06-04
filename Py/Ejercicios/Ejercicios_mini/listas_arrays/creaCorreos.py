def crear_correos(nombres, dominios):
    correos = [f"{nombre.lower()}@{dominio}" for nombre in nombres for dominio in dominios]
    return correos

# Ejemplo de uso de la función
nombres = ["juan", "maria", "pedro"]
dominios = ["gmail.com", "yahoo.com", "hotmail.com"]
direcciones_correo = crear_correos(nombres, dominios)
print("Direcciones de correo electrónico creadas:")
for correo in direcciones_correo:
    print(correo)