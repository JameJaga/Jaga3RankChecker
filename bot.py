import discord
import os
#Heroku.comのリンク用
TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()

levelup_guest = 0
levelup_regular = 0
levelup_bronze = 0
levelup_silver = 0
levelup_gold = 0
levelup_platinum = 0
levelup_diamond = 0
levelup_vip = 0
levelup_svup = 0
levelup_uvip = 0
levelup_mage = 0
levelup_god = 0

@client.event
async def on_ready():
    print('We have logged in as  {0.user}'.format(client))
    
@client.event
async def on_message(message):
    guild = message.guild
    #バグ修正>既に権限がアルかどうかで弾くプログラムの変数
    role_guest = discord.utils.get(guild.roles, name="Guest")
    levelup_guest = 0
    role_regular = discord.utils.get(guild.roles, name="Regular")
    levelup_regular = 1
    role_bronze = discord.utils.get(guild.roles, name="Bronze")
    levelup_bronze = 10
    role_silver = discord.utils.get(guild.roles, name="Silver")
    levelup_silver = 80
    role_gold = discord.utils.get(guild.roles, name="Gold")
    levelup_gold = 240
    role_platinum = discord.utils.get(guild.roles, name="Platinum")
    levelup_platinum = 500
    role_diamond = discord.utils.get(guild.roles, name="Diamond")
    levelup_diamond = 1000
    role_vip = discord.utils.get(guild.roles, name="VIP")
    levelup_vip = 2000
    role_svip = discord.utils.get(guild.roles, name="SuperVIP")
    levelup_svip = 5000
    role_uvip = discord.utils.get(guild.roles, name="UltraVIP")
    levelup_uvip = 10000
    role_mage = discord.utils.get(guild.roles, name="Mage")
    levelup_mage = 25000
    role_GOD = discord.utils.get(guild.roles, name="GOD")
    levelup_god = 50000

    if message.author.bot:
        return
    msg_count = 0
    rc = 0
    #/rcmeコマンド
    if message.content.startswith('/rcme'):
        await message.channel.send('Counting...PleaseWait.')
        member = message.author
        for channel in guild.text_channels:
            msgs = await channel.history(limit=None).flatten()
            msg_c = sum(msg.author == member for msg in msgs)
            msg_count = msg_c + msg_count
        rc = 1
         
    #/rcyouコマンド
    if message.content.startswith('/rcyou'):
        if message.author.guild_permissions.administrator:
            await message.channel.send('Counting...PleaseWait.')
            member = message.mentions[0]
            for channel in guild.text_channels:
                msgs = await channel.history(limit=None).flatten()
                msg_c = sum(msg.author == member for msg in msgs)
                msg_count = msg_c + msg_count
            rc = 1
        else:
            embed = discord.Embed(title="AccessDenied",description = 'You do not have permisson to use this command',color=discord.Colour.from_rgb(255, 0, 0))
            await message.channel.send(embed=embed)
    if rc == 1:
        if(msg_count >= levelup_god):
            nowrole = 'GOD'
            nextrole = '次のランクアップなし。'
            tonext = 0
        elif(msg_count >= levelup_mage):
            nowrole = 'Mage'
            nextrole = 'GOD'
            tonext = levelup_god - msg_count
        elif(msg_count >= levelup_uvip):
            nowrole = 'UltraVIP'
            nextrole = 'Mage'
            tonext = levelup_mage - msg_count
        elif(msg_count >= levelup_svip):
            nowrole = 'SuperVIP'
            nextrole = 'UltraVIP'
            tonext = levelup_uvip - msg_count
        elif(msg_count >= levelup_vip):
            nowrole = 'VIP'
            nextrole = 'SuperVIP'
            tonext = levelup_svip - msg_count
        elif(msg_count >= levelup_diamond):
            nowrole = 'Diamond'
            nextrole = 'VIP'
            tonext = levelup_vip - msg_count
        elif(msg_count >= levelup_platinum):
            nowrole = 'Platinum'
            nextrole = 'Diamond'
            tonext = levelup_diamond - msg_count
        elif(msg_count >= levelup_gold):
            nowrole = 'Gold'
            nextrole = 'Platinum'
            tonext = levelup_platinum - msg_count
        elif(msg_count >= levelup_silver):
            nowrole = 'Silver'
            nextrole = 'Gold'
            tonext = levelup_gold - msg_count
        elif(msg_count >= levelup_bronze):
            nowrole = 'Bronze'
            nextrole = 'Silver'
            tonext = levelup_silver - msg_count
        elif(msg_count >= levelup_regular):
            nowrole = 'Regular'
            nextrole = 'Bronze'
            tonext = levelup_bronze - msg_count
        elif(msg_count >= levelup_guest):
            nowrole = 'Guest'
            nextrole = 'Regular'
            tonext = levelup_regular - msg_count
        
        
        embed = discord.Embed(title="RemarkStatus",color=discord.Colour.from_rgb(0,191,255))
        embed.add_field(name="**YourRemark**",value=f'{member.mention} さんの現在の発言数は{str(msg_count)}です。',inline=False)
        embed.add_field(name="**Rank**",value=f'{member.mention} さんの現在のランクは{str(nowrole)}です。',inline=False)
        embed.add_field(name="**NextRank**",value=f'{member.mention} さんの次のランクは{str(nextrole)}です。',inline=False)
        embed.add_field(name="**HowFarToNextRank**",value=f'{member.mention} さんの次のランクまでに必要な発言数は{str(tonext)}です。',inline=False)  
        await message.channel.send(embed=embed)
    
    member = message.author
    msg_count = 0
    for channel in guild.text_channels:
        msgs = await channel.history(limit=None).flatten()
        msg_c = sum(msg.author == member for msg in msgs)
        msg_count = msg_c + msg_count
        print(msg_count)
    if(msg_count == levelup_regular):
        if role_regular in member.roles:
            role = discord.utils.get(guild.roles, name="Guest")
            await member.remove_roles(role)
            role = discord.utils.get(guild.roles, name="Regular")
            await member.add_roles(role)
            await message.channel.send(f'**おめでとうございます！！**\n {member.mention} さんは{str(role)}に昇格しました！:tada::tada:')
    if(msg_count == levelup_bronze):
        if role_regular in member.roles:
            role = discord.utils.get(guild.roles, name="Regular")
            await member.remove_roles(role)
            role = discord.utils.get(guild.roles, name="Bronze")
            await member.add_roles(role)
            await message.channel.send(f'**おめでとうございます！！**\n {member.mention} さんは{str(role)}に昇格しました！:tada::tada:')
    if(msg_count == levelup_silver):
        if role_regular in member.roles:
            role = discord.utils.get(guild.roles, name="Bronze")
            await member.remove_roles(role)
            role = discord.utils.get(guild.roles, name="Silver")
            await member.add_roles(role)
            await message.channel.send(f'**おめでとうございます！！**\n {member.mention} さんは{str(role)}に昇格しました！:tada::tada:')
    if(msg_count == levelup_gold):
        if role_regular in member.roles:
            role = discord.utils.get(guild.roles, name="Silver")
            await member.remove_roles(role)
            role = discord.utils.get(guild.roles, name="Gold")
            await member.add_roles(role)
            await message.channel.send(f'**おめでとうございます！！**\n {member.mention} さんは{str(role)}に昇格しました！:tada::tada:')
    if(msg_count == levelup_platinum):
        if role_regular in member.roles:
            role = discord.utils.get(guild.roles, name="Gold")
            await member.remove_roles(role)
            role = discord.utils.get(guild.roles, name="Platinum")
            await member.add_roles(role)
            await message.channel.send(f'**おめでとうございます！！**\n {member.mention} さんは{str(role)}に昇格しました！:tada::tada:')
    if(msg_count == levelup_diamond):
        if role_regular in member.roles:
            role = discord.utils.get(guild.roles, name="Platinum")
            await member.remove_roles(role)
            role = discord.utils.get(guild.roles, name="Diamond")
            await member.add_roles(role)
            await message.channel.send(f'**おめでとうございます！！**\n {member.mention} さんは{str(role)}に昇格しました！:tada::tada:')    
    if(msg_count == levelup_vip):
        if role_regular in member.roles:
            role = discord.utils.get(guild.roles, name="Diamond")
            await member.remove_roles(role)
            role = discord.utils.get(guild.roles, name="VIP")
            await member.add_roles(role)
            await message.channel.send(f'**おめでとうございます！！**\n {member.mention} さんは{str(role)}に昇格しました！:tada::tada:')
    if(msg_count == levelup_svip):
        if role_regular in member.roles:
            role = discord.utils.get(guild.roles, name="VIP")
            await member.remove_roles(role)
            role = discord.utils.get(guild.roles, name="SuperVIP")
            await member.add_roles(role)
            await message.channel.send(f'**おめでとうございます！！**\n {member.mention} さんは{str(role)}に昇格しました！:tada::tada:')
    if(msg_count == levelup_uvip):
        if role_regular in member.roles:
            role = discord.utils.get(guild.roles, name="SuperVIP")
            await member.remove_roles(role)
            role = discord.utils.get(guild.roles, name="UltraVIP")
            await member.add_roles(role)
            await message.channel.send(f'**おめでとうございます！！**\n {member.mention} さんは{str(role)}に昇格しました！:tada::tada:')
    if(msg_count == levelup_mage):
        if role_regular in member.roles:
            role = discord.utils.get(guild.roles, name="UltraVIP")
            await member.remove_roles(role)
            role = discord.utils.get(guild.roles, name="Mage")
            await member.add_roles(role)
            await message.channel.send(f'**おめでとうございます！！**\n {member.mention} さんは{str(role)}に昇格しました！:tada::tada:')
    if(msg_count == levelup_god):
        if role_regular in member.roles:
            role = discord.utils.get(guild.roles, name="Mage")
            await member.remove_roles(role)
            role = discord.utils.get(guild.roles, name="GOD")
            await member.add_roles(role)
            await message.channel.send(f'**おめでとうございます！！**\n {member.mention} さんは{str(role)}に昇格しました！:tada::tada:')

client.run('Njc3MDYyODM4MjgzNDAzMjY0.XkZb_g.PiPVL40RHLQi8B4uDRowkYxJm-g')
