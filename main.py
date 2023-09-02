import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

token = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def get_result(query):
  app_id = os.environ['AppID']
  base_url = "http://api.wolframalpha.com/v1/result"
  params = {
      "i": query,
      "appid": app_id,
  }
    
  response = requests.get(base_url, params=params)
    
  if response.status_code == 200:
    try:
      return response.text
    except Exception as e:
      print(f"An unexpected error occurred: {e}")
      return f"Error: Received status code {response.status_code}"
  elif response.status_code == 501:
    return "The input value cannot be interpreted by the API."
  elif response.status_code == 400:
    return "The API did not find an input parameter while parsing."
  else:
    print(f"Received unexpected status code {response.status_code}: {response.text}")
    return f"Error: Received status code {response.status_code}"

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
        await message.channel.send(get_result(query))
        
keep_alive()

client.run(token)