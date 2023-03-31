print("Perez Valdovinos Uriel Alejandro");
print("Perez Ruelas Jesus Isaias");
print("Perez Tovar Santiago");
print("práctica 2");
print("TEMA: Uso de funciones sin parámetros");
print("equipo 01");


Tarea1=60;
Tarea2=80;
Tarea3=25.5;
Tarea4=60;
Tarea5=70;
Examen1=100;
Examen2=30;
Examen3=75;
print("1. Un alumno desea saber cuál será su promedio general en las tres materias más difíciles quecursa y cuál será el promedio que obtendrá en cada una de ellas. Estas materias se evalúancomo se muestra a continuación:");
print("La calificación de Fundamentos se obtiene de la siguiente manera:");
print("Examen 25%");
print("Promedio de tareas 75%");
def materia1( ):
    M1=("Fundamentos");
    return M1;
def examanes1( ):
    R1=(Examen1+Examen2+Examen3)/300*25;
    return R1;
def tarea1( ):
    R2=(Tarea1+Tarea2+Tarea3+Tarea4+Tarea5)/500*75;
    return R2;
print("En esta materia se pidió un total de cinco tareas--->",materia1());

print("el promedio del examen de Fundamentos es de",examanes1(),"%");

print("el promedio de tareas de Fundamentos es de", tarea1(),"%");

print("PROMEDIO FINAL=",examanes1()+tarea1(),"%");



print("La calificación de Seguridad se obtiene de la siguiente manera:");
print("Examen 40%");
print("Promedio de tareas 60%");
def materia2( ):
    M2=("Seguridad");
    return M2;
def examanes2( ):
    R3=(Examen1+Examen2+Examen3)/300*40
    return R3;
def tarea2( ):
    R4=(Tarea1+Tarea2)/200*60
    return R4;
print("En esta materia se pidió un total de dos tareas--->",materia2());

print("el promedio del examen de Seguridad es de",examanes2(),"%");

print("el promedio de tareas de Seguridad es de", tarea2(),"%");

print("PROMEDIO FINAL=",examanes2()+tarea2(),"%");



print("La calificación de Computación Tolerante se obtiene de la siguiente manera:");
print("Examen 30%");
print("Promedio de tareas 70%");
def materia3( ):
    M3=("COMPUTACION");
    return M3;
def examenes3():
    R5=(Tarea1+Tarea2+Tarea3)/300*30
    return R5;
def tarea3():
    R6=(Examen1+Examen2+Examen3)/300*70
    return R6;
print("En esta materia se pidió un total de tres tareas--->",materia3());
print("COMPUTACION");

print("el promedio del examen de COMPUTACION es de",examenes3(),"%");

print("el promedio de tareas de COMPUTACION es de", tarea3(),"%");

print("PROMEDIO FINAL=",examenes3()+tarea3(),"%");




print("2.en esta ocasion 3 inversores realizan una inversion de 550 pesos, el porcentaje que les corresponde es el siguiente EL inversor 1 pone 120 el inversor 2 pone 130 y el inversor 3 pone 300");
def inversor1():
    Inv1=120/500*100;
    return Inv1;
def inversor2():
    Inv2=130/500*100;
    return Inv2;
def inversor3():
    Inv3=300/500*100;
    return Inv3;
print("el porcentaje de la empresa del inversor1 es:",inversor1(),"%");
print("el porcentaje de la empresa del inversor1 es:",inversor2(),"%");
print("el porcentaje de la empresa del inversor1 es:",inversor3(),"%");


print("3. Calcular el total de kilos de manzana a pagar si cada kilo cuesta 20.99 $ y se hacen 3 compras una de 2 kilos, 3 kilos y otra de 1 kilos");
kilo=20.99;
def kilos( ):
    K1=(kilo*2)
    return K1;
def kilos2( ):
    K2=(kilo*3)
    return K2;
def kilos3( ):
    K3=(kilo*1)
    return K3;
print("primera compra",kilos(),"$")
print("segunda compra",kilos2(),"$")
print("tercera compra",kilos3(),"$")




print("4. Al reforestar un bosque nos encontramos con los siguientes números:");
print("El costo de sembrar uno por uno es de 30.99 $"); 
print("De un MILLON de arboles sembrados determinar cuantos arboles se sembraron de cada especie y cuanto fue el costo total por cada especie");
def arboles():
    ArbolP=30.99;
    arbT=1000000;
    pinos=arbT*30//100;
    pinosC=pinos*30.99;
    cendro=arbT*20//100;
    cendroC=cendro*30.99;
    ebano=arbT*10//100;
    ebanoC=ebano*30.99;
    eucalipto=arbT*40//100;
    eucaliptoC=eucalipto*30.99;
    pinosT=print("Arboles de  pinos se plantaron", pinos, "que costaron", pinosC, "$");
    cendroT=print("Arboles de  pinos se plantaron", cendro, "que costaron", cendroC, "$");
    ebanoT=print("Arboles de  pinos se plantaron", ebano, "que costaron", ebanoC, "$");
    eucaliptoT=print("Arboles de  pinos se plantaron", eucalipto, "que costaron", eucaliptoC, "$");
    costoT=pinosC+cendroC+ebanoC+eucaliptoC;
    return costoT;
print("Se gasto un total de", arboles(), "$");
