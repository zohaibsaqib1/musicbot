import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)





client.run("ODk1ODc5OTgwMDYyNDc0Mjgx.YV-_Pw.y4b8EbLkTBNL_7toQZJF9ueYCHQ")
