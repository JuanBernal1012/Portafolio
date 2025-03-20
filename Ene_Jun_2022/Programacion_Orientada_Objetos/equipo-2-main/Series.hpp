#pragma once
#include "Video.hpp"
#include "Episode.hpp"


class Series : public Video { 
public:
    std::vector<Episode *> episodes;
    std::string calificacion;
public:
    Series();
    virtual ~Series();
    Series(std::string,std::string,std::string,std::string,std::string);    
    std::string Mostrar() override;    
    std::string GetCalificacion() override; 
    void SetCalificacion(std::string calificacion) override;
    void SetEpisode(Episode*);
    std::string ShowEpisodes(); 
    std::string GetID() override; 
    std::string Numerepisodios() override;

};