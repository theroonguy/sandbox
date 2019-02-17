import discord
from discord.ext import commands
import pprint
import requests

TOKEN = 'NTQ2NDkyNTYxMDQ1NDU0ODY4.D0pA0A.P7oXTCDd8ZNUtWxOyRlwbnZIpfI'

client = commands.Bot(command_prefix = 'z-')

@client.event
async def on_ready():
    print('Awaiting your command')
'''
@client.event
async def on_message(message):

    channel = message.channel
    
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='pray', value='Usage: z-pray (location)')
    embed.add_field(name='eat', value='Usage: z-eat (all | (food)) (location)')

    if message.content == 'z-help':
        await client.send_message(channel, '```Commands:\nz-pray ( location ) -- shows you the closet available praying location\nz-eat ( all | [foodtype] ) ( location ) -- shows you the closest available eating location with a specific food```')
'''
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
    zabihah_url = data['data']['url']

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.add_field(name='Brought to you by ZabihahBot', value='{} {}'.format(desc, distance), inline=True)
    embed.add_field(name=name,value='{}\n{} {} {} \n{}'.format(address, city, state, zipcode, phone),inline=False)

    embed.set_footer(text='Click on the link for more info')
    embed.set_image(url=photo)
    embed.set_thumbnail(url='https://www.zabihah.com/img/logo_zabihah_bot.png')

    await client.say(embed=embed)
    await client.say(zabihah_url)

@client.command()
async def eat(*args):
    output = ''
    for word in args:
        output+=word
        output+=' '

    output2=tuple(output.split(','))

    output3 = []
    for word in output2:
        output3.append(word)

    output3.append(output3[0])
    del output3[0]
#   await client.say('Searching for '+output2[0])
    
    url = 'http://iphone.halalfire.com/bot_restaurant.php?uuid=1&key=O2A8Uo5ACzEXW7NnPYPX&l={}&k={}'.format(output3[0],output3[1])
    res = requests.get(url)
    data = res.json()

    await client.say(url)

    number = data['data']['number']

    if number == 0:
        await client.say('Error.')
    status_text = data['data']['status_text']
    photo = data['data']['photo_url']
    name = data['data']['name']
    address = data['data']['address']
    city = data['data']['city']
    state = data['data']['state']
    zipcode = data['data']['zip']
    phone = data['data']['phone']
    distance = data['data']['distance']
    desc = data['data']['desc']
    tags = data['data']['tags']
    zabihah_url = data['data']['url']

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.add_field(name='{}'.format(status_text), value="{} {}".format(desc, distance), inline=True)
    embed.add_field(name=name,value='{}\n{}\n{} {} {} \n{}'.format(tags, address, city, state, zipcode, phone),inline=False)
    embed.set_footer(text='Click on the link below for more info'.format(zabihah_url))
    embed.set_image(url=photo)

    await client.say(embed=embed)
    await client.say(zabihah_url)
 
client.run(TOKEN)
