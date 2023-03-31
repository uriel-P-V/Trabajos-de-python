from msvcrt import getch
from msvcrt import getche
from msvcrt import kbhit
import os
from colorama import Cursor,init,Fore;

def e1():
    init();
    x=25;
    y=25;
    a=50
    b=25
    p=75
    q=25
    while True:
        print(Cursor.POS(1,1)+Fore.WHITE+"Usa las Teclas W,A,S,D para mover el cuadrado")
        print(Cursor.POS(1,8)+Fore.WHITE+"Nota:Profe hay un bug que pasa en mi computadora, que es que cuando tienes el archivo abierto en el editor de python y en cmd los comandos de las teclas no funcionan, lo aclaro por si a usted le pasa lo mismo")
        print(Cursor.POS(1,2)+Fore.WHITE+"Usa las Teclas U,H,J,K para mover el triangulo")
        print(Cursor.POS(1,3)+Fore.WHITE+"Usa las Flechas del teclado para mover el circulo")
        print(Cursor.POS(1,4)+Fore.WHITE+"Usa la Tecla ESC para salir")
        print(Cursor.POS(70,1)+Fore.LIGHTBLUE_EX+"PEREZ VALDOVINOS URIEL ALEJANDRO");
        print(Cursor.POS(70,2)+Fore.LIGHTBLUE_EX+"PEREZ TOVAR SANTIAGO");
        print(Cursor.POS(70,3)+Fore.LIGHTBLUE_EX+"PEREZ RUELAS JESUS ISAIAS");
        print(Cursor.POS(70,4)+Fore.LIGHTBLUE_EX+"practica numero 6");
        print(Cursor.POS(70,5)+Fore.LIGHTBLUE_EX+"TEMA uso de colorama");
        print(Cursor.POS(70,6)+Fore.LIGHTBLUE_EX+"equipo 1");
        print(Cursor.POS(70,7)+Fore.LIGHTBLUE_EX+"Sección: D01");
        tecla=getch();
        if(ord(tecla)==119):
            #("hacia arriba")
            os.system ("cls");
            y=y-1;
            print(Cursor.POS(a,b)+ Fore.LIGHTYELLOW_EX + "*");
            print(Cursor.POS(a-1,b-1)+ Fore.LIGHTYELLOW_EX + "***");
            print(Cursor.POS(a-2,b-2)+ Fore.LIGHTYELLOW_EX + "*****");
            print(Cursor.POS(a-3,b-3)+ Fore.LIGHTYELLOW_EX + "*******");
            print(Cursor.POS(p,q)+ Fore.RED + " ****");
            print(Cursor.POS(p,q-1)+ Fore.RED + "*    *");
            print(Cursor.POS(p,q-2)+ Fore.RED + "*    *");
            print(Cursor.POS(p,q-3)+ Fore.RED + " ****");
            print(Cursor.POS(x,y)+ Fore.GREEN + "********");
            print(Cursor.POS(x,y-1)+ Fore.GREEN  + "*      *");
            print(Cursor.POS(x,y-2)+ Fore.GREEN + "*      *");
            print(Cursor.POS(x,y-3)+ Fore.GREEN + "********");
        elif(ord(tecla)==100):
            #("hacia derecha")
            os.system ("cls");
            x=x+1
            print(Cursor.POS(a,b)+ Fore.LIGHTYELLOW_EX + "*");
            print(Cursor.POS(a-1,b-1)+ Fore.LIGHTYELLOW_EX + "***");
            print(Cursor.POS(a-2,b-2)+ Fore.LIGHTYELLOW_EX + "*****");
            print(Cursor.POS(a-3,b-3)+ Fore.LIGHTYELLOW_EX + "*******");
            print(Cursor.POS(p,q)+ Fore.RED + " ****");
            print(Cursor.POS(p,q-1)+ Fore.RED + "*    *");
            print(Cursor.POS(p,q-2)+ Fore.RED + "*    *");
            print(Cursor.POS(p,q-3)+ Fore.RED + " ****");
            print(Cursor.POS(x,y)+ Fore.GREEN + "********");
            print(Cursor.POS(x,y-1)+ Fore.GREEN  + "*      *");
            print(Cursor.POS(x,y-2)+ Fore.GREEN + "*      *");
            print(Cursor.POS(x,y-3)+ Fore.GREEN + "********");
            
        elif(ord(tecla)==97):
            #("hacia izquierda")
            os.system ("cls");
            x=x-1
            print(Cursor.POS(a,b)+ Fore.LIGHTYELLOW_EX + "*");
            print(Cursor.POS(a-1,b-1)+ Fore.LIGHTYELLOW_EX + "***");
            print(Cursor.POS(a-2,b-2)+ Fore.LIGHTYELLOW_EX + "*****");
            print(Cursor.POS(a-3,b-3)+ Fore.LIGHTYELLOW_EX + "*******");
            print(Cursor.POS(p,q)+ Fore.RED + " ****");
            print(Cursor.POS(p,q-1)+ Fore.RED + "*    *");
            print(Cursor.POS(p,q-2)+ Fore.RED + "*    *");
            print(Cursor.POS(p,q-3)+ Fore.RED + " ****");
            print(Cursor.POS(x,y)+ Fore.GREEN + "********");
            print(Cursor.POS(x,y-1)+ Fore.GREEN  + "*      *");
            print(Cursor.POS(x,y-2)+ Fore.GREEN + "*      *");
            print(Cursor.POS(x,y-3)+ Fore.GREEN + "********");
        elif(ord(tecla)==115):
            #("hacia abajo")
            os.system ("cls");
            y=y+1;
            print(Cursor.POS(a,b)+ Fore.LIGHTYELLOW_EX + "*");
            print(Cursor.POS(a-1,b-1)+ Fore.LIGHTYELLOW_EX + "***");
            print(Cursor.POS(a-2,b-2)+ Fore.LIGHTYELLOW_EX + "*****");
            print(Cursor.POS(a-3,b-3)+ Fore.LIGHTYELLOW_EX + "*******");
            print(Cursor.POS(p,q)+ Fore.RED + " ****");
            print(Cursor.POS(p,q-1)+ Fore.RED + "*    *");
            print(Cursor.POS(p,q-2)+ Fore.RED + "*    *");
            print(Cursor.POS(p,q-3)+ Fore.RED + " ****");
            print(Cursor.POS(x,y)+ Fore.GREEN + "********");
            print(Cursor.POS(x,y-1)+ Fore.GREEN  + "*      *");
            print(Cursor.POS(x,y-2)+ Fore.GREEN + "*      *");
            print(Cursor.POS(x,y-3)+ Fore.GREEN + "********");
        elif(ord(tecla)==117):
            #("hacia arriba")
            os.system ("cls")
            b=b-1;
            print(Cursor.POS(x,y)+ Fore.RED + "********");
            print(Cursor.POS(x,y-1)+ Fore.RED  + "*      *");
            print(Cursor.POS(x,y-2)+ Fore.RED + "*      *");
            print(Cursor.POS(x,y-3)+ Fore.RED + "********");
            print(Cursor.POS(p,q)+ Fore.LIGHTYELLOW_EX + " ****");
            print(Cursor.POS(p,q-1)+ Fore.LIGHTYELLOW_EX + "*    *");
            print(Cursor.POS(p,q-2)+ Fore.LIGHTYELLOW_EX + "*    *");
            print(Cursor.POS(p,q-3)+ Fore.LIGHTYELLOW_EX + " ****");
            print(Cursor.POS(a,b)+ Fore.GREEN + "*");
            print(Cursor.POS(a-1,b-1)+ Fore.GREEN + "***");
            print(Cursor.POS(a-2,b-2)+ Fore.GREEN + "*****");
            print(Cursor.POS(a-3,b-3)+ Fore.GREEN + "*******");

        elif(ord(tecla)==107):
            #("hacia derecha")
            os.system ("cls")
            a=a+1
            print(Cursor.POS(x,y)+ Fore.RED + "********");
            print(Cursor.POS(x,y-1)+ Fore.RED  + "*      *");
            print(Cursor.POS(x,y-2)+ Fore.RED + "*      *");
            print(Cursor.POS(x,y-3)+ Fore.RED + "********");
            print(Cursor.POS(p,q)+ Fore.LIGHTYELLOW_EX + " ****");
            print(Cursor.POS(p,q-1)+ Fore.LIGHTYELLOW_EX + "*    *");
            print(Cursor.POS(p,q-2)+ Fore.LIGHTYELLOW_EX + "*    *");
            print(Cursor.POS(p,q-3)+ Fore.LIGHTYELLOW_EX + " ****");
            print(Cursor.POS(a,b)+ Fore.GREEN + "*");
            print(Cursor.POS(a-1,b-1)+ Fore.GREEN + "***");
            print(Cursor.POS(a-2,b-2)+ Fore.GREEN + "*****");
            print(Cursor.POS(a-3,b-3)+ Fore.GREEN + "*******");
        elif(ord(tecla)==104):
            #("hacia izquierda")
            os.system ("cls")
            a=a-1
            print(Cursor.POS(x,y)+ Fore.RED + "********");
            print(Cursor.POS(x,y-1)+ Fore.RED  + "*      *");
            print(Cursor.POS(x,y-2)+ Fore.RED + "*      *");
            print(Cursor.POS(x,y-3)+ Fore.RED + "********");
            print(Cursor.POS(p,q)+ Fore.LIGHTYELLOW_EX + " ****");
            print(Cursor.POS(p,q-1)+ Fore.LIGHTYELLOW_EX + "*    *");
            print(Cursor.POS(p,q-2)+ Fore.LIGHTYELLOW_EX + "*    *");
            print(Cursor.POS(p,q-3)+ Fore.LIGHTYELLOW_EX + " ****");
            print(Cursor.POS(a,b)+ Fore.GREEN + "*");
            print(Cursor.POS(a-1,b-1)+ Fore.GREEN + "***");
            print(Cursor.POS(a-2,b-2)+ Fore.GREEN + "*****");
            print(Cursor.POS(a-3,b-3)+ Fore.GREEN + "*******");
        elif(ord(tecla)==106):
            #("hacia abajo")
            os.system ("cls")
            b=b+1;
            print(Cursor.POS(x,y)+ Fore.RED + "********");
            print(Cursor.POS(x,y-1)+ Fore.RED  + "*      *");
            print(Cursor.POS(x,y-2)+ Fore.RED + "*      *");
            print(Cursor.POS(x,y-3)+ Fore.RED + "********");
            print(Cursor.POS(p,q)+ Fore.LIGHTYELLOW_EX + " ****");
            print(Cursor.POS(p,q-1)+ Fore.LIGHTYELLOW_EX + "*    *");
            print(Cursor.POS(p,q-2)+ Fore.LIGHTYELLOW_EX + "*    *");
            print(Cursor.POS(p,q-3)+ Fore.LIGHTYELLOW_EX + " ****");
            print(Cursor.POS(a,b)+ Fore.GREEN + "*");
            print(Cursor.POS(a-1,b-1)+ Fore.GREEN + "***");
            print(Cursor.POS(a-2,b-2)+ Fore.GREEN + "*****");
            print(Cursor.POS(a-3,b-3)+ Fore.GREEN + "*******");
        elif(ord(tecla)==72):
            #("hacia arriba")
            os.system ("cls")
            q=q-1
            print(Cursor.POS(x,y)+ Fore.LIGHTYELLOW_EX + "********");
            print(Cursor.POS(x,y-1)+ Fore.LIGHTYELLOW_EX  + "*      *");
            print(Cursor.POS(x,y-2)+ Fore.LIGHTYELLOW_EX + "*      *");
            print(Cursor.POS(x,y-3)+ Fore.LIGHTYELLOW_EX + "********");
            print(Cursor.POS(a,b)+ Fore.RED + "*");
            print(Cursor.POS(a-1,b-1)+ Fore.RED + "***");
            print(Cursor.POS(a-2,b-2)+ Fore.RED + "*****");
            print(Cursor.POS(a-3,b-3)+ Fore.RED + "*******");
            print(Cursor.POS(p,q)+ Fore.GREEN + " ****");
            print(Cursor.POS(p,q-1)+ Fore.GREEN + "*    *");
            print(Cursor.POS(p,q-2)+ Fore.GREEN + "*    *");
            print(Cursor.POS(p,q-3)+ Fore.GREEN + " ****");
        elif(ord(tecla)==77):
            #("hacia derecha")
            os.system ("cls")
            p=p+1
            print(Cursor.POS(x,y)+ Fore.LIGHTYELLOW_EX + "********");
            print(Cursor.POS(x,y-1)+ Fore.LIGHTYELLOW_EX  + "*      *");
            print(Cursor.POS(x,y-2)+ Fore.LIGHTYELLOW_EX + "*      *");
            print(Cursor.POS(x,y-3)+ Fore.LIGHTYELLOW_EX + "********");
            print(Cursor.POS(a,b)+ Fore.RED + "*");
            print(Cursor.POS(a-1,b-1)+ Fore.RED + "***");
            print(Cursor.POS(a-2,b-2)+ Fore.RED + "*****");
            print(Cursor.POS(a-3,b-3)+ Fore.RED + "*******");
            print(Cursor.POS(p,q)+ Fore.GREEN + " ****");
            print(Cursor.POS(p,q-1)+ Fore.GREEN + "*    *");
            print(Cursor.POS(p,q-2)+ Fore.GREEN + "*    *");
            print(Cursor.POS(p,q-3)+ Fore.GREEN + " ****");
        elif(ord(tecla)==75):
            #("hacia izquierda")
            os.system ("cls")
            p=p-1
            print(Cursor.POS(x,y)+ Fore.LIGHTYELLOW_EX + "********");
            print(Cursor.POS(x,y-1)+ Fore.LIGHTYELLOW_EX  + "*      *");
            print(Cursor.POS(x,y-2)+ Fore.LIGHTYELLOW_EX + "*      *");
            print(Cursor.POS(x,y-3)+ Fore.LIGHTYELLOW_EX + "********");
            print(Cursor.POS(a,b)+ Fore.RED + "*");
            print(Cursor.POS(a-1,b-1)+ Fore.RED + "***");
            print(Cursor.POS(a-2,b-2)+ Fore.RED + "*****");
            print(Cursor.POS(a-3,b-3)+ Fore.RED + "*******");
            print(Cursor.POS(p,q)+ Fore.GREEN + " ****");
            print(Cursor.POS(p,q-1)+ Fore.GREEN + "*    *");
            print(Cursor.POS(p,q-2)+ Fore.GREEN + "*    *");
            print(Cursor.POS(p,q-3)+ Fore.GREEN + " ****");
        elif(ord(tecla)==80):
            #("hacia abajo")
            os.system ("cls")
            q=q+1
            print(Cursor.POS(x,y)+ Fore.LIGHTYELLOW_EX + "********");
            print(Cursor.POS(x,y-1)+ Fore.LIGHTYELLOW_EX  + "*      *");
            print(Cursor.POS(x,y-2)+ Fore.LIGHTYELLOW_EX + "*      *");
            print(Cursor.POS(x,y-3)+ Fore.LIGHTYELLOW_EX + "********");
            print(Cursor.POS(a,b)+ Fore.RED + "*");
            print(Cursor.POS(a-1,b-1)+ Fore.RED + "***");
            print(Cursor.POS(a-2,b-2)+ Fore.RED + "*****");
            print(Cursor.POS(a-3,b-3)+ Fore.RED + "*******");
            print(Cursor.POS(p,q)+ Fore.GREEN + " ****");
            print(Cursor.POS(p,q-1)+ Fore.GREEN + "*    *");
            print(Cursor.POS(p,q-2)+ Fore.GREEN + "*    *");
            print(Cursor.POS(p,q-3)+ Fore.GREEN + " ****");
        elif(ord(tecla)==27):
            break
e1();
