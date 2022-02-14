import discord
import os
import random

import openai
from dotenv import load_dotenv


client = discord.Client()

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        if random.random() > 0.16:
            return
        response = openai.Completion.create(
  engine="text-davinci-001",
  prompt = message.content,
  temperature=0.5,
  max_tokens=60,
  top_p=0.3,
  frequency_penalty=1,
  presence_penalty=0.5
)
        return await message.channel.send(response.choices[0].text)

    elif message.content.startswith('Guys, meet Baljeet'):
        response = openai.Completion.create(
  engine="text-davinci-001",
  prompt = 'Introducing Baljeet, a sarcastic classmate of Sreehari',
  temperature=0.5,
  max_tokens=60,
  top_p=0.3,
  frequency_penalty=1,
  presence_penalty=0.5
)
        return await message.channel.send(response.choices[0].text)

    elif message.author.id == '589783387384840211':
        response = openai.Completion.create(
  engine="text-davinci-001",
  prompt = message.content,
  temperature=0.5,
  max_tokens=60,
  top_p=0.3,
  frequency_penalty=1,
  presence_penalty=0.5
)
        return await message.channel.send(response.choices[0].text)

    elif message.content.startswith('!b'):
        text = message.content[2:]
        response = openai.Completion.create(
  engine="text-davinci-001",
  prompt = text,
  temperature=0.5,
  max_tokens=60,
  top_p=0.3,
  frequency_penalty=1,
  presence_penalty=0.5
)
        return await message.channel.send(response.choices[0].text)
    
    else:
        if random.random() <= 0.5:
            return
        response = openai.Completion.create(
  engine="text-davinci-001",
  prompt = text,
  temperature=0.5,
  max_tokens=60,
  top_p=0.3,
  frequency_penalty=1,
  presence_penalty=0.5
)
        return await message.channel.send(response.choices[0].text)

TOKEN = os.getenv("TOKEN")
client.run(TOKEN)