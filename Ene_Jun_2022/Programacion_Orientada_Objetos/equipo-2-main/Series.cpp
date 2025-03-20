#include "Series.hpp"
#include "Episode.hpp"
#include <iostream>
#include <string>

Series::Series()
{
    this-> ID="S-0001";
    this-> nombre="Serie X";
    this-> duracion="90min";
    this-> genero="misterio";
    this-> calificacion= "5";
}

Series::~Series()
{

}

Series::Series(std::string pID,std::string pnombre,std::string pduracion,std::string pgenero, std::string ccalificacion) 
{
    this-> ID=pID;
    this-> nombre=pnombre;
    this-> duracion=pduracion;
    this-> genero=pgenero;
    this-> calificacion = ccalificacion;
}
std::string Series::Mostrar()
{       
    return "ID serie: " + ID + " Series: " + nombre + " Length: " + duracion + " Genre: " + genero + " Score: " + calificacion + "\n" ; 
}

std::string Series::GetID(){
    return this->ID;
}
std::string Series::GetCalificacion()
{  
    return this -> calificacion;
}

void Series::SetCalificacion(std::string score)
{
    this-> calificacion = score;
}

void Series::SetEpisode(Episode *enew){
    episodes.push_back(enew);
}

std::string Series::ShowEpisodes()
{    
    std::string ShowE{""};
    for(auto i=0;i<episodes.size();i++){
        ShowE += episodes[i]->Show() + "\n";
    }
    return ShowE;
}

std::string Series::Numerepisodios(){
    return std::to_string(episodes.size());
}
