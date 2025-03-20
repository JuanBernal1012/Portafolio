#include <iostream>
#include "Episode.hpp"
#include "App.hpp"
#include "Video.hpp"
#include "Movie.hpp"
#include "Series.hpp"

int main()
{
        int opt;
        App a;
    do {
        opt = a.Menu(); 
        if (opt == 1){
            a.Archivo("input.txt");
            std::cout << "Se realizó la subida del archivo con éxito." << "\n";
        }
        if (opt == 2){
            bool continuar {false};
            do {
                continuar = a.MenuOpcionyGenero();
            }
            while(continuar == false);
        }
        if (opt == 3){
            std::string Califis,IDopt;
            std::cout << "Calificación de la serie: ";
            std::cin >> Califis;
            std::cout << "ID de la serie: " ;
            std::cin >> IDopt;
            a.EpisodioporCalificacion(IDopt,Califis);
        }

        if(opt == 4 ){bool continuar {false};
        do{
                continuar = a.PeliculasPorCalificacionMENU();
            }
            while(continuar == false);
        }
        if (opt == 5){
            bool continuar = false;
            do
            {
                continuar = a.MenuVideoCalificacion();
            } while (continuar == false);}
        if (opt == 6){a.All();}
        if(opt == 7){a.ShowM();}}
    while (opt !=0);
return 0;
}