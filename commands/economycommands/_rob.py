# Librerias
import random, json, sys

# For import stuff 
sys.path.append("./commands/economycommands")

from discord.ext import commands
from discord.ext.commands import cooldown, command, BucketType
from discord import Embed

# Funciones importadas
from _create_account import _update_Value

# Funciones
async def _Get_Random_String(): 
  with open("./commands/economycommands/Strings/Rob_Strings.json", 'r') as documento: 
    return json.load(documento)[str(random.randrange(1, 8))]

# Clase
class Rob_Handler(commands.Cog, name = '_rob'): 
  def __init__(self, client): 
    self.client = client

  # Comando robar
  @command(aliases = [ 'robar' ])
  @cooldown(1, 15, BucketType.user)
  async def _Rob_Something_Random(self, ctx): 
    first_random = random.randrange(100, 200)
    second_random = random.randrange(first_random, 250)
    
    # Actualizamos el valor de la persona (que luego automaticamente este se actualizara en el documento)
    thereis = await _update_Value(ctx.author, "cartera", second_random)
    string = await _Get_Random_String() + str(second_random) + "!"

    user_name = ctx.author.name + '#' + ctx.author.discriminator

    if thereis == True: 
      my_embed = Embed(color = 0x16dac3, description = string)
      my_embed.set_author(name = user_name, icon_url = ctx.author.avatar_url)
      my_embed.set_footer(text = "Robar es malo niños, no lo hagan esto es solo un juego!")
      await ctx.channel.send( embed = my_embed )
    else: 
      return

  # Error handler
  @_Rob_Something_Random.error
  async def info_error(self, ctx, error): 
    if isinstance(error, commands.CommandOnCooldown):
        my_embed = Embed(color = 0xff0000, description = f"Pana que paso? No puedes usar ese comando otra vez hasta dentro de {round(error.retry_after)} segundos.")
        await ctx.channel.send( embed = my_embed )

def setup(client): 
  client.add_cog(Rob_Handler(client))