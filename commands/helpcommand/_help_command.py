# Librerias
from discord import Embed 
from discord.ext import commands 
from discord.ext.commands import command, cooldown, BucketType 

# Funciones
async def _check_type_of_help(string, ctx): 
  if string == "economia": 
    user_name = ctx.author.name + '#' + ctx.author.discriminator
    
    mensaje_embed = Embed(
        color = 0xf4ff5c
    )
    mensaje_embed.add_field(name = "pana abrir", value = "Este comando abrira una cuenta para tu dinero en el PanaBanco y podras empezar a ganar dinero!", inline = True)
    mensaje_embed.add_field(name = "pana b", value = "Este comando te mostrara tu dinero en el banco, en tu cartera y un total de todo eso sumado! Tiene cooldown de 10secs!", inline = True)
    mensaje_embed.add_field(name = "pana robar", value = "Este comando te permitira ganar una cantidad random por ciertas cosas que hagas, tiene un cooldown de 15sec!",inline = True)
    mensaje_embed.add_field(name = "pana sacar [monto]", value = "Este comando sacara el monto de dinero que especifiques, aunque tiene que ser mayor a 100$ para poder hacerlo, politica del banco. Tiene un cooldown de 8secs!", inline = True)
    mensaje_embed.add_field(name = "pana depositar [monto]", value = "Depositara el monto de dinero que especifiques en tu banco, asi, este no podra ser robado por otros jugadores! Tiene un cooldown de 12secs!", inline = True)
    mensaje_embed.set_author(name = user_name, icon_url = ctx.author.avatar_url)
    mensaje_embed.set_footer(text = "Este comando es solo para poder ver los diferentes comandos de ayuda que puedes usar en el sistema de economia!")

    await ctx.channel.send( embed = mensaje_embed )
  elif string == "desarrollo": 
    mensaje_embed = Embed(
        color = 0xf4ff5c,
        description = "Si quieres ver a PanaBot y como funciona puedes ir al siguiente link y leer README.md para mas informacion! Gracias por usar PanaBot y te deseo un buen dia."
    )
    mensaje_embed.add_field(name = "GitHub Repository", value = "Link: https://github.com/zey-creator/PanaBot")
    mensaje_embed.add_field(name = "Repl.it Repository", value = "Link: https://repl.it/@zeycreator/PanaBot")
    mensaje_embed.set_footer(text = "Gracias por ayudar al desarrollo, tkm mucho pana!")

    await ctx.channel.send( embed = mensaje_embed )

# Clases
class _help_command(commands.Cog, name = '_help_command'): 
  def __init__(self, client): 
    self.client = client 

  @command(aliases = ['ayuda', 'help', 'comandos'])
  @cooldown(1, 5, BucketType.user)
  async def _help_command_async(self, ctx, *, tipodeayuda = None): 
    if tipodeayuda: 
      await _check_type_of_help(tipodeayuda, ctx)
    else: 
      user_name = ctx.author.name + '#' + ctx.author.discriminator

      mensaje_embed = Embed(
        color = 0xf4ff5c, 
        description = "Ten en cuenta que los siguientes comandos estan en desarrollo y puedes experimentar una serie de bugs o errores en ellos, de ser posible y que pasara esto porfavor contactate con el desarrollador y dejaselo saber."
      )
      mensaje_embed.add_field(name = "pana ayuda economia", value = "Usa este comando para ver los comandos que estan disponibles para el sistema de economia de PanaBot!")
      mensaje_embed.set_author(name = user_name, icon_url = ctx.author.avatar_url)
      mensaje_embed.set_footer(text = "Este comando es solo para poder ver los diferentes comandos de ayuda que puedes usar!")

      await ctx.channel.send( embed = mensaje_embed )
  
  @_help_command_async.error
  async def _help_command_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown): 
        my_embed = Embed(color = 0xff0000, description = f"Pana que paso? No puedes usar ese comando otra vez hasta dentro de {round(error.retry_after)} segundos.")
        await ctx.channel.send( embed = my_embed ) 

def setup(client): 
  client.add_cog(_help_command(client))