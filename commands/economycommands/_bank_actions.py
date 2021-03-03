# Librerias
import discord, random, json

from discord import Embed
from discord.ext import commands
from discord.ext.commands import cooldown, command, BucketType

# Funciones (async)
async def _get_Database_(): 
  with open('./commands/economycommands/DataBase/economia.json', 'r') as documento: 
    panas = json.load(documento)

    return panas

# Clases para nuestras funciones, etc.
class BankAccount_Transactions(commands.Cog, name = "_bank_actions"): 
  def __init__(self, client): 
    self.client = client

  # Crear cuenta 
  @command( aliases = [ 'crearcuenta', 'crear-cuenta', 'abrir' ] )
  @cooldown( 1, 5, BucketType.user )
  async def _create_bank_account(self, ctx): 
    panas = await _get_Database_()
    key = str(ctx.author.id)

    if ( key in panas ): 
      return 
    else:
      panas[key] = {}
      panas[key]["cartera"] = 0
      panas[key]["banco"] = 0
      panas[key]["total"] = 0

    # Añadimos las cosas a el documento
    with open('./commands/economycommands/DataBase/economia.json', 'w') as documento: 
      json.dump(panas, documento)

# Funcion para añadir la "cog" a nuestro bot y asi poder tener los comandos, etc.
def setup(client): 
  client.add_cog(BankAccount_Transactions(client))