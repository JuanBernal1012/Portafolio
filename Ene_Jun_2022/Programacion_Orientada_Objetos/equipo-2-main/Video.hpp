#pragma once
#include <string>
#include <vector>

//Todo video tiene un ID, un nombre, una duración y un género (drama, acción, misterio).
class Video {
    
public:
    std::string ID;
    std::string nombre;
    std::string duracion;
    std::string genero;

public:
    Video();
    virtual ~Video();
    Video(std::string,std::string,std::string,std::string);
    virtual std::string Mostrar()=0;
    virtual std::string GetCalificacion()=0;
    virtual void SetCalificacion(std::string score)=0;
    virtual std::string GetID()=0;
    virtual std::string Numerepisodios()=0;
};