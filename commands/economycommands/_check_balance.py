# Librerias
import sys

# For import stuff 
sys.path.append("./commands/economycommands")

from discord.ext import commands
from discord.ext.commands import cooldown, command, BucketType
from discord import Embed

# Funciones importadas
from _create_account import _get_Database_

# Clase
class _Check_Balance(commands.Cog, name = '_check_balance'): 
  def __init__(self, client): 
    self.client = client

  @command(aliases = ['b', 'cuenta'])
  @cooldown(1, 10, BucketType.user)
  async def _check_balance_of_user(self, ctx): 
    panas = await _get_Database_()
    pana = panas[str(ctx.author.id)]

    if pana: 
      mensaje_embed = Embed(color = 0x0a12ff, title = "Esta es tu cuenta pana!", description = "Si quieres mas dinero puedes usar los comandos para empezar a generar ingreso, para despues, poder comprar cosas exclusivas en la tienda!")
      mensaje_embed.add_field(name="Tu moni:", value = str(pana["cartera"]) + "$", inline=True)
      mensaje_embed.add_field(name="En el banco:", value = str(pana["banco"]) + "$", inline=True)
      mensaje_embed.add_field(name="Total: ", value = str(pana["total"]) + "$", inline=True)

      await ctx.channel.send( embed = mensaje_embed )

  # Error handler
  @_check_balance_of_user.error
  async def info_error(self, ctx, error): 
    if isinstance(error, commands.CommandOnCooldown):
        my_embed = Embed(color = 0xff0000, description = f"Pana que paso? No puedes usar ese comando otra vez hasta dentro de {round(error.retry_after)} segundos.")
        await ctx.channel.send( embed = my_embed )

def setup(client): 
  client.add_cog(_Check_Balance(client))