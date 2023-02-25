
print("Agregar Contacto")
nombreCompleto = input("Ingrese el nombre completo: ")
cedulaContacto = input("Ingrese el numero de cedula: ")

with open("text.txt", "write") as file:
    file.write("I am learning Python!\n")
    file.write("I am really enjoying it!\n")
    file.write("And I want to add more lines to say how much I like it")
