#include <iostream>
#include <string>

using namespace std;
int operation1();
int operation11();
int operation2();
int operation22();

int operation1()
{
    int number,suma=0, cont;

    cout<<"Gimme number: ";
    cin>>number;
    for (cont=1;cont<=number;cont++)
    {
        suma=suma+cont;
    }
    cout<<"La suma es "<<suma<<endl;
    return suma;
}

int operation11()
{
     int number, producto=1, cont;

    cout<<"Gimme number: ";
    cin>>number;
    for (cont=1;cont<=number;cont++)
    {
        producto=producto*cont;
    }
    cout<<"El producto es "<<producto<<endl;
    return producto;
}

int operation2()
{
    int number1, number2, suma=0, cont;
    cout<<"Gimme number1 and number2 (separados por un espacio): ";
    cin>>number1>>number2;
    if (number1<number2)
        {
            for (cont=number1;cont<=number2;cont++)
            {
                suma=suma+cont;
            }
            cout<<"La suma es "<<suma<<endl;
        }
    else
    {
        cout<<"number1 debe ser menor a number2.";
    } 
    return suma;
}

int operation22()
{
    int number1, number2, producto=1, cont;
    cout<<"Gimme number1 and number2 (separados por un espacio): ";
    cin>>number1>>number2;
    if (number1<number2)
        {
            for (cont=number1;cont<=number2;cont++)
            {
                producto=producto*cont;
            }
            cout<<"El producto es "<<producto<<endl;
        }
    else
    {
        cout<<"number1 debe ser menor a number2.";
    } 
    return producto;
}

int main()
{
    int opc;

    cout<<"TECLEA 1 O 2 PARA EL TIPO DE OPERACIÓN: ";
    cin>>opc;

    if (opc==1)
    {
        operation1();
        operation11();
    }
    else if (opc==2)
    {
        operation2();
        operation22();
    }
}