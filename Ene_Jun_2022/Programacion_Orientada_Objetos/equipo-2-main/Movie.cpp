#include "Movie.hpp"
#include <iostream>
#include <string>

Movie::Movie()
{
    this-> ID="S-0001";
    this-> nombre="Serie X";
    this-> duracion="90min";
    this-> genero="misterio";
    this-> calificacion= "5";
}

Movie::~Movie()
{
    
}
Movie::Movie(std::string mID,std::string mName,std::string mDuration,std::string mGenre, std::string calificacion) 
{
    this-> ID=mID;
    this-> calificacion=calificacion;
    this-> nombre=mName;
    this-> duracion=mDuration;
    this-> genero=mGenre;
}
std::string Movie::Mostrar()
{    
    return "ID movie: "+ID+" Movie: "+ nombre +" Duration: "+duracion +" Genre: "+ genero + " Score: " + calificacion + "\n";    
}
std::string Movie::GetCalificacion()
{    
    return this -> calificacion;
}

void Movie::SetCalificacion(std::string score)
{
    this -> calificacion = score;
}

std::string Movie::GetID(){
    return this->ID;
}

std::string Movie::Numerepisodios(){
    return "0";
}

