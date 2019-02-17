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
    zabihah_url = data['data']['url']

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.add_field(name='Brought to you by ZabihahBot', value='{} {}'.format(desc, distance), inline=True)
    embed.add_field(name=name,value='{}\n{} {} {} \n{}'.format(address, city, state, zipcode, phone),inline=False)

    embed.set_footer(text='Check out the link below for more info')
    embed.set_footer(text='[Click here for more info] ({})'.format(zabiha_url))
    embed.set_image(url=photo)
    embed.set_thumbnail(url='https://www.zabihah.com/img/logo_zabihah_bot.png')

    await client.say(embed=embed)
    await client.say(zabihah_url)

@client.command()
async def find(*args):
    output2 = ''
    for word in args:
        output2 += word

    url = 'http://iphone.halalfire.com/bot_restaurant.php?uuid=1&key=O2A8Uo5ACzEXW7NnPYPX&l={}&k={}'.format(output2, output3)
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
    tags = data['data']['tags']
    zabiha_url = data['data']['url']    

    embed = discord.Embed{
        colour = discord.Colour.red()
    )

    embed.add_field(name='{} {}'.format(status_text, distance), value=desc, inline=True)
    embed.add_field(name=name,value='{}\n{}\n{} {} {} \n{}'.format(tags, address, city, state, zipcode, phone),inline=False)
    embed.set_footer(text='[Click here for more info] ({})'.format(zabiha_url))
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
