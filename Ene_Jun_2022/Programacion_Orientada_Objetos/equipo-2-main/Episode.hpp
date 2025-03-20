#pragma once 
#include <vector>
#include <string>

class Episode {
protected:
    std::string temporada;
    std::string episode;
    std::string titulo;
    std::vector<int> calificaciones;
    std::string calificacion;
public:
    Episode();
    Episode(std::string,std::string,std::string, std::string);
    std::string GetCalificacion();
    void SetCalificacion(int calificacion);
    std::string Show();
};