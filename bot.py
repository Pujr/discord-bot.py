import discord
from discord.ext import commands

TOKEN = ""

client = commands.Bot(command_prefix = "<")
client.remove_command('help') 

@client.event 
async def on_ready():
    await client.change_presence(game=discord.Game(name='Type <help'))
    print("I'm ready Master")

@client.event 
async def on_message(message):
    print('A user has sent a message.')
    await client.process_commands(message)


    #Help Info------------------------------------------------------------------

@client.command()
async def help():
    await client.say('**Commands List - <user <bot <mod <fun <nsfw**')

@client.command()
async def helpuser():
    await client.say('**<ping**')

@client.command()
async def helpbot():
    await client.say('**Null**')

@client.command()
async def helpmod():
    await client.say('**Null**')

@client.command()
async def helpfun():
    await client.say('**Null**')

@client.command()
async def helpnsfw():
    await client.say ('**Null**')     



    #User Commands----

@client.command()
async def ping():
    await client.say('Pong!')
		

    #Fun Commands-----



    #Bot Commands----

@client.command()
async def info():
    await client.say(' `Bot made and created by 🎃🖤Daddy Purj🖤🎃#3418` ')

    #Nsfw Commands-------
	
	
	
	
	

	#Server Commands-------

	
    
              
              
      
client.run(TOKEN)    