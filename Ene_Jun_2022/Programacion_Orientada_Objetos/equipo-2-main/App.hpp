#pragma once
#include <vector>
#include <iostream>
#include "Series.hpp"
#include "Video.hpp"
#include "Movie.hpp"
class App {
public:
App();
~App();
void Appstart();
App(std::string);
int Menu();
std::vector<Video *> videos;
void SetVideo(Video *);
std::string ShowVideos();
void Archivo(std::string file);
bool MenuOpcionyGenero();
void VideoporCalificacion(std::string);
void VideoporGenero(std::string);
void EpisodioporCalificacion(std::string, std::string);
bool PeliculasPorCalificacionMENU();
void PeliculasPorCalificacion(std::string);
bool MenuVideoCalificacion();
void SetVideoCalificacion(std::string, std::string);
void All();
friend std::ostream& operator<<(std::ostream&,Movie& ); 
void ShowM();
void MostrarErr();
};