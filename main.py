import cv2
import os
import pytesseract as pt
import discord
from discord import message, Attachment
from discord.ext import commands
import numpy as np
import requests

TOKEN=os.environ["BOT_TOKEN"]

app = commands.Bot(command_prefix='!')

@app.event
async def on_ready():
    print(app.user.name, 'has connected to Discord!')
    await app.change_presence(status=discord.Status.online, activity=None)
    print("ready")

@app.command()
async def 수로(ctx):
    url = ctx.message.attachments[0].url
    image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
    image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
    height, width, channels = image.shape
    scale=4
    image = cv2.resize(image,(int(width*scale),int(height*scale)))

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    image = cv2.dilate(image, kernel, anchor=(-1, -1), iterations=1)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    #cv2.imwrite("/mnt/c/Users/simdh/Documents/test.jpg", image)

    result = pt.image_to_string(image,lang='kor+eng')

    print("="*30)
    print(result)
    print("="*30)
    await ctx.send(result)

app.run(TOKEN)
