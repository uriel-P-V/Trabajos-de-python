def menu():
    #Profesor el menu no tiene un boton para regresar al menu y es por que el documento de google drive no lo especifica, y siempre que hacemos cosas que no vienen en el pdf sentimos que nos baja puntos
    #asi que ahora si nomas nos apegamos al documento y que fuera funcional sobre todo sin agregar extenciones de cierre, comodides al usuario o otros detalles. Cualquier cosa haganoslo saber en la sesion.
    print("\nHecho por: \nPEREZ VALDOVINOS URIEL ALEJANDRO \nPEREZ TOVAR SANTIAGO \nPEREZ RUELAS JESUS ISAIAS")
    print("-----------------")
    print("practica numero 5");
    print("-----------------")
    print("TEMA Uso de la iteración - for");
    print("-----------------")
    print("seccion d01");
    print("-----------------")
    print("equipo numero 1");
    print("-----------------")
    Opciones=int(input("\n1.Convertidor de numeros a positivos \n2.Peras y Manzanas en un canasto \n3.La tienda de Don Nacho \n4. N personas cuantos a dias ha vivido? \n5.Cerrar programa \n"))
    for i in range (Opciones):
        if (i==0 and Opciones==1):
            """profe al decir la indicacion de que ponga 0
            para salir primero tiene que ingresar un numero mayor a 0
            y despues podra poner 0 para salir."""
            def p1():
                n=int(input("¿cuantos numeros vas a meter mi rey?, y usa el 0 para salir del programa mi rey :"));
                if (n>0):
                    for i in range(n):
                        dato=float(input("Ingresa tu numero mi rey: " "o presiona 0 para salir"));
                        if (dato==0)or (n==0):
                            break
                        elif (dato>0):
                            res=dato
                            print("tu numero ya era positivo mi rey: ", res);
                        elif (dato<0):
                            res2=dato*-1
                            print("aqui tienes tu numero en positivo mi rey: ",res2);
                        elif (dato==0):
                            print("gracias por usar el programa mi rey :)")
                        else:
                            print("escribe un valor valido mi rey")
            p1();
            
        elif (i==1 and Opciones==2):
            def e1():
                compra=[]
                compra2=[]
                while True:
                    opcion=int(input("\n1.ingresar peras \n2.ingresar manzanas \n3.mostrar canastas \n4.finalizar programa \n"))
                    p=0
                    p=opcion
                    if p==1:
                        producto=input("\n#solo necesitas escribir (1 pera)\n")
                        if producto in compra:
                                print()
                        else:
                            compra.append(producto) 
                    if p==2:
                        producto1=input("\n#solo necesitas escribir (1 manzana)\n")
                        if producto1 in compra2:
                            print()
                        else:
                            compra2.append(producto1)
                    elif p== 3:    
                        print("canasta 1")
                        for e in compra:
                            print(e) 
                        print("canasta 2")
                        for e in compra2:
                            print(e)
                    elif p==4:
                        print("hasta luego")
                        break
                    elif (p>4 or p<1):
                        print("opcion incorreta");
            e1();
            
        elif (i==2 and Opciones==3):
            def ee():
                venta=[]
                precios=[]
                while True:
                    co=int(input("que vas a querer hacer \n1.ingresar productos vendidos \n2.mostrar la lista de los productos \n3.mostrar las ganancias del dia \n4.cerrar el programa \n"))
                    p=0
                    p=co
                    if p==1:
                        cont=int(input("cuantos productos vas capturar --->"));
                        num=0;
                        i=1
                        while num<cont:
                            g=input("ingresa el #"+str(i)+ "producto vendido---->")
                            h=float(input("ingresa su valor------>"))
                            num=num+1
                            i=i+1
                            if g in venta:
                                    print()
                            else:
                                venta.append(g)
                            if h in precios:
                                    print()
                            else:
                                precios.append(h)
                    if p==2:
                        print("lista de los productos");
                        for e in venta:
                            print("-",e)
                            print("-----------------")
                    if p==3: 
                        suma=0
                        for i in precios:
                            suma=suma+i
                        print("total de los productos vendidos",suma,"$")
                        print("-----------------");
                    if p==4:
                        print("hasta luego");
                        break
                    if p<1 or p>4:  
                        print("opcion incorreta")
                        print("-----------------")
            ee();
        elif (i==3 and Opciones==4):
            def p4():
                import math
                np=int(input("¿de cuantas personas vas a sacar su numero de dias de vida mi rey?  o usa 0 para salir "));
                if(np==0):
                    print("Gracias por usar el programa");
                elif(np>0):
                    for i in range(np):
                            edad=int(input("ingresa la edad de una persona mi rey:"))
                            if (edad==0):
                                break
                            elif (edad>0):
                                dias=365.256363*edad                 
                                diasredondeados=math.floor(dias)
                                print("estos dias tiene esa persona en este planeta", diasredondeados);
                                """la duracion real de un año son (365 días 5 horas 48 minutos con 45.10 segundos) pero como se considera que esto seria confuso para las personas simplemente
                                se quitan las hora extra de cada año y se compensan con un dia extra cada cuatro, pero con este sistema parece que sobran 45 minutos, por lo que los
                                años que terminan en 00 y son multiplos de 400 no son considerados años biciestos, de igual manera la funcion math.floor siempre redondeara el numero de dias hacia abajo por dos razones logicas
                                los años biciestos son utilizados por que nadie cuenta los dias con decimales, y punto numero dos, el problema pide contar solamente dias por lo que una persona que ha vivido
                                809 dias 23 horas 59 minutos con 59 segundos esta persona solo ha vivido en realidad 809 dias apegandonos a la estricta definicion de dia

                                PD: se podria hacer mas exacto pidiendo tu fecha de nacimiento y en base a eso poder ver cuantos años biciestos a vivido
                                pero como en la hoja de ejercicios especifica que nomas pedir la edad usamos esta formula"""
                            else:
                                print("ingresa un valor valido")
                    print("Gracias por usar el programa si quiere repetir el progreso reinicie el programa :D");

            p4();
        elif (i==4 and Opciones==5):
            print("Muchas gracias por haber usado nuestro programa :D")     
menu();
