//Incluimos las librerias que aprendimos durante el curso
#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <string>


using namespace std;
//Declaramos todas las del proyecto funciones para que no crashie el programa 
int menu();
void registroMascotas();
void regitroUsuarios();
void mascotasDesaparecidas();
void MenucambioInformacion();
void borrarUsuarios();
//Creamos una clase que se llame mascotas
class mascotas {
    public:
    //Hicimos todos los atributos públicos para que no hubiera mayor problema al accesar los datos
    string Id;
    string Especie;
    string nombreMascota;
    string Raza;
    string Fecha_registro;
    string Estatus;
};
//El main; prácticamente es un agradecimiento en donde se explica en pocas palabras lo que hace el proyecto
int main(){
    cout<<"******************************"<<endl;
    cout<<"¡Bienvenido! Este proyecto esta diseñado para ser una base de datos para mascotas perdidas"<<endl;
    cout<<"Para comenzar, se te desplegará un menú; en donde eligirás en lo que se te puede ayudar"<<endl;
    cout<<"******************************"<<endl;
    cout<<endl;
    //Se llama a la función menú para que se pueda continuar
    menu();
    return 0;
}
//Función que se encarga de Registrar a cada una de las mascotas que ingrese el usuario
void registroMascotas(){
    //Ojo que se crea el objeto de la clase mascotas
    mascotas Mascotas_01;
    //Se declaran variables, que posteriormente serán los atributos del objeto
    string nombreMascota;
    string especie;
    string raza;
    string fecha_reg;
    string estado;
    string linea;
    string estatus;
    int cont=0;
    //Se declaran las variables de entrada y de salida de los documentos 
    ofstream informacionSalida;
    ifstream informacionEntrada;
    //Se abre el archivo de Registro de mascotas
    informacionSalida.open("Registro_mascotas.txt",ios::app);
    cout << "*******************************" << flush << endl << endl;
    cin.ignore();
    cout << setw(20) << left << "Ingresa el nombre de tu mascota: ";
        getline(cin,nombreMascota);
         cin.sync();
    Mascotas_01.nombreMascota = nombreMascota;
    cout << setw(15) << "Ingresa a que especie pertence tu mascota (Perro, gato, etc): ";
        getline(cin,especie);
         cin.sync();
    Mascotas_01.Especie = especie;
    cout << setw(15) << "Ingresa la raza a la cual pertenece tu mascota (Si no sabes teclea 00): ";
        getline(cin,raza);
         cin.sync();
    cout << setw(15) << "Ingresa la fecha de registro: ";
        getline(cin,fecha_reg);
        cin.sync();
    cout<<setw(10) << "Ingresa el estado de la mascota (estable, enfermo, rescatado o desaparecido): " ;
        getline(cin, estatus);
        cin.sync();
     // Se incializa los valores de los atributos del objeto
    Mascotas_01.Raza = raza;
    Mascotas_01.Fecha_registro = fecha_reg;
    Mascotas_01.Estatus = estatus;
    //Se declara que es de tipo de ifstream Registro_mascotas.txt
    ifstream in("Registro_mascotas.txt");
    while (getline(in,linea))
    {
        //Se va sumando el contador
        cont++;
    }
    //Se imprime la informacion del usuario en el archivo en este caso en el txt del Registro_mascotas
    informacionSalida << setw(6) << setfill('0') << right << cont << " ";
        informacionSalida << setw(20) << setfill(' ') << left << Mascotas_01.nombreMascota << " "
            << setw(20) << Mascotas_01.Especie << " "<< setw(20) << Mascotas_01.Raza << " "<< setw(20) << Mascotas_01.Fecha_registro << " "<<  setw(20) << Mascotas_01.Estatus << " "<< endl;

    

    //Se cierra el archivo
    informacionSalida.close();
}
//Función que se encarga de registrar a las personas
void registroUsuarios(){
    string nombreDueno;
    string ciudad;
    string fechaDueno;
    string celular;
    ofstream iregistroUsuarios;
    ifstream oregistroUsuarios;
    iregistroUsuarios.open("Registro_usuarios.txt", ios::app);
    cout<<"************************************"<<endl;
    cin.ignore();
    cout<<"Ingresa tu nombre completo: "<<endl;
        getline(cin,nombreDueno);
        cin.sync();
    cout<<"Ingresa la ciudad en donde vives: "<<endl;
        getline(cin, ciudad);
        cin.sync();
    cout<<"Ingresa la fecha de registro: "<<endl;
        getline(cin, fechaDueno);
        cin.sync();
    cout<<"Ingresa tu número de celular: "<<endl;
        getline(cin, celular);
        cin.sync();
    iregistroUsuarios << setw(1)<< setfill(' ')<< right << nombreDueno << " ";
     iregistroUsuarios << setw(20) << setfill(' ') << left << ciudad << " "
        << setw(20) << fechaDueno << " "<< setw(20) << celular << " "<<endl;

    iregistroUsuarios.close();
}
//Función que despliega todos las mascotas; las cuales tengan un estatus de desaparecidos
void mascotasDesaparecidas(){
    string linea;
    string estatus="desaparecido";
    ifstream informacionSalida;
    informacionSalida.open("Registro_mascotas.txt");
    if(informacionSalida.fail()){
        cout<<"Error al abrir archivo"<<endl;
    }
    else{
        cout<<"****************************"<<endl;
        //Se va iterando linea por linea en el archivo txt
        while((getline(informacionSalida, linea))){
            if(linea.find(estatus,0)!=string::npos){
                cout<<linea<<endl;
            }
        }
    }


}
//Función que se enccarga de hacer los cambios de información en la base de datos
void MenucambioInformacion(){
    int option_2;
    string estatus;
    string linea;
    string id;
    string nuevo_numero;
    string nombre_registro;
    string viejo_numero;
    string texto;
    ifstream informacionSalida;
    ofstream informacionEntrada;
    



    cout<<endl;
    cout<<"******************"<<endl;
    cout<<"1) Cambio de estatus de alguna mascota"<<endl;
    cout<<"2) Cambio de número telefónico"<<endl;
    cout<<"Teclee una opcion: ";
    cin>>option_2;
    if(option_2==1){
        cout<<endl;
        cout<<"Teclee la matrícula de la mascota: ";
        cin>>id;
         cin.sync();
        cout<<"Teclee el nuevo estatus de la mascota: ";
        string nuevo_estatus;
        cin>>nuevo_estatus;
        informacionSalida.open("Registro_mascotas.txt",ios::in);
        informacionEntrada.open("temporal.txt",ios::out);
        if(informacionSalida.fail()){
            cout<< "Error de archivo" << endl;
        }
        else{
            //Se va iterando linea por linea en el archivo txt
            while(getline(informacionSalida,linea)){
                if(linea.find(id,0)!=string::npos){
                    string viejo_estatus = linea.substr(91,100);
                    cout<<"El viejo estatus era: "<<viejo_estatus<<endl;
                    cout<<"Cambio de estatus exitoso"<<endl;
                    //Se va buscando lo que se quiere en el documento y se guarda en la variable linea
                    string linea_nueva = linea.replace(linea.find(viejo_estatus,0), viejo_estatus.length(), nuevo_estatus);
                    linea.replace(linea.find(id, 0),linea_nueva.length(),linea_nueva);
                    informacionEntrada<<linea<<endl;

            }
            else{
                informacionEntrada<<linea<<endl;
            }
            }

              

            


        }
        informacionSalida.close();
        informacionEntrada.close();
        //Se elimina el txt original y se cambia de nombre el del temporal al nombre que tenía el documento original
        remove("Registro_mascotas.txt");
        rename("temporal.txt", "Registro_mascotas.txt");
        
    }
    else if(option_2==2){
        cout<<endl;
        cin.ignore();
        cout<<"Teclee el nombre con el que se registro: ";
        getline(cin,nombre_registro);
        cin.sync();
        informacionSalida.open("Registro_usuarios.txt",ios::in);
        informacionEntrada.open("temporal.txt",ios::out);
        if(informacionSalida.fail()){
            cout<< "Error de archivo" << endl;
        }
        else{
            cout<<"Teclee el nuevo número de telefono: ";
            cin>>nuevo_numero;
            //Se va iterando linea por linea en el archivo txt
            while(getline(informacionSalida,linea)){
                if(linea.find(nombre_registro,0)!=string::npos){
                    viejo_numero = linea.substr(62,68);
                    cout<<"Su viejo número era: "<<viejo_numero<<endl;
                    cout<<"Cambio de número exitoso"<<endl;
                    string linea_nueva = linea.replace(linea.find(viejo_numero,0), viejo_numero.length(), nuevo_numero);
                    linea.replace(linea.find(nombre_registro, 0),linea_nueva.length(),linea_nueva);
                    informacionEntrada<<linea<<endl;
                }
                else{
                    //Se escribe de igual de forma lo que no se cambia
                    informacionEntrada<<linea<<endl;
                }
            }
            
        }


        informacionSalida.close();
        informacionEntrada.close();
        //Se elimina el txt original y se cambia de nombre el del temporal al nombre que tenía el documento original
        remove("Registro_usuarios.txt");
        rename("temporal.txt", "Registro_usuarios.txt");
    }
}
void borrarUsuarios(){
    //Se declaran las variables
    int opcion;
    string linea;
    string matricula;
    string nombre_persona;
    ifstream informacionSalida;
    ofstream informacionEntrada;



    cout<<endl;
    cout<<"******************"<<endl;
    cout<<"1) Borrar información de usuario"<<endl;
    cout<<"2) Borrar informacion de mascota"<<endl;
    cout<<"Teclee una opcion: ";
    cin>>opcion;
    if(opcion==1){
        cout<<endl;
        cin.ignore();
        cout<<"Teclee su nombre en el Registro: "<<endl;
        getline(cin,nombre_persona);
        cin.sync();
        informacionSalida.open("Registro_usuarios.txt",ios::in);
        informacionEntrada.open("temporal.txt",ios::out);
         if(informacionSalida.fail()){
            cout<< "Error de archivo" << endl;
        }
        else{
            //Se va iterando en el documento txt
            while(getline(informacionSalida,linea)){
                if(linea.find(nombre_persona,0)!=string::npos){
                    cout<<"Su usuario ha sido borrado"<<endl;
                }
                else{
                    informacionEntrada<<linea<<endl;
                }
            }

        }
        informacionSalida.close();
        informacionEntrada.close();
        //Se elimina el txt original y se cambia de nombre el del temporal al nombre que tenía el documento original
        remove("Registro_usuarios.txt");
        rename("temporal.txt", "Registro_usuarios.txt");
    }
    else if(opcion==2){
        cout<<endl;
        cin.ignore();
        cout<<"Tecle la matrícula de su mascota: ";
        getline(cin,matricula);
        cin.sync();
        informacionSalida.open("Registro_mascotas.txt",ios::in);
        informacionEntrada.open("temporal.txt",ios::out);
        if(informacionSalida.fail()){
            cout<<"Error al abrir archivo"<<endl;
        }
        else{
            while(getline(informacionSalida,linea)){
                if(linea.find(matricula,0)!=string::npos){
                    cout<<"Su mascota ha sido borrada de la base de datos"<<endl;
                }
                else{
                    informacionEntrada<<linea<<endl;
                }
            }
        }
        informacionSalida.close();
        informacionEntrada.close();
        //Se elimina el txt original y se cambia de nombre el del temporal al nombre que tenía el documento original
        remove("Registro_mascotas.txt");
        rename("temporal.txt", "Registro_mascotas.txt");


    }
    


}
//Función menú que va llamando a las otras funciones anteriores y las va llamando; en caso de ser necesario.
int menu(){
    int opcion;
    do{
    cout<<"-----MENÚ FYP-----"<<endl;
    cout<<"1) Registro de mascota"<<endl;
    cout<<"2) Registro de usuario"<<endl;
    cout<<"3) Ver mascotas desaparecidas"<<endl;
    cout<<"4) Cambio de informacion"<<endl;
    cout<<"5) Borrar usuario"<<endl;
    cout<<"6) Salir"<<endl;
    cout<<"-------------------"<<endl;
    cout<<"Entra tu opción: ";
    cin>>opcion;
    if(opcion==1){
        registroMascotas();
    }
    else if(opcion==2){
        registroUsuarios();
    }
    else if(opcion==3){
        mascotasDesaparecidas();
    }
    else if(opcion==4){
        MenucambioInformacion();
    }
    else if(opcion==5){
        borrarUsuarios();
    }
}while(opcion != 6);
    return 0;
}
