#pragma once
#include "Video.hpp"
#include <vector>

class Movie : public Video { 
private:    
    std::vector<int> calificaciones;
    std::string calificacion;
public:
    Movie();
    virtual ~Movie();
    Movie(std::string,std::string,std::string,std::string,std::string);
    std::string Mostrar() override; 
    std::string GetCalificacion() override; 
    void SetCalificacion(std::string score) override;
    std::string GetID() override;
    std::string Numerepisodios() override;

};
