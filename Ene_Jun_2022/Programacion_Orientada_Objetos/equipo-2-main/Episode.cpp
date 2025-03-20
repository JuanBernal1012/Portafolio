#include "Episode.hpp"
#include <iostream>
#include <vector>
#include <string>

Episode::Episode()
{
    this-> titulo="xd";
    this-> temporada="1";
    this-> episode="01";
    this-> calificacion="5";
}

Episode::Episode(std::string ptemporada,std::string pepisode,std::string ptitulo, std::string calificacion)
{    
    this-> titulo = ptitulo;
    this-> temporada = ptemporada;
    this-> episode = pepisode;
    this-> calificacion=calificacion;
}

std::string Episode::GetCalificacion()
{    
    return calificacion;
}

void Episode::SetCalificacion(int calificacion)
{

}

std::string Episode::Show(){

    return "Episode: " +episode+" Title: "+ titulo + " Season: " + temporada + " Score: " + calificacion;    
}