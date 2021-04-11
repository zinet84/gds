import cv2
import os
import pytesseract
import discord
from discord import message
from discord.ext import commands

TOKEN=os.environ["BOT_TOKEN"]

app = commands.Bot(command_prefix='!수')

@app.event
async def on_ready():
    print(app.user.name, 'has connected to Discord!')
    await app.change_presence(status=discord.Status.online, activity=None)
    print("ready")

aaa = cv2.imread("https://cdn.discordapp.com/attachments/500371271314571266/830877235895861248/3.png")
print(f"image: {aaa}")

@app.command()
async def 로(ctx, *, text):
    await ctx.send(f"{ctx.message}\n\n{ctx.kwargs}")

app.run(TOKEN)
