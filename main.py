# El bot de los panas, creado por SharkyBoy#2024
# Es gratis, codigo abierto y pueden modificarlo si quieren, esto es lo basico.

# Requerimos las librerias que vamos a necesitar para nuestro bot
# en nuestro caso nosotros no necesitamos descargar nada mas, rpl.it
# hace eso por nostros. Si estas pensando en hacerlo en un IDE o editor
# de codigo diferente, recomendaria que descargaran las librerias
# necesarias, de lo contrario este no funcionara.
import discord, os, random, json
from discord.ext import commands # ext es un modulo que tiene mas modulos con mas funciones xd

# Las variables de entorno son variables que estan en el sistema operativo, si quisieras
# tener este bot para otro servidor pero osea, tu propio bot tendrias que crear
# un documento con terminacion .env sin nombre como se hace aqui.
bot_token = os.getenv('DISCORDBOT_SECRET_TOKEN')
bot_prefix = os.getenv('DISCORDBOT_PREFIX')

# Bot / cliente, este es el que requerimos y al final nos hereda 
# todos los metodos, eventos y demas para poder crear nuestro bot propio
client = commands.Bot(command_prefix = bot_prefix)

# Funciones para el bot que mas adelante van a ser usadas 
# para no tener q quebrarnos el cuello tan dificilmente
async def _update_values(user, newvalue = 0, lugar = "cartera", set = False):
  # Le di valores prederterminados, por ejemplo si "newvalue" no se indica simplemente
  # va a pasarse como 0 y basicamente no se va a añadir nada, igualmente con el "lugar"
  # si no se pasa nada, pasa a ser prederterminado como "cartera" siendo este el lugar
  # a modificar el valor, etc.

  valores = await _get_balance(user)

  # Ahora solamente podemos modificar / añadir u otro. 
  if set == False: 
    valores[lugar][lugar] += newvalue
  else: 
    valores[lugar] = newvalue

async def _get_balance(user): 
  with open('./DataBase/economia.json', 'r') as documento: 
    panas = json.load(documento)

    return panas[str(user.id)]

# Eventos del bot, como otros Game Engine u otros frameworks, etc
# hay eventos, que si se cumplen ciertos requisitos estos se "lanzan"
# y podemos manejar con ellos ciertas funcionalidades que queramos.
@client.event
async def on_ready():
  print('HORA D LEVANTARSE!')
  await client.change_presence(activity = discord.Game(name = "SOY DIOS ADMIRENME"))

@client.command( aliases = [ 'crearcuenta' ] )
async def _creacion_de_la_cuenta(ctx): 
  # Basicamente lo que estamos haciendo aqui es abrir el documento jason y declarar una variable
  # que lo "sostenga", yo use "documento" para una utilizacion mas facil. 
  with open("./DataBase/economia.json", 'r') as documento: 
    # Despues vamos a cargar el documento, esto nos devolvera la coleccin de lo q se almacena ahi
    panas = json.load(documento)

    # Ahora verificaremos que el pana no este en la base d datos, de lo contrario no haremos
    # nada especial
    if ( str(ctx.author.id) in panas ): 
      return False 
    else: 
      # Creamos una variable para el usiario / autor del mensaje
      user = ctx.author

      # Despues declaramos que la id d nuestro usuario sea una coleccion, este permitiendonos
      # almacenar muchas mas cosas 
      panas[str(user.id)] = {}
      
      # Despues insertamos lo que vendria siendo el valor "cartera" y el valor "banco" 
      panas[str(user.id)]["cartera"] = 0
      panas[str(user.id)]["banco"] = 0

  # Y ahora añadimos eso a nuestro documento json asi podemos crear una base d datos
  # que basicamente se "guarda" 
  with open("./DataBase/economia.json", 'w') as documento: 
    json.dump(panas, documento)

# Usamos el constructor "run" que basicamente mandara una señal a Discord para q empiece a correr
# nuestra aplicacion con el token especifico.
client.run(bot_token)