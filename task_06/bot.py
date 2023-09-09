import discord 
import scraper
from discord.ext import commands
import csv
score = []
k= ""

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


          


        
Client.run("MTE0OTM0MTk4ODY3NjcxODcwMw.Gr1xB4.0Y6Vwp4kpOBa4RJYG2edVwgy6RioToac2icOpQ")