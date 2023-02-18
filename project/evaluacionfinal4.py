import pywhatkit

pywhatkit.sendwhatmsg("USUARIO","LA VENTA FUE PROCESADA EXITOSAMENTE ",18,30)

def sendCorreo():
    email = input("Ingrese su email: ")
    exists = False

    if email == exists:
        return "EL CORREO NO EXISTE"

    else:
        return "LA VENTA FUE PROCESADA EXITOSAMENTE"

sendCorreo()
