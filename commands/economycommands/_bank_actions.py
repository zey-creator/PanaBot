# Librerias
import sys

# For import stuff 
sys.path.append("./commands/economycommands")

from discord.ext import commands
from discord.ext.commands import cooldown, command, BucketType
from discord import Embed

# Funciones importadas
from _create_account import _get_Database_, _update_DataBase_

# Clase
class _Withdraw_and_Deposit_(commands.Cog, name = '_bank_actions'): 
  def __init__(self, client): 
    self.client = client

  @command(aliases = ['w', 'sacar'])
  @cooldown(1, 8, BucketType.user)
  async def _withdraw_(self, ctx, *, monto): 
    if int(monto) < 100: 
      mensaje_embed = Embed(color = 0xff0000, description = "Pana no puedes sacar menos de 100$ del PanaBanco, lo siento pana pero es normativa del banco!")
      await ctx.channel.send( embed = mensaje_embed )
    else: 
      panas = await _get_Database_() 
      
      if ( str(ctx.author.id) in panas ): 
        if ( panas[str(ctx.author.id)]["banco"] >= int(monto) ):
          panas[str(ctx.author.id)]["banco"] -= int(monto)
          panas[str(ctx.author.id)]["cartera"] += int(monto)
          panas[str(ctx.author.id)]["total"] = panas[str(ctx.author.id)]["cartera"] + panas[str(ctx.author.id)]["banco"]

          await _update_DataBase_(panas)

          mensaje_embed1 = Embed(color = 0xff0000, description = "Acabas de sacar " + monto + "$ del PanaBanco! Ahora puedes usarlo para lo que sea que lo querias xd.")
          await ctx.channel.send( embed = mensaje_embed1 )    
        else: 
          mensaje_embed1 = Embed(color = 0xff0000, description = "No tienes esa cantidad pana! Por lo tanto no puedes retirar nada del banco.")
          await ctx.channel.send( embed = mensaje_embed1 )

          return
      else: 
        mensaje_embed2 = Embed(color = 0xff0000, description = "Debes de tener una cuenta en el PanaBanco antes de poder sacar cualquier cantidad de este! Crea una cuenta y despues ven cuando tengas algo de dinero.")
        await ctx.channel.send( embed = mensaje_embed2 )

        return

  @command(aliases = ['poner', 'depositar'])
  @cooldown(1, 12, BucketType.user)
  async def _deposit_(self, ctx, *, monto): 
    if int(monto) < 50: 
      mensaje_embed = Embed(color = 0xff0000, description = "No puedes depositar menos de 50$ en el banco, politica de usuarios.")
      await ctx.channel.send( embed = mensaje_embed )
    else: 
      panas = await _get_Database_() 
      
      if ( str(ctx.author.id) in panas ): 
        if ( panas[str(ctx.author.id)]["cartera"] >= int(monto) ):
          panas[str(ctx.author.id)]["cartera"] -= int(monto)
          panas[str(ctx.author.id)]["banco"] += int(monto)
          panas[str(ctx.author.id)]["total"] = panas[str(ctx.author.id)]["cartera"] + panas[str(ctx.author.id)]["banco"]

          await _update_DataBase_(panas)

          mensaje_embed1 = Embed(color = 0xff0000, description = "Acabas de depositar " + monto + "$ en tu cuenta bancaria de PanaBanco! Ahora estara guardado y no puede ser robado por otros jugadores, con cuidado!")
          await ctx.channel.send( embed = mensaje_embed1 )    
        else: 
          mensaje_embed1 = Embed(color = 0xff0000, description = "No tienes esa cantidad en tu cartera pana, consigue mas dinero y despues trata denuevo.")
          await ctx.channel.send( embed = mensaje_embed1 )

          return
      else: 
        mensaje_embed2 = Embed(color = 0xff0000, description = "Debes de tener una cuenta en el PanaBanco antes de poder depositar cualquier cantidad en este! Crea una cuenta y despues ven cuando tengas algo de dinero.")
        await ctx.channel.send( embed = mensaje_embed2 )

        return

  # Error handlers
  @_withdraw_.error
  async def _withdraw_error(self, ctx, error): 
    if ( isinstance(error, commands.CommandOnCooldown) ): 
      my_embed = Embed(color = 0xff0000, description = f"Pana que paso? No puedes usar ese comando otra vez hasta dentro de {round(error.retry_after)} segundos.")
      await ctx.channel.send( embed = my_embed )
    elif ( isinstance(error, commands.MissingRequiredArgument) ): 
      my_embed = Embed(color = 0xff0000, description = "Especifica una cantidad para sacar de tu cuenta bancaria, intenta denuevo en algunos segundos!")
      await ctx.channel.send( embed = my_embed )

  @_deposit_.error
  async def _deposit_error(self, ctx, error): 
    if ( isinstance(error, commands.CommandOnCooldown) ): 
      my_embed = Embed(color = 0xff0000, description = f"Pana que paso? No puedes usar ese comando otra vez hasta dentro de {round(error.retry_after)} segundos.")
      await ctx.channel.send( embed = my_embed )
    elif ( isinstance(error, commands.MissingRequiredArgument) ): 
      my_embed = Embed(color = 0xff0000, description = "Especifica una cantidad para depositar en tu cuenta bancaria y despues intenta de nuevo!")
      await ctx.channel.send( embed = my_embed )

def setup(client): 
  client.add_cog(_Withdraw_and_Deposit_(client))