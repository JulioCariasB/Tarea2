# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"
image FreezerIntroduce = "FreezerIntroduce.png"
image VegetaLlega = "VegetaLlega.png"
image FreezerRie = "FreezerRie.png"
image VegetaAtaca = "VegetaAtaca.png"
image PlanetaFondo = "PlanetaFondo.png"
image VegetaFondo = "VegetaFondo.png"
image PeleaFreezerVegeta = "PeleaFreezerVegeta.png"
image AdiosVegeta = "AdiosVegeta.png"
image GokuLlego = "GokuLlego.png"
image FreezerAlAtaque = "FreezerAlAtaque.png"
image GokuAlAtaque = "GokuAlAtaque.png"
image FondoPeleaGoku = "FondoPeleaGoku.png"
image PeleaGokuFreezer = "PeleaGokuFreezer.png"
image GokuGano = "GokuGano.png"
image FondoPeleaFinal = "FondoPeleaFinal.png"
image movie = Movie(size=(320,240),xpos=475,ypos=50,xanchor=0,yanchor=0)
 

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el 
#   ejemplo.
define f = Character('Freezer', color="#c8ffc8")
define v = Character('Vegeta', color ="#c8ffc8")
define g = Character('Goku', color="#c8ffc8")


# The game starts here.
# - El juego comienza aquí.
label start:
$ renpy.movie_cutscene("intro.ogv")
scene PlanetaFondo with dissolve
show FreezerIntroduce with dissolve
play music "Goku.mp3"

f "Soy el emperador Freezer, ninguno de estos insectos podrá destruirme."

scene VegetaFondo with dissolve
show VegetaLlega with dissolve

v "Callate sambadija, Tu eres un guerrero de clase inferior... ¡¡Acabaré contigo Freezer!!"

scene PlanetaFondo with dissolve
show FreezerRie with dissolve

f "¿Tu me vencerás a mi Vegeta? Tienes buen sentido del humor, pero no buen cerebro."

scene VegetaFondo with dissolve
show VegetaAtaca with dissolve
v "Callate insolente, ahora conocerás al Principe de los Saiyayines!!"

show PeleaFreezerVegeta 

f "Debo reconocer que has mejorado tu nivel de pelea Vegeta."

show PeleaFreezerVegeta with dissolve

f "Pero te falta mucho para poder vencer AL EMPERADOR FREEZER!!"

scene PlanetaFondo with dissolve
show AdiosVegeta with dissolve

f "Hora de decir Adios Vegeta, creí que habría algún insecto capaz de derrotarme."
 
scene VegetaFondo with dissolve
show GokuLlego with dissolve

g "No tan rapido Freezer. La verdadera pelea es conmigo, no con el."

scene PlanetaFondo with dissolve
show FreezerAlAtaque with dissolve

f "Tú tambien crees que me vas a derrotar asqueroso gusano. Peliemos al máximo nivel."

scene VegetaFondo with dissolve 
show GokuAlAtaque with dissolve

g "Tú lo pediste Freezer. Pagarás por todas las personas inocentes que les hiciste daño."

scene FondoPeleaFinal with dissolve
show PeleaGokuFreezer with dissolve

g "Llegó tu fin Freezer!!"

scene FondoPeleaGoku with dissolve
show GokuGano with dissolve

g "Todo terminó. La paz ha vuelto."
$ renpy.movie_cutscene("dbz.ogv")
 
