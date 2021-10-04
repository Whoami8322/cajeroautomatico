# Cajero Automático

from random import randrange 
saldo = randrange(0,9000000)

print("Welcome al Cajero Automático")
print("")
print("1. Opciones Disponibles")
print("2. Cuenta de Ahorro")
print("3. Cuenta de Debito")
print("4. Pagos de Facturas")
print("5. Enviar Dinero")
print("6. Nequi")
print("7. Tarjeta de Credito")
print("8. Transferencias")
print("0. Exit")

opcion = int(input("Selecciones la Opción: "))
if opcion in range(9):
    if opcion == 0:
        print("Hasta Luego... Feliz Día.")
    
    elif opcion == 1:
        print(f"Su saldo disponible es:  {saldo}")
    
    elif opcion == 2:
        print("Cuenta de Ahorro.")                
        monto = int(input("Ingrese el monto a retirar: "))
        if monto > saldo:
            print("Saldo insuficiente para hacer su retiro.")
            print("Hasta luego, puede retirar su tarjeta...")
        else:
            saldo = saldo - monto
            pesos = "pesos"
            print("Retiro Exitoso")
            print(f"Su saldo actual es:  ${saldo} pesos")

    elif opcion == 3:
        print("Cuenta de Debito.")
        monto = int(input("Ingrese el monto a retirar: "))
        if monto > saldo:
            print("Saldo insuficiente para hacer su retiro.")
            print("Hasta luego, puede retirar su tarjeta...")
        else:
            saldo = saldo - monto
            print("Retiro Exitoso")
            print(f"Su saldo actual es:  {saldo}")

    elif opcion == 4:
        print("Pagos de Facturas.")
        monto = int(input("Ingrese el monto a retirar: "))
        if monto > saldo:
            print("Saldo insuficiente para hacer su retiro.")
            print("Hasta luego, puede retirar su tarjeta...")
        else:
            saldo = saldo - monto
            print("Pago de Facturas Exitoso")
            print(f"Su saldo actual es:  {saldo}")

    elif opcion == 5:
        print("Enviar Dinero.")
        monto = int(input("Ingrese el monto a enviar: "))
        saldo = saldo + monto
        print(f"Monto a Enviar: {monto}")
        print(f"Su saldo es: {saldo}")

    elif opcion == 6:
        print("Cuenta de Nequi.")
        cuenta_Nequi = int(input("Ingrese los 10 digitos de su Celular. "))
        codigo = int(input("Ingrese su codigo de 6 digitos. "))
        monto = int(input("Ingrese el monto a retirar: "))
        if monto > saldo:
            print("Saldo insuficiente para hacer su retiro.")
            print("Hasta luego, puede retirar su tarjeta...")
        else:
            saldo = saldo - monto
            print("Retiro Exitoso")
            print(f"Su saldo actual es:  {saldo}")

    elif opcion == 7:
        print("Avance de tu tarjeta de credito.")
        contraseña = int(input("Ingrese su contrase: "))
        monto = int(input("Ingrese el monto a retirar: "))
        if monto > saldo:
            print("Saldo insuficiente para hacer su avance.")
            print("Hasta luego, puede retirar su tarjeta...")
        else:
            saldo = saldo - monto
            print("Su Avance fue Exitoso")
            print(f"Su saldo actual es:  {saldo}")

    elif opcion == 8:
        print("Trnasferencias.")
        cuenta = int(input("Ingrese el Nro. de cuenta a transferir. "))
        monto = int(input("Ingrese el monto a retirar: "))
        if monto > saldo:
            print("Saldo insuficiente para transferir.")
            print("Hasta luego, puede retirar su tarjeta...")
        else:
            saldo = saldo - monto
            pesos = "pesos"
            print("Transferencia Exitoso")
            print(f"Su saldo actual es:  ${saldo} pesos")