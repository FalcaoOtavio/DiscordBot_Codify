import discord
import os
from API import token

token = token
client = discord.Client(intents=discord.Intents.all())

print("Bot Iniciado!")

# Função para codificar a mensagem
def encode(message):
  mensagem_codificada = message.content.replace('!codify ', '').encode('utf-8').hex()
  return mensagem_codificada

# Função para decodificar a mensagem
def decode(message):
  mensagem_decodificada = bytes.fromhex(message.replace('!decodify ', '')).decode('utf-8')
  return mensagem_decodificada

# Função para enviar a mensagem codificada no canal
async def send_message_encoded(message):
  mensagem_codificada = encode(message)
  await message.delete()  # Apaga a mensagem original
  await message.channel.send(mensagem_codificada)

# Função para enviar a mensagem decodificada no privado da pessoa
async def send_message_decoded(user, message):
  mensagem_decodificada = decode(message.content)
  await user.send(mensagem_decodificada)

# Função para ouvir os eventos do Discord
@client.event
async def on_message(message):
  # Verifica se a mensagem começa com !codify
  if message.content.startswith("!codify"):
    await send_message_encoded(message)

  # Verifica se a mensagem começa com !decodify
  elif message.content.startswith("!decodify"):
    await send_message_decoded(user=message.author, message=message)

# Inicia o bot
client.run(token)
