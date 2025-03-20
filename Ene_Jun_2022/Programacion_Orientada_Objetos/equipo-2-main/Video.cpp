#include <iostream>
#include "Video.hpp"

Video::Video()
{
    this-> ID="01";
    this-> nombre="Rogelio";
    this-> duracion="8";
    this-> genero="drama";
}

Video::~Video()
{

}

Video::Video(std::string vID,std::string vNombre,std::string vDuracion,std::string vGenre) 
{
    this-> ID=vID;
    this-> nombre=vNombre;
    this-> duracion=vDuracion;
    this-> genero=vGenre;
}

std::string Video::Mostrar()
{
    return "ID: "+ ID + " Name: " + nombre + " Duration: " + duracion + " Genre: " + genero+ "\n";
}

std::string Video::GetCalificacion()
{
    return 0;
}

void Video::SetCalificacion(std::string score)
{
     
}
