# Librerias
import discord
from discord.ext import commands

# Clases para nuestras funciones, etc.
class On_ready_event_handler(commands.Cog): 
  def __init__(self, client): 
    self.client = client

  # Registramos lo que vendria siendo ese evento 
  @commands.Cog.listener()
  async def on_ready(self): 
    # Ponemos un mensaje en nuestra consola y despues cambiamos la actividad del bot
    print( 'Listo para sobrevivir con los animales!' )

    await self.client.change_presence(activity = discord.Game(name = "Hola panas soy un bot inservible por el momento jiji."))

def setup(client): 
  client.add_cog(On_ready_event_handler(client))