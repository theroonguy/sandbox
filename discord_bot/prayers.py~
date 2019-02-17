import discord
from discord.ext import commands
import pprint
import requests
    

TOKEN = 'NTQ2NDkyNTYxMDQ1NDU0ODY4.D0pA0A.P7oXTCDd8ZNUtWxOyRlwbnZIpfI'


client = commands.Bot(command_prefix = 'z-')


@client.event
async def on_ready():
    print('Awaiting your command')
      
@client.command()
async def pray(*args):
    output = ''
    for word in args:
        output += word

    url = 'http://iphone.halalfire.com/bot_prayerspace.php?l={}&uuid=1&key=O2A8Uo5ACzEXW7NnPYPX'.format(output)
    res = requests.get(url)
    data = res.json()

    status_text = data['data']['status_text']
    photo = data['data']['photo_url']
    name = data['data']['name']
    placetype = data['data']['type']
    address = data['data']['address']
    city = data['data']['city']
    state = data['data']['state']
    zipcode = data['data']['zip']
    phone = data['data']['phone']
    distance = data['data']['distance']
    desc = data['data']['desc']
    zabiha_url = data['data']['url']

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.add_field(name='{} {}'.format(status_text, distance), value=desc, inline=True)
    embed.add_field(name=name,value='{}\n{} {} {} \n{}'.format(address, city, state, zipcode, phone),inline=False)
    embed.set_footer(text='Check out {} for more info'.format(zabiha_url))
    embed.set_image(url=photo)

    await client.say(embed=embed)


@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

client.run(TOKEN)
