from colorama import init
from colorama import Fore
from colorama import Cursor
def e():
    from colorama import Cursor, init, Fore;
    import msvcrt;
    import os;
    init();
def añoymes(año,mes):
    init();
    naño=año;
    nmes=mes;
    if (año>0) and (mes>=0):
        if mes==1:
            print("favor de presionar enter para seguir o ingresa cualquier cosa")
            print(Fore.RESET+"----------------------------------")
            print(Fore.RESET+"|",Fore.BLUE+"Enero",naño,Fore.RESET+"                    |")
        elif mes==2:
            print("favor de presionar enter para seguir o ingresa cualquier cosa")
            print(Fore.RESET+"----------------------------------")
            print(Fore.RESET+"|",Fore.BLUE+"Febrero",naño,Fore.RESET+"                  |")
        elif mes==3:
            print("favor de presionar enter para seguir o ingresa cualquier cosa")
            print(Fore.RESET+"----------------------------------")
            print(Fore.RESET+"|",Fore.BLUE+"Marzo",naño,Fore.RESET+"                    |")
        elif mes==4:
            print("favor de presionar enter para seguir o ingresa cualquier cosa")
            print(Fore.RESET+"----------------------------------")
            print(Fore.RESET+"|",Fore.BLUE+"Abril",+naño,Fore.RESET+"                    |")
        elif mes==5:
            print("favor de presionar enter para seguir o ingresa cualquier cosa")
            print(Fore.RESET+"-------------------------------- -")
            print(Fore.RESET+"|",Fore.BLUE+"Mayo",+naño,Fore.RESET+"                     |")
        elif mes==6:
            print("favor de presionar enter para seguir o ingresa cualquier cosa")
            print(Fore.RESET+"----------------------------------")
            print(Fore.RESET+"|",Fore.BLUE+"Junio",+naño,Fore.RESET+"                    |")
        elif mes==7:
            print("favor de presionar enter para seguir o ingresa cualquier cosa")
            print(Fore.RESET+"----------------------------------")
            print(Fore.RESET+"|",Fore.BLUE+"Julio",+naño,Fore.RESET+"                    |")
        elif mes==8:
            print("favor de presionar enter para seguir o ingresa cualquier cosa")
            print(Fore.RESET+"----------------------------------")
            print(Fore.RESET+"|",Fore.BLUE+"Agosto",+naño,Fore.RESET+"                   |")
        elif mes==9:
            print("favor de presionar enter para seguir o ingresa cualquier cosa")
            print(Fore.RESET+"----------------------------------")
            print(Fore.RESET+"|",Fore.BLUE+"Septiembre",+naño,Fore.RESET+"               |")
        elif mes==10:
            print("favor de presionar enter para seguir o ingresa cualquier cosa")
            print(Fore.RESET+"---------------------------------")
            print(Fore.RESET+"|",Fore.BLUE+"Octubre",+naño,Fore.RESET+"                 |")
        elif mes==11:
            print("favor de presionar enter para seguir o ingresa cualquier cosa")
            print(Fore.RESET+"-----------------------------------")
            print(Fore.RESET+"|",Fore.BLUE+"Noviembre",+naño,Fore.RESET+"                 |")
        elif mes==12:
            print("favor de presionar enter para seguir o ingresa cualquier cosa")
            print(Fore.RESET+"----------------------------------")
            print(Fore.RESET+"|",Fore.BLUE+"Diciembre",+naño,Fore.RESET+"                |")
        return naño,nmes;
def semana(año,mes):
    init();
    if mes==1:
        mess=mes+12
        años=año-1
    elif mes==2:
        mess=mes+12
        años=año-1
    else:
        mess=mes
        años=año
    r=(1+((13*(mess+1))//5)+años+(años//4)-(años//100)+(años//400))%7
    if (r==0):
        print(Fore.RESET+"----------------------------------")
        print(Fore.YELLOW+"|SA| |DO| |LU| |MA| |MI| |JU| |VI|")
        print(Fore.RESET+"---------------------------------")
    elif (r==1):
        print(Fore.RESET+"----------------------------------")
        print(Fore.YELLOW+"|DO| |LU| |MA| |MI| |JU| |VI| |SA|")
        print(Fore.RESET+"----------------------------------")
    elif (r==2):
        print(Fore.RESET+"----------------------------------")
        print(Fore.YELLOW+"|LU| |MA| |MI| |JU| |VI| |SA| |DO|")
        print(Fore.RESET+"----------------------------------")
    elif (r==3):
        print(Fore.RESET+"----------------------------------")
        print(Fore.YELLOW+"|MA| |MI| |JU| |VI| |SA| |DO| |LU|")
        print(Fore.RESET+"----------------------------------")
    elif (r==4):
        print(Fore.RESET+"----------------------------------")
        print(Fore.YELLOW+"|MI| |JU| |VI| |SA| |DO| |LU| |MA|")
        print(Fore.RESET+"----------------------------------")
    elif (r==5):
        print(Fore.RESET+"----------------------------------")
        print(Fore.YELLOW+"|JU| |VI| |SA| |DO| |LU| |MA| |MI|")
        print(Fore.RESET+"----------------------------------")
    elif (r==6):
        print(Fore.RESET+"----------------------------------")
        print(Fore.YELLOW+"|VI| |SA| |DO| |LU| |MA| |MI| |JU|")
        print(Fore.RESET+"----------------------------------")

def diasdelmes(año,mes):
    if (mes==1):
        print(Fore.GREEN+"|1 |",Fore.RESET+"|2 | |3 | |4 | |5 | |6 | |7 |")
        print("----------------------------------")
        print("|8 | |9 | |10| |11| |12| |13| |14|")
        print("----------------------------------")
        print("|15| |16| |17| |18| |19| |20| |21|")
        print("----------------------------------")
        print("|22| |23| |24| |25| |26| |27| |28|")
        print("----------------------------------")
        print("|29| |30| |31| |  | |  | |  | |  |")
        print("----------------------------------")
    elif mes==2 and año%4==0 and (año%100 !=0 or año % 400 == 0):
        print(Fore.GREEN+"|1 |",Fore.RESET+"|2 | |3 | |4 | |5 | |6 | |7 |")
        print("----------------------------------")
        print("|8 | |9 | |10| |11| |12| |13| |14|")
        print("----------------------------------")
        print("|15| |16| |17| |18| |19| |20| |21|")
        print("----------------------------------")
        print("|22| |23| |24| |25| |26| |27| |28|")
        print("----------------------------------")
        print("|29| |  | |  | |  | |  | |  | |  |")
        print("----------------------------------")
    elif (mes==2):
        print(Fore.GREEN+"|1 |",Fore.RESET+"|2 | |3 | |4 | |5 | |6 | |7 |")
        print("----------------------------------")
        print("|8 | |9 | |10| |11| |12| |13| |14|")
        print("----------------------------------")
        print("|15| |16| |17| |18| |19| |20| |21|")
        print("----------------------------------")
        print("|22| |23| |24| |25| |26| |27| |28|")
        print("----------------------------------")
    elif (mes==3):
        print(Fore.GREEN+"|1 |",Fore.RESET+"|2 | |3 | |4 | |5 | |6 | |7 |")
        print("----------------------------------")
        print("|8 | |9 | |10| |11| |12| |13| |14|")
        print("----------------------------------")
        print("|15| |16| |17| |18| |19| |20| |21|")
        print("----------------------------------")
        print("|22| |23| |24| |25| |26| |27| |28|")
        print("----------------------------------")
        print("|29| |30| |31| |  | |  | |  | |  |")
        print("----------------------------------")
    elif (mes==4):
        print(Fore.GREEN+"|1 |",Fore.RESET+"|2 | |3 | |4 | |5 | |6 | |7 |")
        print("----------------------------------")
        print("|8 | |9 | |10| |11| |12| |13| |14|")
        print("----------------------------------")
        print("|15| |16| |17| |18| |19| |20| |21|")
        print("----------------------------------")
        print("|22| |23| |24| |25| |26| |27| |28|")
        print("----------------------------------")
        print("|29| |30| |  | |  | |  | |  | |  |")
        print("----------------------------------")
    elif (mes==5):
        print(Fore.GREEN+"|1 |",Fore.RESET+"|2 | |3 | |4 | |5 | |6 | |7 |")
        print("----------------------------------")
        print("|8 | |9 | |10| |11| |12| |13| |14|")
        print("----------------------------------")
        print("|15| |16| |17| |18| |19| |20| |21|")
        print("----------------------------------")
        print("|22| |23| |24| |25| |26| |27| |28|")
        print("----------------------------------")
        print("|29| |30| |31| |  | |  | |  | |  |")
        print("----------------------------------")
    elif (mes==6):
        print(Fore.GREEN+"|1 |",Fore.RESET+"|2 | |3 | |4 | |5 | |6 | |7 |")
        print("----------------------------------")
        print("|8 | |9 | |10| |11| |12| |13| |14|")
        print("----------------------------------")
        print("|15| |16| |17| |18| |19| |20| |21|")
        print("----------------------------------")
        print("|22| |23| |24| |25| |26| |27| |28|")
        print("----------------------------------")
        print("|29| |30| |  | |  | |  | |  | |  |")
        print("----------------------------------")
    elif (mes==7):
        print(Fore.GREEN+"|1 |",Fore.RESET+"|2 | |3 | |4 | |5 | |6 | |7 |")
        print("----------------------------------")
        print("|8 | |9 | |10| |11| |12| |13| |14|")
        print("----------------------------------")
        print("|15| |16| |17| |18| |19| |20| |21|")
        print("----------------------------------")
        print("|22| |23| |24| |25| |26| |27| |28|")
        print("----------------------------------")
        print("|29| |30| |31| |  | |  | |  | |  |")
        print("----------------------------------")
    elif (mes==8):
        print(Fore.GREEN+"|1 |",Fore.RESET+"|2 | |3 | |4 | |5 | |6 | |7 |")
        print("----------------------------------")
        print("|8 | |9 | |10| |11| |12| |13| |14|")
        print("----------------------------------")
        print("|15| |16| |17| |18| |19| |20| |21|")
        print("----------------------------------")
        print("|22| |23| |24| |25| |26| |27| |28|")
        print("----------------------------------")
        print("|29| |30| |31| |  | |  | |  | |  |")
        print("----------------------------------")
    elif (mes==9):
        print(Fore.GREEN+"|1 |",Fore.RESET+"|2 | |3 | |4 | |5 | |6 | |7 |")
        print("----------------------------------")
        print("|8 | |9 | |10| |11| |12| |13| |14|")
        print("----------------------------------")
        print("|15| |16| |17| |18| |19| |20| |21|")
        print("----------------------------------")
        print("|22| |23| |24| |25| |26| |27| |28|")
        print("----------------------------------")
        print("|29| |30| |  | |  | |  | |  | |  |")
        print("----------------------------------")
    elif (mes==10):
        print(Fore.GREEN+"|1 |",Fore.RESET+"|2 | |3 | |4 | |5 | |6 | |7 |")
        print("----------------------------------")
        print("|8 | |9 | |10| |11| |12| |13| |14|")
        print("----------------------------------")
        print("|15| |16| |17| |18| |19| |20| |21|")
        print("----------------------------------")
        print("|22| |23| |24| |25| |26| |27| |28|")
        print("----------------------------------")
        print("|29| |30| |31| |  | |  | |  | |  |")
        print("----------------------------------")
    elif (mes==11):
        print(Fore.GREEN+"|1 |",Fore.RESET+"|2 | |3 | |4 | |5 | |6 | |7 |")
        print("----------------------------------")
        print("|8 | |9 | |10| |11| |12| |13| |14|")
        print("----------------------------------")
        print("|15| |16| |17| |18| |19| |20| |21|")
        print("----------------------------------")
        print("|22| |23| |24| |25| |26| |27| |28|")
        print("----------------------------------")
        print("|29| |30| |  | |  | |  | |  | |  |")
        print("----------------------------------")
    elif (mes==12):
        print(Fore.GREEN+"|1 |",Fore.RESET+"|2 | |3 | |4 | |5 | |6 | |7 |")
        print("----------------------------------")
        print("|8 | |9 | |10| |11| |12| |13| |14|")
        print("----------------------------------")
        print("|15| |16| |17| |18| |19| |20| |21|")
        print("----------------------------------")
        print("|22| |23| |24| |25| |26| |27| |28|")
        print("----------------------------------")
        print("|29| |30| |31| |  | |  | |  | |  |")
        print("----------------------------------")
    input();

def main():
    from colorama import Cursor, init, Fore;
    import msvcrt;
    import os;
    init();
    X=1
    Y=1
    a=0
    while True:
        print("-Perez Valdovinos Uriel Alejandro\n-Perez Tovar Santiago \n-Perez Ruelas Jesus Isaias\n-Practica numero 8\n-Equipo\n-Seccion D01")
        print("Favor de ingresar los numeros en su variable entera y ingrese 0 para salir")
        try:
            año=int(input("dame el año mi rey:"))
            while año < 0:
                año=int(input("ingresa un numero valido \ndame el año mi rey: "))
            if año==0:
                break
            elif año>=1:
                pass
        except:
            print("ingresa un valor valido en numeros enteros")
            main();
        try:
            mes=int(input("dame el mes mi rey:"))
            while mes <= 0:
                mes=int(input("ingresa un numero valido \ndame el mes mi rey: "))
            if (mes>=1) and (mes<=12):
                pass
            elif (mes==0):
                break
        except:
            print("ingresa un valor valido en numeros enteros")
            main();
        try:
            cuantos=int(input("cuantos meses quieres imprimir"))
            while cuantos <= 0:
                cuantos=int(input("ingresa un numero valido \ncuantos meses quieres imprimir"))
            if (cuantos>=1) and (cuantos<=12):
                pass
            if (cuantos==0):
                break
        except:
            print("ingresa un valor valido en numeros enteros")
            main();
    
        for a in range (cuantos):
            añoymes(año,mes);
            semana(año,mes);
            diasdelmes(año,mes);
            mes=mes+1;
            e();
main();

