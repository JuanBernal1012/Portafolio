#include <stdexcept>
#include <vector>
#include <iostream>
#include <cstring>  
#include "Series.hpp"
#include "Video.hpp"
#include "Movie.hpp"
#include "App.hpp"

#include "Episode.hpp"
#include <fstream>
#include <string>  
#include <charconv>
#include <set>
#define maiterator 10
using namespace std;
int variable {0};  
string stringe[maiterator]; 
App::App(){
}
App::~App(){
}
void App::SetVideo(Video *vnew)
{
    this->videos.push_back(vnew);
}
int len(string swings)  
{  
    int length = 0;  
    for (int i = 0; swings[i] != '\0'; i++)  
    {  
        length++;            
    }  
    return length;     
}  
int App::Menu()
{

    std::cout<<"\n";
    std::cout<<"MENÚ \n";
    std::cout<<"1: cargar archivo de datos\n";
    std::cout<<"2: mostrar los videos en general con una cierta calificación o de un cierto género.\n";
    std::cout<<"3: mostrar los episodios de una determinada serie con una calificacion determinada.\n";
    std::cout<<"4: mostrar las películas con cierta calificación.\n";
    std::cout<<"5: calificar un video."<<"\n";
    std::cout<<"6: mostrar videos de la app."<<"\n";
    std::cout<<"7: mostrar películas de la app."<<"\n";
    std::cout<<"0: salir\n";
    MostrarErr(); 
    return variable;
}
void App::MostrarErr(){
    try{
        std::cin>>variable;
        if(variable > 7||variable < 0){
            std::string msjegrl { std::to_string(variable) + " no es una variable del menú disponible."};
            throw std::invalid_argument(msjegrl);
        }
    }
    catch(std::invalid_argument &e){
        std::cerr << "Ocurrió algo inesperado: " << e.what() << "\n";

    }
}
void split (string swings, char splitter)  
{  
    int iterator;
    iterator=0;
    for (iterator=0;iterator<=9;iterator++)
    {
        stringe[iterator]="";
    }
    int indiceactual= 0, i = 0;  
    int indiceinicia = 0,terminaindice = 0;  
    while (i <= len(swings))  
    {  
        if (swings[i] == splitter || i == len(swings))  
        {  terminaindice = i;  
            string subStr = "";  
            subStr.append(swings, indiceinicia, terminaindice - indiceinicia);  
            stringe[indiceactual] = subStr;  
            indiceactual += 1;  
            indiceinicia = terminaindice + 1;  
        }  i++;}}  
std::string App::ShowVideos(){
    std::string m{""};
    for(auto i=0;i<videos.size();i++){m += videos[i]->Mostrar() + "\n";}return m;}
void App::Archivo(std::string file)
{
    std::ifstream archivo(file);
    std::string Videodeserie;
    std::string IDms;
    std::string Nombrems;
    std::string Duracionms;
    std::string Genrems;
    std::string califnumms;
    std::string NombreEps;
    std::string Temporadass;
    std::string Califs;
    char splitters = '|';
    Series *lastSerie;
    std::set<std::string >conjunto;

    while (getline(archivo, Videodeserie))
    {             
        split(Videodeserie, splitters);  
        IDms= stringe[0];
        Nombrems= stringe[1]; 
        Duracionms= stringe[2];
        Genrems= stringe[3];
        califnumms= stringe[4];
        NombreEps= stringe[5];
        Temporadass= stringe[6];
        Califs= stringe[7];

        if (NombreEps == ""){
            Movie *movie = new Movie(IDms,Nombrems,Duracionms,Genrems,califnumms);
            videos.push_back(movie);
        } else{
            const bool is_in = conjunto.find(IDms) != conjunto.end();
            if(!is_in){
                Series *serie = new Series(IDms,Nombrems,Duracionms,Genrems,califnumms); 
                conjunto.insert(IDms);
                videos.push_back(serie); }
            Series* lastSerie = dynamic_cast<Series*>(videos[videos.size()-1]);
            Episode *episodio = new Episode(Temporadass,califnumms,NombreEps,Califs);
            lastSerie->SetEpisode(episodio);
             }}}
bool App::MenuOpcionyGenero(){
    std::cout<<"1: mostrar con base a calificaciones." << "\n";
    std::cout<<"2: mostrar con base a géneros." << "\n";
    std::cout<<"3: regresar." << "\n";
    int variable = 0;
    std::string califes {""};
    std::cin>>variable;
    std::string genree {""};
    if (variable == 1)
    {std::cout<<"Establezca una calificación: " ;
        std::cin>>califes; 
        VideoporCalificacion(califes);
        return true;
    }
    else if (variable == 2)
    {std::cout<<"Establezca un género: ";
        std::cin>>genree;
        VideoporGenero(genree);
        return true;
    }
    else if (variable == 3)
    {return true;}
    else
    { std::cout<<"Selección es inválida...";
        return false;
    }
    return false;   
}
void App::VideoporCalificacion(std::string variable) 
{
for (int i = 0; i < videos.size() ; i++)
{if (videos[i]->GetCalificacion() == variable){std::cout<<videos[i]->Mostrar() << "\n";}  }    
}
void App::VideoporGenero(std::string variable)
{
    for (int i = 0; i <= videos.size() - 1; i++)
    {
        if (videos[i]->genero == variable)
        {
            std::cout<<videos[i]->Mostrar();
        }
    }
}


void App::EpisodioporCalificacion(string IDtch, string Califtch)
{
    for (int i = 0; i < videos.size() ; i++){
       if (videos[i]->GetID() == IDtch){
        Series* s = dynamic_cast<Series*>(videos[i]);
            for(auto j = 0; j < s->episodes.size() ;j++){
                
                if (s->episodes[j]->GetCalificacion() == Califtch){
                    std::cout << s->episodes[j]->Show() << "\n";
                }
            }
        }
    }
}
bool App::PeliculasPorCalificacionMENU(){
    std::string MPC;
    std::cout << "Calificación de las películas: "; 
    std::cin >> MPC;
    PeliculasPorCalificacion(MPC);
    return true; 
}


void App::PeliculasPorCalificacion(std::string posselection)
{
    for (int i = 0; i < videos.size(); i++)
    {
        if (videos[i]->Numerepisodios() == "0" && videos[i]->GetCalificacion() == posselection)
        {
            std::cout<<videos[i]->Mostrar();
        }
    }
}


bool App::MenuVideoCalificacion(){
    std::string vids;
    std::cout<<"Otorgue el ID del video: ";
    std::cin>>vids;
    std::string posselection;
    std::cout<<"Otorgue la calificación: ";
    std::cin>>posselection;
    SetVideoCalificacion(vids,posselection);
    std::cout<<"Acción realizada con éxito.";
    return true;    

}

void App::SetVideoCalificacion(std::string IDtch, std::string Califtch)
{
    for (int i = 0; i < videos.size() ; i++)
    {
        if (videos[i]->GetID() == IDtch)
        {
            videos[i]->SetCalificacion(Califtch);
            std::cout << videos[i]->Mostrar() << "\n";
        }
    }
     
}
void App::All(){
for(auto i = 0 ;i < videos.size() ; i++){std::cout << videos[i]->Mostrar(); }}
std::ostream& operator<<(std::ostream& output,Movie *newmovie )
{   
    output << newmovie->Mostrar();
    return output;
}
void App::ShowM(){
    for(auto i = 0 ;i < videos.size() ; i++){if (videos[i]->Numerepisodios() == "0"){
            Movie* moviesendl = dynamic_cast<Movie*>(videos[i]);
            std::cout << moviesendl;           
        }}}
