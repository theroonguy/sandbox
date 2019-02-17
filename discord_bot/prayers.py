import discord
from discord.ext import commands
import pprint
import requests
    

TOKEN = 'NTQzOTUzNDM2NTUxNDEzNzcw.D0EFWQ.koaPnK_GT59KJtfKqP4Xis2CqKI'

client = commands.Bot(command_prefix = 'p/')


@client.event
async def on_ready():
    print('Awaiting your command')
      
@client.command()
async def w(*args):
    output = ''
    for word in args:
        output += word

    url = 'http://iphone.halalfire.com/salatomatic_1.php?l={}&uuid=1&key=O2A8Uo5ACzEXW7NnPYPX'.format(output)
    res = requests.get(url)
    data = res.json()

    await client.say(data['data']['status_text']+'\n')

    name = data['data']['name']
    placetype = data['data']['type']
    address = data['data']['address']
    city = data['data']['city']
    state = data['data']['state']
    zipcode = data['data']['zip']
    phone = data['data']['phone']
    distance = data['data']['distance']

    await client.say(data['data']['photo_url'])
    await client.say('**{} {}**\n'.format(name, placetype))
    await client.say('{}\n{} {} {} \n{}'.format(address, city, state, zipcode, phone))                   

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

client.run(TOKEN)
