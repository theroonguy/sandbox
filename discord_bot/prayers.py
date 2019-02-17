import discord
from discord.ext import commands
import pprint
import requests
    

TOKEN = 'NTQzOTUzNDM2NTUxNDEzNzcw.D0EFWQ.koaPnK_GT59KJtfKqP4Xis2CqKI'

client = commands.Bot(command_prefix = 'pray ')


@client.event
async def on_ready():
    print('Awaiting your command')
      
@client.command()
async def near(*args):
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

    await client.say('{} {}\n{}\n{}\n'.format(status_text, distance, desc, photo))
    await client.say('**{} {}**\n'.format(name, placetype))
    await client.say('{}\n{} {} {} \n{}'.format(address, city, state, zipcode, phone))
    await client.say('Check out {} for more info'.format(zabiha_url))

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

client.run(TOKEN)
