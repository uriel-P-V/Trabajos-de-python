#  Practica-04 - Uso de la iteración - while;
print("Perez Valdovinos Uriel ALejandro");
print("Perez Tovar Santiago");
print("Perez Ruelas Jesus Isaias");
print("practica numero 4");
print("TEMA Uso de la iteración - while");
print("seccion d01");
print("equipo numero 1");
"""
Profesor en este programa esta hecho para que de cierta manera no se rompa tan facilmente (claro a excepcion de usar palabras ahi puede que salte un error)
asi que ponga tanto 0 como numeros negativos y podra darse cuenta de si la solucion de escape fue la mas optima o por lo contrario pueda ayudarnos a buscar
otro metodo para hacer estos problemas en caso de que se inclumpla lo solicitado. Disculpe si ve cosas avanzadas, pero uno de los integrantes
aplica un poco de la logica de otros lenguajes para ser mas claros el uso de imports y las listas que en otro lenguaje se llaman Array's
esperemos que esto no sea un inconveniente pues el programa corre y utilizamos los while. Esperamos que este teniendo un agradable dia. ATTE. Equipo 1.
"""

def menuprincipal():
    menu=int(input("menu: \n 1.promediador de calificaciones y cual sera la mayor de estas \n 2.sacador de pares y impares \n 3.calculadora de area de una esfera \n 0.salir \n. "))
    m=0 #bandera de while
    while m == 0:
        
        if (menu==1):
            print("Promediador de calificaciones y ademas mostrar la calificacion mas alta");
            def e1():
                a=0 #bandera de while
                while (a == 0):
                    cali=[]; #calificacion lista
                    CanC=str(input("cuantas calificaciones vas a registrar? si ya no quieres seguir escribe NO ")); #Numero de calificaciones
                    mayor = 0
                    menor = 0
                    i = 1
                    if (CanC=="No" or CanC=="NO" or CanC=="no" or CanC=="nO"):
                        print("Gracias por usar este programa");
                        break;
                    else: CanC=float(CanC);
                    if(CanC <= 0):
                        print("por favor vuelva a seleccionar esta opcion y ahora solo ponga numeros mayores a 0");
                        break;
                    else:
                        while(CanC > 0):
                            num=float(input("Ingresa la #"+ str(i) + " calificacion: "));
                            cali.append(num);
                            i=i+1
                            CanC = CanC - 1;
                        
                    mayor=max(cali);
                    promedio=sum(cali)/float(len(cali));
                    print("aqui estan todas las calificaciones: ", cali);
                    print("aqui esta el promedio: ", promedio);
                    print("aqui esta la calificacion mayor: ", mayor);
            
                     
            e1();

            menu=int(input("menu: \n 1.promediador de calificaciones y cual sera la mayor de estas \n 2.sacador de pares y impares \n 3.calculadora de area de una esfera \n 0.salir \n. "));
            
        elif (menu == 2):
            print("separador de numeros pares y impares")
            def e2():
                a=0 #bandera de while
                while (a == 0):

                    num=str(input("ingresa un numero o si quieres parar el programa ponga la palabra NO "));
                    if(num=="No" or num=="NO" or num=="no" or (num=="nO")):
                        print("Gracias por usar este programa");
                        break;
                    else: num=int(num);
                    if(num==0):
                        print("El numero 0 no es par ni impar")
                    elif (num < 0 and num%2==1):
                        print("los numeros negativos no estan especificados como par o impar pero...");
                        print("el numero negativo", num, "es impar");
                    elif (num < 0 and num%2==0):
                        print("los numeros negativos no estan especificados como par o impar pero...");
                        print("el numero negativo", num, "es impar");
                    elif(num%2==1):
                        print("el numero", num, "es impar");
                    elif(num%2==0):
                        print("el numero", num, "es par");
            e2();
            menu=int(input("menu: \n 1.promediador de calificaciones y cual sera la mayor de estas \n 2.sacador de pares y impares \n 3.calculadora de area de una esfera \n 0.salir \n. "))
        elif (menu == 3):
            print(" estas en la opcion--->calculadora del area para una esfera,mi rey:");
            def e3():
                r=0 #bandera de while
                while (r<=0):
                    radio=str(input("¿dime en centimetros cuanto mide el radio de tu esfera mi rey? o esbribe la palabra NO si quieres parar "));
                    if(radio=="No" or radio=="NO" or radio=="no" or radio=="nO"):
                        print("Gracias por usar este programa");
                        break;
                    else: radio=float(radio);
                    if (radio<=0):
                        print("El radio de un circulo no puede ser 0, o menor a 0, vuelva e ingrese una cantidad valida mi rey");
                        break;
                    else:
                        R3= 4*3.1416*(radio*radio);
                    print("el radio de una esfera de:",radio,"cm es",R3,"cm");
                    
            e3();
            menu=int(input("menu: \n 1.promediador de calificaciones y cual sera la mayor de estas \n 2.sacador de pares y impares \n 3.calculadora de area de una esfera \n 0.salir \n. "));
        elif (menu == 0):
            print("Gracias por usar el programa");
            break;
            

menuprincipal();


                