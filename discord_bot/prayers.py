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

    await client.say(data['status_text']+'\n')
    await client.day(data['prayerspaces']['name'])

    address = data['prayerspaces']['address']
    city = data['prayerspaces']['city']
    state = data['prayerspaces']['state']
    zipcode = data['prayerspaces']['zip']
    phone = data['prayerspaces']['phone']
    distance = data['prayerspaces']['distance']

    fname = '{}'.format(name)
    faddress = '{}'.format(address)
    fcity = '{}'.format(city)
    fstate = '{}'.format(state)
    fzipcode = '{}'.format(zipcode)
    fphone = '{}'.format(phone)

    await client.say('**{}**'.format(name))

    await client.say(faddress+'\n'+fcity+', '+fstate+' '+fzipcode+'\n'+fphone)

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

client.run(TOKEN)
