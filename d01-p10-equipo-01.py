1
 with open('Usuarios.json','a') as json_file:
                                
                                
                                json.dump(base_de_datos,json_file,indent=4)
                                json_file.close();
2
[
    {
        "A": 
    }
]

print("Si quieres avanzar preciona enter, si quieres volver usa ESC \n");
    tecla=getch();
    if (ord(tecla)==27):
        Altas();
    elif (ord(tecla)==13):
        cp=int(input("Cuantas personas quieres dar de alta?\n"));
        persona1=[]
        salario1=[]
        personaid1=[]
        for i in range(cp):
            
            persona=input("nombre del empleado:")
            persona1.append(persona)
            salario=(input("Ingresa el salario:"))
            salario1.append(salario)
            personaid=(input("ingresa la id (solo numeros):"))
            personaid1.append(personaid)

            print("Ya fue registrado");
            base_de_datos1=[]
            persona={}
            persona['EMPLEADO']=persona
            persona['id']=personaid
            base_de_datos1.append(persona)
            with open('Usuarios.json','a') as json_file:
                
                json.dump(base_de_datos1,json_file)
                                
                json_file.close();
