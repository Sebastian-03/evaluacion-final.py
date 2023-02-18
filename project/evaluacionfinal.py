import controller as ctr

message="""
    1)Insertar un usuario
    2)ver lista de usuarios
    3)buscar usuario
    4)Lista de productos
"""
global option
option=input('ingrese una opcion: ')

def registerUser():
    usuario=input('ingrese el siguiente data usuario: ')
    password=input('ingrese el siguiente data password: ')
    email=input('ingrese el siguiente data email: ')
    fullname=input('ingrese el siguiente data fullname: ')
    tipousuario=input('ingrese el siguiente data tipousuario: ')
    data=(usuario,password,email,fullname,tipousuario)
    try:
        ctr.insertUser(data)
    except Exception as e:
         print("error al ingresar data")
         print(e)
def listUser():
    data=ctr.controllerUser()
    for row in data:
        print(row)



def regProduct():
    orderid=input('ingrese el ORDER_ID: ')
    pricetotal=input('ingrese el  PRICE_TOTAL: ')
    productid=input('ingrese el PRODUCT_ID: ')
    name=input('ingrese el NAME : ')
    nroserie=input('ingrese el NROSERIE: ')
    cantidad=input('ingrese la CANTIDAD: ')
    product=input('ingrese el PRODUCT: ')
    priceunit=input('ingrese el PRICE_UNIT')
    categoria=input('ingrese la CATEGORIA: ')
    stockactual=input('ingrese el STOCK_ACTUAL: ')
    date=input("INGRESE LA FECHA: ")
    useradmin=("INGRESE EL USER_ADMIN")
    userclient="(INGRESE EL USER_CLIENT)"
    data=(orderid,pricetotal,productid,name,nroserie,cantidad,product,priceunit,categoria,stockactual,date,useradmin,userclient)
    try:
        ctr.insertProduct(data)
    except Exception as e:
         print("error al ingresar data")
         print(e)

def showListP():
    print("LA LISTA ES: ")
    data=ctr.controllerProduct()
    for row in data:
        print(row)


if __name__=='__main__':
 if option=='1':
    registerUser()
 elif option=='2':
    listUser()
 elif option=='3':
    regProduct()
 elif option=='4':
    showListP()
 else:
    print("error")