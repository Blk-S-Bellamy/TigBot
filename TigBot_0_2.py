import os
import socket
# used to hide api key
from dotenv import load_dotenv
# packages for API communication
import requests
from requests.exceptions import ConnectTimeout
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
#Pycord
import discord
import discord.ext.commands as commands
pr = discord.permissions
import openai
import asyncio

import interface
load_dotenv()
intents = discord.Intents.default()
intents.members = True
intents = intents.all()

botname="TigBot0.2"
VERSION="TigBot0.2"
program_info = f"""
⣝⡵⡯⣯⣝⡵⡯⣯⣝⡵⡯⣯⣝⡵⡯⣯⣝⡵⢾
¤|        __         |¤
¤|     -=(¤ '.       |¤
¤|        '.-.\      |¤
¤|        /|  \\     |¤
¤|        '|  ||     |¤
¤|         ▄\_):,    |¤
¤|  PROGRAMMED BY:   |¤
⣝⡵⡯|ßlk-S-Bellamy|⣝⡵⡯⢾
══{VERSION}══
══https://github.com/Blk-S-Bellamy?tab=repositories══
"""

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|--------------Config Variables------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

# Channel to send welcom messages
Welcome_Channel_id = int(1206448622816854026)
# guild id numbers
guild_id_lst = [1206163627841818676]

# voice channel people join to be made their own vc
vc_creation_id = int(1206425843388256306)
vc_creation_category = "Voice Channels"
# the text after the vc creators name in the title of new vc "Balkon<here>"
vc_pre_decor = "|"
# the text before the vc creators name in the title of new vc "<here>Balkon"
vc_post_decor = "⡯⣯|>"

log_channel_id = int(1206424268628561971)
log_joke_calls = False
log_vc_creation = False
log_vc_deletion = False

ai_channels = [1206888054766440468]

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|--------------Logging Functions-----------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿


# used to determine logging

async def log_jcall(memb_name, chnl, call):
    if log_joke_calls is True:
        channel = bot.get_channel(log_channel_id)
        await channel.send(f'```{memb_name} called {call} in \"{chnl.name}|ID:{chnl.id}\"```')

    else:
        pass

async def log_vc_c(memb_name, chnl):
    if log_vc_creation is True:
        channel = bot.get_channel(log_channel_id)
        await channel.send(f'```{memb_name} auto-generated \"{chnl.name}|ID:{chnl.id}\" voice channel```')
    else:
        pass

async def log_vc_d(chnl):
    if log_vc_deletion is True:
        channel = bot.get_channel(log_channel_id)
        await channel.send(f'``` \"{chnl.name}|ID:{chnl.id}\" has 0 members and was deleted```')
    else:
        pass


#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|------Environment/Global Variables--------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

# setting the timeout for one second.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                           
s.settimeout(1.0)
bot = commands.Bot()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|------------Global Item Lists-------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

# contains all of the voice channels generated during runtime
created_vc = []

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|----------API Requests Section------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

def req_dad_joke():
  # the headers for the api request that make it go through
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
             'Accept': 'text/plain',
            }

  # requesting the joke from the api and then parsing the result to get text result dad joke
  response = requests.get('https://icanhazdadjoke.com/', headers=headers)
  soup = BeautifulSoup(response.content, 'html.parser')
  # returning the dad joke in raw text form
  return str(soup)


def req_nsfw_joke():
  # the headers for the api request that make it go through
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            }

  # requesting the joke from the api and then parsing the result to get text result nsfw joke
  response = requests.get('https://v2.jokeapi.dev/joke/Dark?format=txt&type=single', headers=headers)
  soup = BeautifulSoup(response.content, 'html.parser')
  # returning the dad joke in raw text form
  return str(soup)


#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|--------------Slash-Commands--------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿


@bot.slash_command(guild_ids=guild_id_lst, name = "botinfo")
async def botinfo(ctx):
    await ctx.respond(f"```py\n{program_info}\n```")


@bot.slash_command(guild_ids=guild_id_lst, name='avatar', help='fetch avatar of a user')
async def dp(ctx, *, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar
    await ctx.respond(userAvatar)
    return

# /dadjoke command response
@bot.slash_command(guild_ids=guild_id_lst, name = "dadjoke", description = "Ask and recieve a dad joke!")
async def dadjoke(ctx):
    ddjoke = req_dad_joke()
    await ctx.respond(ddjoke)
    await log_jcall(ctx.author.name, ctx.channel, "dadjoke")

# /darkjoke command response
@bot.slash_command(guild_ids=guild_id_lst, name = "darkjoke", description = "Ask and recieve a dark joke!")
async def darkjoke(ctx):
    djoke = req_nsfw_joke()
    await ctx.respond(djoke)
    await log_jcall(ctx.author.name, ctx.channel, "darkjoke")


# check if a user has a certain permission level my roles (bool return)
async def admin_check(ctx):
    # check for owner status
    if ctx.author.guild_permissions.administrator:
        return True
    else:
        pass

    # check their rolls to see if they have admin
    for role in ctx.author.roles:
        if role.permissions.administrator:
            return True
        else:
            pass
    return False

@bot.slash_command(guild_ids=guild_id_lst, name = "purge", description = "purge a number of messages from a channel")
async def purge(ctx, amount: int = 1000000):
    if await admin_check(ctx) is True:
        await ctx.channel.purge(limit=amount)
        await ctx.respond(f"```cleared {amount} messages```")

        return
    else:
        pass

    await ctx.respond("```you need admin to execute this command```")
    return

    perms = ctx.author.guild_permissions
    roles = ctx.author.roles

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|----------------Bot-Events----------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

@bot.event
async def on_member_join(member):
    await member.send(
        f'Welcome to the server, {member.mention}! Enjoy your stay here.'
    )

@bot.event
async def on_voice_state_update(member, before, after):
    
    # check if user that joined was a bot (prevents trolling)
    if after is not member.bot:
      pass
    else:
      pass
    
    # this is the chat that is reported to in order to inform of someone joining the vc
    specCh = bot.get_channel(log_channel_id)
    
    # if the person is joining the channel, make a new vc
    if after.channel is not None and after.channel.id == vc_creation_id:
        
        guild = bot.get_guild(member.guild.id)
        cat = discord.utils.get(guild.categories, name=vc_creation_category)
        v_channel = await guild.create_voice_channel(f"{vc_pre_decor}{member.display_name}{vc_post_decor}", category=cat) 
        channel = bot.get_channel(int(v_channel.id))
        await member.move_to(channel)
        await log_vc_c(member.name, channel)

        # add the channel id to the list of generated channels 
        created_vc.append(v_channel.id)
        
    # if somone is leaving vc, check all generated vc to check if any are empty and should be deleted
    elif before.channel is not None:
        
        # make sure the person left a generated vc before checking the list
        if before.channel.id in created_vc:
            # iterate the list of generated vc and check each for 0 members
            for count, id_num in enumerate(created_vc):
                # refresh the channel from the API
                channel = bot.get_channel(int(id_num))
                # make sure the instance is a vc
                if isinstance(channel, discord.VoiceChannel):
                    # if a generated vc is empty, delete it
                    if len(channel.members) == 0:
                        await channel.delete()
                        await log_vc_d(channel)
                    else:
                        pass
                else:
                    pass

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|-------------AI Response Bot--------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

openai.api_key = os.getenv('OPENAI_KEY')
IGNORE_PREFIX = "/"
IGNORE_PREFIX = "/"

@bot.event
async def on_message(message):
    templist = []
    if message.author.bot:
        return
    elif message.content.startswith(IGNORE_PREFIX):
        return
    elif bot.user.id not in [mention.id for mention in message.mentions]:
        return
    elif message.channel.id not in ai_channels:
        return
    else:
        pass

    await message.channel.trigger_typing()


    async def send_typing_interval():
        while True:
            await message.channel.trigger_typing()
            await asyncio.sleep(5)

    send_typing_task = asyncio.create_task(send_typing_interval())

    convo_temp = []
    conversation = []
    conversation.append({
        'role': 'system',
        'content': 'You are Tig Bot. Tig Bot is a Discord Bot in the Tanz Army Discord server. Tig Bot was coded by Tig. Tig Bot is a complete jerk, his responses are witty, sarcastic, and sometimes very cruel. Tig Bot dislikes weird chests. Devin is a weird chest. Tig Bot is slightly racist.'
    })
    async for msg in message.channel.history(limit=10):
        if msg.author.bot and msg.author.id != bot.user.id:
            continue
        if msg.content.startswith(IGNORE_PREFIX):
            continue

        username = message.author.display_name.replace(' ', '_').replace(r'[^\w\s]', '')
        
        if msg.author.id == bot.user.id:
            botusername = bot.user.name
            convo_temp.append({
                'role': 'assistant',
                'name': botusername,
                'content': msg.content,
            })
            continue
        
        # filters out bot name if said in history
        rcontent = msg.content.split(">", 1)
        try:
            rcontent = rcontent[1]
        # if no bot name is said, skips removing characters
        except IndexError as e:
            rcontent = rcontent[0]

        convo_temp.append({
            'role': 'user',
            'name': username,
            'content': rcontent,
            })
        try:

            conversation.extend(convo_temp[::-1])
        except TypeError as e:
            print(f"There was an error>> {e}")


    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=conversation)

    send_typing_task.cancel()
    if not response:
        await message.reply("I'm having some trouble connecting to the internet. Try again in a moment.")
        return

    response_message = response.choices[-1].message.content
    chunk_size_limit = 2000

    for i in range(0, len(response_message), chunk_size_limit):
        chunk = response_message[i:i + chunk_size_limit]
        await message.reply(chunk)

bot.run(os.getenv("DISCORD_TOKEN"))
