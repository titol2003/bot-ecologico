
import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print("Bot conectado correctamente")
    print(bot.user)

@bot.command()
async def clasificar(ctx, objeto):
    objeto = objeto.lower()

    if objeto == "botella":
        await ctx.send("Si esta vacia y limpia, deposita la botella plastica en el contenedor blanco en Colombia.")
    elif objeto == "papel":
        await ctx.send("El papel limpio y seco puede ir en el contenedor blanco.")
    elif objeto == "comida":
        await ctx.send("Los restos de comida van en el contenedor verde donde exista separacion de organicos.")
    else:
        await ctx.send("Todavia no tengo informacion sobre ese objeto.")


token = os.getenv("DISCORD_TOKEN")

if not token:
    raise RuntimeError("Falta configurar DISCORD_TOKEN")

bot.run(token)


