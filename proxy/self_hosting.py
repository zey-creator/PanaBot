from flask import Flask as flask
from threading import Thread

Aplicacion = flask('')

@Aplicacion.route('/')
def Inicio():
    return "Hola, esta es una pagina sencilla para mantener nuestro bot vivo y despierto!"

def CorrerAplicacion():
  Aplicacion.run(host='0.0.0.0',port=8080)

def Mantener_Despierto():
    thread = Thread(target = CorrerAplicacion)
    thread.start()