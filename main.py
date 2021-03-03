# El bot de los panas, creado por SharkyBoy#2024
# Es gratis, codigo abierto y pueden modificarlo si quieren, esto es lo basico.
# Toda la documentacion esta en el DOCUMENTACION.md. Mas informacion en el README.md

# Librerias
import discord, os, random, json
from discord.ext import commands 

# Variables de entorno
bot_token = os.getenv('DISCORDBOT_SECRET_TOKEN')
bot_prefix = os.getenv('DISCORDBOT_PREFIX')

# Bot / cliente, este es el que requerimos y al final nos hereda 
# todos los metodos, eventos y demas para poder crear nuestro bot propio
client = commands.Bot(command_prefix = bot_prefix)

# Cargamos las cogs / extensiones para poder llamar los comandos 
for forfolder in os.listdir('./commands'): 
  for filename in os.listdir(f'./commands/{forfolder}'):
    if filename.endswith('.py'): 
      client.load_extension(f'commands.{forfolder}.{filename[:-3]}')

# Caragamos ahora los eventos
for filename in os.listdir('./events'): 
  if filename.endswith('.py'): 
    client.load_extension(f'events.{filename[:-3]}')

# Usamos el constructor "run" que basicamente mandara una señal a Discord para q empiece a correr
# nuestra aplicacion con el token especifico.
client.run(bot_token)