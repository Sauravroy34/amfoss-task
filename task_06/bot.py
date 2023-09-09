import discord 
import scraper
import os 
from discord.ext import commands
import csv
score = []
k= ""
#1149341988676718703
#bfc2f802febddcf5ad8eec0033b663a4ba51729a27cc02855a0d2d44652b0b62
#
token = os.getenv("SECRET_KEY")
Client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#bot is getting ready
@Client.event
async def on_ready():
    print("The bot is ready for use")
    print("------------")

@Client.command()
async def hello(ctx):
    await ctx.send(stuff.intro())


   



  

    
@Client.event
async def on_message(message):

  if message.content.startswith("!help"):
    await message.channel.send(stuff.intro())

  if message.content.startswith("!livescore"):

    
    score.append(stuff.check())

    for i in score:
    
        j = i.split("\n")
    str1 = ""
    j = str1.join(j)



    with open("score.csv","w+") as file:
          writer = csv.writer(file)
          writer.writerow((j.split()))

    await message.channel.send(stuff.check())
    

  
  if message.content.startswith("!csv"):
    
    




    await message.channel.send(file = discord.File("score.csv"))


          


        
Client.run(token)