# Librerias
import json

from discord import Embed
from discord.ext import commands
from discord.ext.commands import cooldown, command, BucketType

# Funciones (async)
async def _get_Database_(): 
  with open('./commands/economycommands/DataBase/economia.json', 'r') as documento: 
    panas = json.load(documento)

    return panas

async def _update_DataBase_(nueva_base_de_datos):
  with open('./commands/economycommands/DataBase/economia.json', 'w') as documento: 
    json.dump(nueva_base_de_datos, documento)
    documento.close()

async def _update_Value(pana, typeOfValue, value): 
  panas = await _get_Database_()
  key = str(pana.id)

  if ( key in panas ): 
    panas[key][typeOfValue] += value
    panas[key]["total"] = panas[key]["cartera"] + panas[key]["banco"]
    
    # Updates the DataBase
    await _update_DataBase_(panas)

    return True
  else: 
    return False

# Clases para nuestras funciones, etc.
class BankAccount_Transactions(commands.Cog, name = "_create_account"): 
  def __init__(self, client): 
    self.client = client

  # Crear cuenta 
  @command( aliases = [ 'crearcuenta', 'crear-cuenta', 'abrir' ] )
  @cooldown( 1, 30, BucketType.user )
  async def _create_bank_account(self, ctx): 
    panas = await _get_Database_()
    key = str(ctx.author.id)

    if ( key in panas ): 
      embed_message = Embed(
        title = "Oopsie!",
        color = 0xff0000,
        description = "Se cayo el sistema joven, dice que usted es demasiado hermoso JAJSDNENW, no es cierto, pero ya no puedes tener mas cuentas pana! Trabaja y gana dinero, despues vienes y lo lavam- digo- lo ponemos en un lugar seguro. :)"
      )
      await ctx.channel.send( embed = embed_message )
    else:
      panas[key] = {}
      panas[key]["cartera"] = 0
      panas[key]["banco"] = 50
      panas[key]["total"] = 50

      embed_message = Embed(
        title = "Cuenta abierta en el PanaBanco!",
        color = 0x0a12ff,
        description = "Gracias por su preferencia al escoger PanaBanco sobre otros bancos! Aqui tiene 50$ iniciales en su cuenta d banco, puede retirarlos con el comando `retirar [cantidad]`! Para conseguir mas dinero puedes robar, asaltar o incluso hacerla d sicario, u otras, pero bueno esa es tu decision... :)"
      )
      embed_message.add_field(name="Tu moni:", value=f"{panas[key]['cartera']}$", inline=True)
      embed_message.add_field(name="Banco: ", value=f"{panas[key]['banco']}$", inline=True)
      embed_message.add_field(name="Total:", value=f"{panas[key]['total']}$", inline=True)
      await ctx.channel.send( embed = embed_message )

    # Añadimos las cosas a el documento
    with open('./commands/economycommands/DataBase/economia.json', 'w') as documento: 
      json.dump(panas, documento)
      documento.close()

# Funcion para añadir la "cog" a nuestro bot y asi poder tener los comandos, etc.
def setup(client): 
  client.add_cog(BankAccount_Transactions(client))