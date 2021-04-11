import cv2
import os
import pytesseract
import discord
from discord.ext import commands

TOKEN=os.environ["BOT_TOKEN"]

app = commands.Bot(command_prefix='!수')

@app.event
async def on_ready():
    print(app.user.name, 'has connected to Discord!')
    await app.change_presence(status=discord.Status.online, activity=None)
    print("ready")

@app.command()
async def 로(ctx, *, text):
    await ctx.send(text)

app.run(TOKEN)
