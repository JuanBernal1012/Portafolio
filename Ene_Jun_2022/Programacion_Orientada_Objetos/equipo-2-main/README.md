# Ejercicio - Calculadora aritmética Simple

## Descripción del Problema

Este ejercicio implementa una calculadora aritmética simple (suma, resta, multiplica, divide).

## Diagrama de Clases

```mermaid
classDiagram
      class App
      App --> Video
      Video <|-- Movie
      Video <|-- Series
      Series --> Episode

      App:+vector<Video*> videos
      App:+App()
      App:+~App()
      App:+App(string)
      App:+void Appstart()
      App:+int Menu()
      App:+void SetVideo(Video*)
      App:+string ShowVideos()
      App:+void Archivo(string file)
      App:+bool MenuOpcionesyGenero
      App:+void VideoporCalificacion(string)
      App:+void VideoporGenero(string)
      App:+void EpisodioporCalificacion(string, string)
      App:+bool PeliculasPorCalificacionMENU()
      App:+void PeliculasPorCalificacion(string)
      App:+bool MenuVideoCalificacion()
      App:+void SetVideoCalificacion(string, string)
      App:+void All()
      App:+void ShowM()
      App:+void MostrarErr()
      App:+friend ostream& operator<<(ostream&, Movie&)      
      
      class Video{
       <<abstract>>
       +string ID
       +string nombre
       +string duracion
       +string genero
       +Video()
       +virtual ~Video()
       +Video(string, string, string, string)
       +virtual string Mostrar()=0
       +virtual string GetCalificacion()=0
       +virtual void SetCalificacion(string score)=0
       +virtual string GetID()=0
       +virtual string Numerepisodios()=0
      }

      Movie: -vector<int> calificaciones
      Movie: -string calificacion
      Movie: +Movie()
      Movie: +virtual ~Movie()
      Movie: +Movie(string, string, string, string, string)
      Movie: +string Mostrar() override
      Movie: +string GetCalificacion() override
      Movie: +void SetCalificacion(string score) override
      Movie: +string GetID() override
      Movie: +string Numerepisodios() override
      
      Series: +vector<Episode*> episodes
      Series: +string calificacion
      Series: +Series()
      Series: +virtual ~Series()
      Series: +Series(string, string, string, string, string)
      Series: +string Mostrar() override
      Series: +string GetCalificacion() override
      Series: +void SetCalificacion(string califcacion) override
      Series: +void SetEpisode(Episode*)
      Series: +string ShowEpisodes()
      Series: +string GetID() override
      Series: +string Numerepisodios() override
      
      Episode: #vector<int> calificaciones
      Episode: #string calificacion
      Episode: #string temporada
      Episode: #string episode
      Episode: #string titulo
      Episode: +Episode()
      Episode: +Episode(string, string, string, string)
      Episode: +string GetCalificacion()
      Episode: +void SetCalificacion(int calificacion)
      Episode: +string Show()
```

## Objetivo

- Busca que el código pase correctamente todas las pruebas
   * Solamente cambia los archivos permitidos para lograr este objetivo (abajo se indican las reglas específicas)
   
- Las GitHub Actions deberán presentar una palomita en verde si se han satisfecho todas las pruebas, y una cruz roja cuando alguna (o todas) las pruebas han fallado.
   * **Recomendación:** Puedes dar clic en la cruz roja para verificar cual de las pruebas ha fallado (o si el código no ha compilado correctamente).
   * **Recomendación:** En caso de que el Autograding no muestre pruebas o no funcione, contacta a tu profesor mediante un issue.

## Instrucciones

- Deberás modificar los archivos (`.cpp` y `.hpp`) que consideres conveniente.

Explicación de los otros archivos:

- Archivo `test/tests.cpp` tiene las pruebas de esta actividad (NO LO CAMBIES!)
- Archivo `test/catch.hpp` tiene la biblioteca de pruebas  CATCH2 (NO LA CAMBIES!)
- Archivo `makefile` tienes los comandos para ejecutar la actividad (NO LO CAMBIES!)
- Archivo  `./build/appTests` se generará después de compilar (para **pruebas locales**, solo ejecútalo)

## Comandos para pruebas locales, ejecución y depuración

- Comando para construir y ejecutar pruebas: `make` o `make test`
    * Si el ejecutable ya está construido, sólo teclea : `./build/appTests`

- Comando para construir y ejecutar la aplicación: `make run` 
    * Si el ejecutable ya está construido, sólo teclea : `./build/exercise`

- Comando para depurar: `make debug`
    * Para conocer los comandos de depuración consulta:
     https://u.osu.edu/cstutorials/2018/09/28/how-to-debug-c-program-using-gdb-in-6-simple-steps/
     
- Comando para depurar con `vsCode` en `GitPod`: `make debugvs` 
    * Utilizar el depurador de la IDE. 

## Notas

- El código será evaluado solamente si compila.
   * La razón de esto es, si no compila no es posible generar el ejecutable y realizar las pruebas.

- Algunos casos de prueba podrían recibir calificación individual, otros podrían recibir calificación y si pasan todos juntos (o todas las pruebas en conjunto).

- La calificación final se otorgará de manera automática en cada *commit*, y se evaluará solamente hasta la fecha limite de la actividad.

Para dudas adicionales, consulta a tu profesor.

## License

MIT License 2020
