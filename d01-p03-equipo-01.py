print("Perez Valdovinos Uriel ALejandro");
print("Perez Tovar Santiago");
print("Perez Ruelas Jesus Isaias");
print("practica numero 3");
print("TEMA Uso de condicional if");
print("seccion d01");
print("equipo numero 1");

 
def el1():
    precio=float(input("cuanto cuestan las sandias?"));
    sandia=float(input("cuantas sandias vas a querer?"));
    o=0
    o=precio
    
    if o<=0:
        print("cantidad no aceptada");
    if o>=1:
        ();
    opc=0
    opc=sandia
    if opc <=0:
        print("venta no procesada");
    elif opc >=7:
        PS= precio*sandia;
        gana=PS*.60
        print("es un total de",gana,"$");
    
    elif opc >=1 <=2:
        print("recibiste un descuento del 10%");
        PS= precio*sandia;
        gana=PS*.90
        print("es un total de",gana,"$");
    
    elif opc>=3 <=6:
        PS= precio*sandia;
        gana=PS
        print("es un total de",gana,"$");
        print("no recibes decuento")
    else:
        print("venta no procesada")
    
    
el1()



def el2():
    precio=float(input("cuanto fue costo general por materia?"))
    materia=float(input("cuantas asignaturas tienes en el semestre?"));
    calificaion=float(input("cual es tu calificacion?"));
    p=0
    p=precio
    if p<=0:
        print("no se aceptan datos negativos");

    
    op=0
    op=materia
    if op<=0:
        print("numero de materias incorretos");
    if op>=4 <=9:
        print()
    
    else:
        print("numero de materias incorrectas");
    
    opc=calificaion
    if opc<=0:
        print("no se aceptan datos negativos");
    if opc>=80.5 <=100:
        k1=((materia*precio)*.75);
        print("tu mensualidad sera de",int(k1));
    elif opc >=1 <=80.4:
        k2=(materia*precio);
        print("tu mensualidad sera de",int(k2));
    
    else:
        print("calificaion erronea");

el2()

def p3():
    pj=95.70;
    ph=pj/8;    #la jornada se paga a 95.70 asi que la cantidad se dividio entre 8 los cuales son las horas que tiene una joranada
    ht=int(input("¿cuantas horas trabajaste?"));
    if ht>=49 and ht<=56:
        t1=(ph*8*2)+(ph*(ht-48)*3);
        t2=(ph*8*2)+(ph*(ht-8)*3);
        print("esto te van a pagar por las horas extras",int(t1),"$");
        print("esto te van a pagar por",ht,"horas de trabajo",int(t2),"$");
    elif ht>=41 and ht<=48:
        t3=(ph*(ht-40));
        t4=(ph*ht);
        print("esto te van a pagar por las horas extras",int(t3),"$");
        print("esto te van a pagar por",ht,"horas de trabajo",int(t4),"$");
    elif ht>=1 and ht<=40:
        t5=ht*ph;
        print("no hay horas extras que pagar");
        print("esto te van a pagar por",ht,"horas de trabajo",int(t5),"$");
    elif ht<0:
        print("numero de horas no valido");
    else:
        print("si trabajas más de 56 horas es ilegal y puedes demandar a tu patrón ten cuidado mi rey");
p3();


def el3():
    o=int(input("¿cuantos arboles deseas plantar?:---->"));
    Ca=10;
    Pt=o;
    P= (Pt*.10);
    Pc= P*Ca;
    C= (Pt*.40);
    Cc= C*Ca;
    Eb= (Pt*.10);
    Ebc= Eb*Ca;
    Eu= (Pt*.40);
    Euc= Eu*Ca;
    
    if Pt <=0:
        print("lo siento no aceptamos a gente negativa");
    elif Cc and Euc < 5000000:
        Ct= (C*10/100)+C;
        Ctc=Ct*Ca;
        Eut= (Eu*10/100)+Eu;
        Eutc= Eut*Ca;
        print ("arboles plantados en total:");
        print("hubo un extra en cendro y eucalipto");
        print("Pino:", int(P));
        print("Costo de plantar pino", Pc);
 
        print("Cedro:", int(Ct));
        print("Costo de plantar cendro sin extra", Cc);
        print("Costo de plantar cedro con extra", Ctc);
        
        print("Ebano:", int(Eb));
        print("Costo de plantar Ebano", Ebc);
 
        print("Eucalipto:", int(Eut));
        print("Costo de plantar eucalipto sin extra", Euc);
        print("Costo de plantar eucalipto con extra", Eutc);
    elif  Cc and Euc > 5000000 :
        Pt= (P*10/100)+P;
        Ptc=Pt*Ca;
        Ebt= (Eb*10/100)+Eb;
        Ebtc= Ebt*Ca;
        print ("arboles plantados en total:");
        print("hubo un extra en pino y ebano");
        print("Pino:", int(Pt));
        print("Costo de plantar pino sin extra", Pc);
        print("Costo de plantar pino con extra", Ptc);
 
        print("Cedro:", int(C));
        print("Costo de plantar cedro", Cc);
        
        print("Ebano:", int(Ebt));
        print("Costo de plantar Ebano sin extra", Ebc);
        print("Costo de plantar Ebano con extra", Ebtc);
 
        print("Eucalipto:", int(Eu));
        print("Costo de plantar eucalipto", Euc);
 
el3();
