import discord
import os
from io import BytesIO
from replit import db
from keep_alive import keep_alive
from get_result import get_result
from result_to_latex import result_to_latex
from latex_to_image import latex_to_image

token = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('!start'):
    db["responding"] = True
    await message.channel.send("Welcome to Wolfram Alpha Bot! If you have a query, please write !solve followed by a space and your query.")

  if msg.startswith('!stop'):
    db["responding"] = False
    await message.channel.send("Bot has been turned off. Please write !start if you want to turn me back on.")
  
  if db["responding"]:
      if msg.startswith('!solve'):
        query = msg.split("!solve ", 1)[1]
        print(f"Query to be solved: {query}")
        result = get_result(query)
        if db["Proper Result"] == True:
          latex_code = result_to_latex(result)
          image_data = latex_to_image(latex_code)
          await message.channel.send(file=discord.File(fp=BytesIO(image_data), filename='image.png'))
        else:
          await message.channel.send(result)
        
keep_alive()

client.run(token)