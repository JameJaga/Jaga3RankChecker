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
    if message.author.bot:
        return
    #/rcコマンド
    if message.content.startswith('/rcme'):
        await message.channel.send('Counting...PleaseWait.')
        member = message.author
        msg_count = 0
        for channel in guild.text_channels:
            msgs = await channel.history().flatten()
            msg_count += sum(msg.author == member for msg in msgs)
        if(msg_count >= 1000):
            role = 'VIP'
            next_role = '<<次のランクアップはなし。>>'
        elif(msg_count >= 10):
            role = 'Member'
            next_role = 'VIP'
        else:
            role = '082'
            next_role = 'Member'
        embed = discord.Embed(title="RemarkStatus",color=discord.Colour.from_rgb(0,191,255))
        embed.add_field(name="**YourRemark**",value=f'{member.mention} さんの現在の発言数は{str(msg_count)}です。',inline=False)
        embed.add_field(name="**Rank**",value=f'{member.mention} さんの現在のランクは{str(role)}です。',inline=False)
        embed.add_field(name="**NextRank**",value=f'{member.mention} さんの次のランクは{str(next_role)}です。',inline=False)  
        await message.channel.send(embed=embed)
        
    #/rcyouコマンド
    if message.content.startswith('/rcyou'):
        if message.author.guild_permissions.administrator:
            await message.channel.send('Counting...PleaseWait.')
            member = message.mentions[0]
            msg_count = 0
            for channel in guild.text_channels:
                msgs = await channel.history().flatten()
                msg_count += sum(msg.author == member for msg in msgs)
            if(msg_count >= 1000):
                role = 'VIP'
                next_role = '<<次のランクアップはなし。>>'
            elif(msg_count >= 10):
                role = 'Member'
                next_role = 'VIP'
            else:
                role = '082'
                next_role = 'Member'
            embed = discord.Embed(title="RemarkStatus",color=discord.Colour.from_rgb(0,191,255))
            embed.add_field(name="**YourRemark**",value=f'{member.mention} さんの現在の発言数は{str(msg_count)}です。',inline=False)
            embed.add_field(name="**Rank**",value=f'{member.mention} さんの現在のランクは{str(role)}です。',inline=False)
            embed.add_field(name="**NextRank**",value=f'{member.mention} さんの次のランクは{str(next_role)}です。',inline=False)  
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="AccessDenied",description = 'You do not have permisson to use this command',color=discord.Colour.from_rgb(255, 0, 0))
            await message.channel.send(embed=embed)
            
    member = message.author
    msg_count = 0
    for channel in guild.text_channels:
        msgs = await channel.history().flatten()
        msg_count += sum(msg.author == member for msg in msgs)
    if(msg_count == 10):
        role = discord.utils.find(lambda r: r.name == '082', member.guild.roles)
        await member.remove_roles(role)
        role = discord.utils.find(lambda r: r.name == 'Member', member.guild.roles)
        await member.add_roles(role)
        await message.channel.send(f'**おめでとうございます！！**\n {member.mention} さんはMemberに昇格しました！:tada::tada:')
    if(msg_count == 1000):
        role = discord.utils.find(lambda r: r.name == 'Member', member.guild.roles)
        await member.remove_roles(role)
        role = discord.utils.find(lambda r: r.name == 'VIP', member.guild.roles)
        await member.add_roles(role)
        await message.channel.send(f'**おめでとうございます！！**\n {member.mention} さんはVIPに昇格しました！:tada::tada:')
client.run(TOKEN)
