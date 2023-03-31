from colorama import init
from colorama import Fore
from colorama import Cursor
año=int(input("dame el año mi rey:"))
mes=int(input("dame el mes mi rey:"))
def añoymes():
    init()
    global año
    global mes
    if (año>=0) and (mes>=0):
        if mes==1:
            print(Fore.BLUE+"Enero",año)
        elif mes==2:
            print(Fore.BLUE+"Febrero",año)
        elif mes==3:
            print(Fore.BLUE+"Marzo",año)
        elif mes==4:
            print(Fore.BLUE+"Abril",+año)
        elif mes==5:
            print(Fore.BLUE+"Mayo",+año)
        elif mes==6:
            print(Fore.BLUE+"Junio",+año)
        elif mes==7:
            print(Fore.BLUE+"Julio",+año)
        elif mes==8:
            print(Fore.BLUE+"Agosto",+año)
        elif mes==9:
            print(Fore.BLUE+"Septiembre",+año)
        elif mes==10:
            print(Fore.BLUE+"Octubre",+año)
        elif mes==11:
            print(Fore.BLUE+"Noviembre",+año)
        elif mes==12:
            print(Fore.BLUE+"Diciembre",+año)
def semana():
    global año
    global mes
    if mes==1 or mes==2 or mes==3 or mes==4 or mes==5 or mes==6 or mes==7 or mes==8 or mes==9 or mes==10 or mes==11 or mes==12:
        a = int((14 - mes) / 12)
        y = año - a
        m = int(mes + (12 * a) - 2)
        r = int(2 + y + int(y/4) - int(y/100) + int(y/400)+((31*m) / 12)) % 7
        
    if (r==0):
        print(Fore.YELLOW+"SA DO LU MA MI JU VI")
    elif (r==1):
        print(Fore.YELLOW+"DO LU MA MI JU VI SA")
    elif (r==2):
        print(Fore.YELLOW+"LU MA MI JU VI SA DO")
    elif (r==3):
        print(Fore.YELLOW+"MA MI JU VI SA DO LU")
    elif (r==4):
        print(Fore.YELLOW+"MI JU VI SA DO LU MA")
    elif (r==5):
        print(Fore.YELLOW+"JU VI SA DO LU MA MI")
    elif (r==6):
        print(Fore.YELLOW+"VI SA DO LU MA MI JU")
   
def diasdelmes():
    global año
    global mes
    if (mes==1):
        print("1 ",Fore.RESET+"2  3  4  5  6  7\n8  9  10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29 30 31")
    elif mes==2 and año%4==0 and (año%100 !=0 or año % 400 == 0):
        print("1 ",Fore.RESET+"2  3  4  5  6  7\n8  9  10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29")
    elif (mes==2):
        print("1 ",Fore.RESET+"2  3  4  5  6  7\n8  9  10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28")
    elif (mes==3):
        print("1 ",Fore.RESET+"2  3  4  5  6  7\n8  9  10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29 30 31")
    elif (mes==4):
        print("1 ",Fore.RESET+"2  3  4  5  6  7\n8  9  10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29 30")
    elif (mes==5):
        print("1 ",Fore.RESET+"2  3  4  5  6  7\n8  9  10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29 30 31")
    elif (mes==6):
        print("1 ",Fore.RESET+"2  3  4  5  6  7\n8  9  10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29 30")
    elif (mes==7):
        print("1 ",Fore.RESET+"2  3  4  5  6  7\n8  9  10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29 30 31")
    elif (mes==8):
        print("1 ",Fore.RESET+"2  3  4  5  6  7\n8  9  10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29 30 31")
    elif (mes==9):
        print("1 ",Fore.RESET+"2  3  4  5  6  7\n8  9  10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29 30")
    elif (mes==10):
        print("1 ",Fore.RESET+"2  3  4  5  6  7\n8  9  10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29 30 31")
    elif (mes==11):
        print("1 ",Fore.RESET+"2  3  4  5  6  7\n8  9  10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29 30")
    elif (mes==12):
        print("1 ",Fore.RESET+"2  3  4  5  6  7\n8  9  10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29 30 31")
    input();
añoymes();
semana();
diasdelmes();
