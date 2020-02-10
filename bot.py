import discord
import os
#Heroku.comのリンク用
TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as  {0.user}'.format(client))
    
@client.event
msg_count = 0
async def on_message(message):
    guild = message.guild
    if message.author.bot:
        return
    #/rcmeコマンド
    if message.content.startswith('/rcme'):
        member = message.author
        for channel in guild.text_channels:
            msgs = await message.channel.history().flatten()
            msg_count = sum(msg.author == member for msg in msgs)
        if(msg_count >= 10):
            role = discord.utils.find(lambda r: r.name == '082', member.guild.roles)
            await member.remove_roles(role)
            role = discord.utils.find(lambda r: r.name == 'Member', member.guild.roles)
            await member.add_roles(role)
        if(msg_count >= 1000):
            role = discord.utils.find(lambda r: r.name == 'Member', member.guild.roles)
            await member.remove_roles(role)
            role = discord.utils.find(lambda r: r.name == 'VIP', member.guild.roles)
            await member.add_roles(role)
    #/rcyouコマンド
    if message.content.startswith('/rcyou'):
        if message.author.guild_permissions.administrator:
            member = message.mentions[0]
            for channel in guild.text_channels:
                msgs = await message.channel.history().flatten()
                msg_count = sum(msg.author == member for msg in msgs)
            if(msg_count >= 10):
                role = discord.utils.find(lambda r: r.name == '082', member.guild.roles)
                await member.remove_roles(role)
                role = discord.utils.find(lambda r: r.name == 'Member', member.guild.roles)
                await member.add_roles(role)
            if(msg_count >= 1000):
                role = discord.utils.find(lambda r: r.name == 'Member', member.guild.roles)
                await member.remove_roles(role)
                role = discord.utils.find(lambda r: r.name == 'VIP', member.guild.roles)
                await member.add_roles(role)
        else:
            embed = discord.Embed(title="AccessDenied",description = 'You do not have permisson to use this command',color=discord.Colour.from_rgb(255, 0, 0))
            await message.channel.send(embed=embed)
client.run(TOKEN)
