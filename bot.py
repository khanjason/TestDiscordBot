from boto.s3.connection import S3Connection
import discord
import time
# Import the os module.
import os

# Import load_dotenv function from dotenv module.


import redis
from discord.ext import commands

# Loads the .env file that resides on the same level as the script.
#load_dotenv()

session=False

general_speakers=[]


# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv('BOT_TOKEN')
#s3 = S3Connection(os.environ['BOT_TOKEN'], os.environ['S3_SECRET'])

# Creates a new Bot object with a specified prefix. It can be whatever you want it to be.
bot = commands.Bot(command_prefix="!")

# on_message() event listener. Notice it is using @bot.event as opposed to @bot.command().
@bot.event
async def on_message(message):
	# Check if the message sent to the channel is "hello".
	if message.content == "hello":
		# Sends a message to the channel.
		await message.channel.send("pies are better than cakes. change my mind.")

	# Includes the commands for the bot. Without this line, you cannot trigger your commands.
	await bot.process_commands(message)

# Command $ping. Invokes only when the message "$ping" is send in the Discord server.
# Alternatively @bot.command(name="ping") can be used if another function name is desired.
@bot.command(
	# Adds this value to the $help ping message.
	help="Uses come crazy logic to determine if pong is actually the correct value or not.",
	# Adds this value to the $help message.
	brief="Prints pong back to the channel."
)
async def ping(ctx):
	# Sends a message to the channel using the Context object.
	await ctx.channel.send("pong")
@bot.command(
	# Adds this value to the $help print message.
	help="Starts the MUN session and enables session commands.",
	# Adds this value to the $help message.
	brief="Starts the MUN session."
)
async def startSession(ctx):
	session=True
	await ctx.channel.send("Session has started!")

@bot.command(
	# Adds this value to the $help print message.
	help="Ends the MUN session and disables session commands.",
	# Adds this value to the $help message.
	brief="Starts the MUN session."
)
async def endSession(ctx):
	session=False
	await ctx.channel.send("Session has ended!")

@bot.command(
	# Adds this value to the $help print message.
	help="Adds user to general speakers list.",
	# Adds this value to the $help message.
	brief="Self-add to speakers list."
)
async def addGS(ctx):
	if session==False:
                general_speakers.append(str(ctx.author.nick))
                
                
                await ctx.channel.send(ctx.author.mention+' has been added to the General Speakers List!')


@bot.command(
	# Adds this value to the $help print message.
	help="View the full general speakers list.",
	# Adds this value to the $help message.
	brief="View speakers list."
)
async def GS(ctx):
	if session==False:
                
                await ctx.channel.send("General Speakers List: ")
                await ctx.channel.send(general_speakers)



@bot.command(
	# Adds this value to the $help print message.
	help="Give someone the floor.",
	# Adds this value to the $help message.
	brief="Give someone the floor for a set amount of time."
)
async def speak(ctx,*args):
	if session==False:
                t=args[1]
                u=args[0]
                await ctx.channel.send(u+" has the floor!")
                time.sleep((int(t)*60)-10)
                await ctx.channel.send("ten seconds left, "+u)
                time.sleep(10)
                await ctx.channel.send("time is up, "+u)
@bot.command(
	# Adds this value to the $help print message.
	help="mod/unmod total time, speakers time, country, topic",
	# Adds this value to the $help message.
	brief="Propose a caucus."
)
async def propose(ctx,*args):
	if session==False:
                type=args[0]
                if type!='unmod':
                        total=args[1]
                        speaking=args[2]
                        country=args[3]
                        topic=' '.join(word for word in args[3:])
                        
                        m = await ctx.channel.send(country+" proposed a "+type+' caucus on '+topic+' for '+total+' mins with '+speaking+ ' seconds speakers time.')
                        await m.add_reaction("\U0001F44D")
                        await m.add_reaction("\U0001F44E")
                else:
                        total=args[1]
                        country=args[2]
                        m = await ctx.channel.send(country+" proposed a "+type+' caucus for '+total+' mins.')
                        await m.add_reaction("\U0001F44D")
                        await m.add_reaction("\U0001F44E")
                        
@bot.command(
	# Adds this value to the $help print message.
	help="Start an unmod.",
	# Adds this value to the $help message.
	brief="Give time in minutes for an unmod."
)
async def unmod(ctx,*args):
	if session==False:
                t=args[0]
                
                await ctx.channel.send("The UnMod has started!")
                time.sleep(int(t)*60)
                
                await ctx.channel.send("UnMod is over!")




# Command $print. This takes an in a list of arguments from the user and simply prints the values back to the channel.
@bot.command(
	# Adds this value to the $help print message.
	help="Looks like you need some help.",
	# Adds this value to the $help message.
	brief="Prints the list of values back to the channel."
)
async def print(ctx, *args):
	response = ""

	# Loops through the list of arguments that the user inputs.
	for arg in args:
		response = response + " " + arg

	# Sends a message to the channel using the Context object.
	await ctx.channel.send(response)

# Executes the bot with the specified token. Token has been removed and used just as an example.






bot.run(DISCORD_TOKEN)
