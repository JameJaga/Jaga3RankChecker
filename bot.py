import discord
import os

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()
num = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    guild = message.guild
    if message.author.bot:
        return
  
  if message.content.startwith(/rankcheckme):
  
  if message.content.startwith(/rankcheckyou):
      if message.author.guild_permissions.administrator:
          
      

  
client.run(TOKEN)
