import discord
from discord.ext import commands
import random

TOKEN = "NTI0Mzc0OTM1MjgwNTQ5ODg5.DvnJ9A.N4Qb-0YDz3rBW0D4jmZQmm6z0hs"

client = commands.Bot(command_prefix = "-")

@client.event
async def on_ready():
    print("Bot is ready!")



@client.command()
async def anime():
    anime = random.randint(0, 3)
    if anime == 0:
        await client.say("https://gfycat.com/anxiousglossyalpinegoat")
    if anime == 1:
        await client.say("http://giphy.com/gifs/RH9JBI7pP0zM4")
    if anime == 2:
        await client.say("https://cdn.discordapp.com/attachments/516778897170366476/524390033759928375/image0.gif")
    if anime == 3:
        await client.say("https://giphy.com/gifs/Y01jP8QeLOox2")

@client.command()
async def cow():
    await client.say(":cow2:")

@client.command()
async def cookie():
    await client.say(":cookie:")
    
@client.command(pass_context=True)
async def clear(ctx, amount=5):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)


#HOMEWORK

@client.group(pass_context=True)
async def hw(ctx):
    if ctx.invoked_subcommand is None:
        await client.say("Please list a command.")

@hw.group()
async def add(*, message: str):
    global add_hw
    await add_hw(message)
    
@hw.command()
async def clear(amount=1):
    global hw
    del hw[amount-1]
    await hwlist()

hw0=1
async def add_hw(msg):
    global hw, hw0
    if hw0 == 1:
        hw=[]
        hw0=0
    hw.append(msg)
    print(hw)
    await hwlist()
    
@hw.command()
async def list():
    global num
    output = ' '
    num = 1
    for word in hw:
        output += str(num)
        output += '. '
        output += word
        output += ' \n'
        num += 1
        
    await client.say(output)

    
async def hwlist():
    global num
    output = ' '
    num = 1
    for word in hw:
        output += str(num)
        output += '. '
        output += word
        output += ' \n'
        num += 1
        
    await client.say(output)

@client.command()
async def echo(*, message: str):
    await client.say(message)
    
client.run(TOKEN)
                                                                                                                                                                                                                
