import discord
import os
#Heroku.comのリンク用
TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as  {0.user}'.format(client))
    
@client.event
async def on_message(message):
    guild = message.guild
    member = message.author
    msg_count = 0
    msgs = await member.history(limit=None).flatten()
    msg_count += len(msgs)
    if message.author.bot:
        return
    if message.content.startwith(/rcme):
        if(msgs >= 10):
            role = discord.utils.find(lambda r: r.name == 'Member', member.guild.roles)
            await member.add_roles(role)
        if(msgs >= 1000):
            role = discord.utils.find(lambda r: r.name == 'VIP', member.guild.roles)
            await member.add_roles(role)
    if message.content.startwith(/rcyou):
        if message.author.guild_permissions.administrator:
            member = message.mentions[0]
            if(msgs >= 10):
                role = discord.utils.find(lambda r: r.name == 'Member', member.guild.roles)
                await member.add_roles(role)
            if(msgs >= 1000):
                role = discord.utils.find(lambda r: r.name == 'VIP', member.guild.roles)
                await member.add_roles(role)
        else:
            embed = discord.Embed(title="AccessDenied",description = 'You do not have permisson to use this command',color=discord.Colour.from_rgb(255, 0, 0))
            await message.channel.send(embed=embed)
client.run(TOKEN)
