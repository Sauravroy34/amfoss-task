import discord 
import scraper
import os 
from discord.ext import commands
import csv
score = []
k= ""

token = os.getenv("SECRET_KEY")
Client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#bot is getting ready
@Client.event
async def on_ready():
    print("The bot is ready for use")
    print("------------")

@Client.command()
async def hello(ctx):
    await ctx.send(scraper.intro())


   



  

    
@Client.event
async def on_message(message):

  if message.content.startswith("!help"):
    await message.channel.send(scraper.intro())

  if message.content.startswith("!livescore"):

    
    score.append(scraper.check())

    for i in score:
    
        j = i.split("\n")
    str1 = ""
    j = str1.join(j)



    with open("score.csv","w+") as file:
          writer = csv.writer(file)
          writer.writerow((j.split()))

    await message.channel.send(scraper.check())
    

  
  if message.content.startswith("!csv"):
    
    




    await message.channel.send(file = discord.File("score.csv"))


          


        
Client.run(token)