def iniciar():
    msj_bienvenida= """ 
            "Bienvenido" 
    Este es un taller de carros, puedes: 
    agregar o borrar carros de la lista
    """
    msj_lista= """ Esta es la lista de carros que hay:
    """
    msj_opc="""Estas son las opciones que hay:
    1- Agregar
    2- Borrar
    3- salir
    :"""
    msj_1= """ Elegiste la opcion 1 (agregar)
    ingresa el nombre de carro que deses agregar:  """

    msj_2=""" Elegiste la opcion 2 (borrar). Ingresa "volver" para regresar
    Ingresa el nombre del  
    carro que deses borrar:  """

    msj_3= """ 
            "Saliste del programa"
    """
    msj_error= """
    Error. Ingrese una opcion valida
    """
    msj_error2="""
    Error. Ingresa correctamente el nombre de carro que quieras eliminar
    """
    msj_errorr="""Error ingresa una opcion valida (numeros)"""

    carros = ["Chevy","Supra MK4","Mustang GT","Camaro"]
    print(msj_bienvenida)
    print (msj_lista,carros)
    while True:
        opc = input(msj_opc).strip()
        if opc == "1":
            agregar = input(msj_1).strip()
            carros.append(agregar)
            print(carros)
            continue
        elif opc == "2":
            while True:
                borrar = input(msj_2).strip()
                if borrar in carros:
                    carros.remove(borrar)
                    print(carros)
                    break
                elif borrar == "Volver":
                    break
                else:
                    print(msj_error2)
                    continue
        elif opc == "3":
            print(msj_3)
            break
        else: 
            print(msj_error)
