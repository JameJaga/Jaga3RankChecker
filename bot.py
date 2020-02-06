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
	msg_count = 0
    if message.author.bot:
		
	if message.content.startwith(/rcme):
		member = message.author
		msgs = await member.history(limit=None).flatten()
		msg_count += len(msgs)
		if(msgs >= 10):
					
		if(msgs >= 1000):
		
    if message.content.startwith(/rcyou):
		if message.author.guild_permissions.administrator:
			member = message.mentions[0]
			msgs = await member.history(limit=None).flatten()
			msg_count += len(msgs)
			if(msgs >= 10):
				role = discord.utils.find(lambda r: r.name == 'Member', member.guild.roles)  
    			await member.add_roles(role)
			if(msgs >= 1000):
				role = discord.utils.find(lambda r: r.name == 'VIP', member.guild.roles)  
    			await member.add_roles(role)	
		else:
			embed = discord.Embed(title="AccessDenied",description = 'You do not have permisson to use this command',color=discord.Colour.from_rgb(255, 0, 0))
            await message.channel.send(embed=embed)
			if(msgs >= 10):
			    role = discord.utils.find(lambda r: r.name == 'Member', member.guild.roles)  
    		    await member.add_roles(role)
			if(msgs >= 1000):
			    role = discord.utils.find(lambda r: r.name == 'VIP', member.guild.roles)  
    		    await member.add_roles(role)
client.run(TOKEN)
