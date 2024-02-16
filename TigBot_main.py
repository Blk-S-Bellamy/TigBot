#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|---------Bot Information---------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

VERSION="TigBot0.3"
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
#|-------------------Imports----------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

import os
import time
import socket
import openai  # openai api library
import asyncio
import requests  # packages for API communication
import discord  #Pycord
import urllib.error
import urllib.request
import Tigbot_config as tc
import Tigbot_logging as tl
import discord.ext.commands as commands
import CNDBL_0_4 as cn  # importing database manager

from datetime import datetime
from bs4 import BeautifulSoup
from requests.exceptions import ConnectTimeout
from dotenv import load_dotenv  # used to hide api key

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|----------------Import Config-------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿
# import functionality from externalized scripts for readability

Welcome_Channel_id = tc.Welcome_Channel_id
guild_id_lst = tc.guild_id_lst
vc_creation_id = tc.vc_creation_id
vc_creation_category = tc.vc_creation_category
vc_pre_decor = tc.vc_pre_decor
vc_post_decor = tc.vc_post_decor
log_channel_id = tc.log_channel_id
log_joke_calls = tc.log_joke_calls
log_vc_creation = tc.log_vc_creation
log_vc_deletion = tc.log_vc_deletion
db_gen_vc = tc.db_gen_vc
db_bot_events = tc.db_bot_events
db_slash_commands = tc.db_slash_commands 
db_ai_conversations = tc.db_ai_conversations

log_db_gen_vc = tl.log_db_gen_vc
log_db_bot_events = tl.log_db_bot_events
log_db_slash_commands = tl.log_db_slash_commands
log_db_ai_conversations = tl.log_db_ai_conversations

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|---------Setting Global Variables---------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

intents = discord.Intents.default()
intents = intents.all()
intents.members = True
load_dotenv()
unix = time.time()  # setting unix time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.settimeout(1.0) # setting the timeout for one second.
bot = commands.Bot(command_prefix='/', intents=intents)
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # set date-time 

guild_id_ = 0  # contains the guild id on runtime
created_vc = [] # contains all of the voice channels generated during runtime

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|----------------Core Functions------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿


async def set_bot_status():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=tc.bot_status))
    return


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    await startup_vc_purge()  # purge generated vc that are empty at bot startup
    await set_bot_status()  # set the bot status
    await tl.log_db_bot_events("debug", "startup", 0, 0)


#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|--------------Logging Functions-----------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿
# logging that is sent through the bot

async def log_jcall(memb_name, chnl, call):
    if log_joke_calls is True:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        channel = bot.get_channel(log_channel_id)
        await channel.send(f'```[{now}]{memb_name} called {call} in \"{chnl.name}|ID:{chnl.id}\"```')

    else:
        pass
    return

async def log_vc_c(memb_name, chnl):
    if log_vc_creation is True:
        channel = bot.get_channel(log_channel_id)
        await channel.send(f'```[{now}]{memb_name} auto-generated \"{chnl.name}|ID:{chnl.id}\" voice channel```')
    else:
        pass
    return

async def log_vc_d(chnl):
    if log_vc_deletion is True:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        channel = bot.get_channel(log_channel_id)
        await channel.send(f'```[{now}]\"{chnl.name}|ID:{chnl.id}\" has 0 members and was deleted```')
    else:
        pass
    return


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


# purge a number of messages from a channel if you have admin or an admin role
@bot.slash_command(guild_ids=guild_id_lst, name = "purge", description = "purge a number of messages from a channel")
async def purge(ctx, amount: int = 1000000):
    if await admin_check(ctx) is True:
        await ctx.channel.purge(limit=amount)
        await ctx.respond(f"```clearing {amount} messages```")

        return
    else:
        pass

    await ctx.respond("```you need admin to execute this command```")
    return


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
        v_channel = await guild.create_voice_channel(f"{vc_pre_decor}{member.name}{vc_post_decor}", category=cat) 
        channel = bot.get_channel(int(v_channel.id))
        # adding the voice channel to the vc hist and the temp storage for deletion when empty

        unix = time.time()
        cn.input_one('tigbot.db', 'generated_vc', (str(channel.name), int(v_channel.id), member.guild.id))
        await log_db_gen_vc('created', str(channel.name), int(v_channel.id), str(member.name), str(member.id), member.guild.id)
        # cn.input_one('tigbot.db', 'generated_vc_hist', (str(channel.name), int(v_channel.id), str(member.id), member.guild.id, unix))
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
                        # remove deleted vc from database
                        cn.execute("tigbot.db", f"DELETE FROM generated_vc WHERE vc_id={id_num}")
                        await log_db_gen_vc('deleted', str(channel.name), int(channel.id), str(member.name), str(member.id), member.guild.id)
                        del created_vc[count]
                    else:
                        pass
                else:
                    pass

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|-------------AI Response Bot--------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

openai.api_key = os.getenv('OPENAI_KEY')
IGNORE_PREFIX = "/"
CHANNELS = tc.ai_channels

@bot.event
async def on_message(message):
    u_message = message.content
    templist = []
    if message.author.bot:
        return
    if message.content.startswith(IGNORE_PREFIX):
        return
    if bot.user.id not in [mention.id for mention in message.mentions]:
        return
    if message.channel.id not in CHANNELS:
        return  

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
        stuff = conversation

    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=conversation)

    
    send_typing_task.cancel()
    if not response:
        await message.reply("I'm having some trouble connecting to the internet. Try again in a moment.")
        return
    

    response_message = response.choices[-1].message.content
    chunk_size_limit = 2000
    res = ''
    
    for i in range(0, len(response_message), chunk_size_limit):
        chunk = response_message[i:i + chunk_size_limit]
        await message.reply(chunk)
        res += str(chunk)
    # save the conversation as it happens to the database if enabled
    await tl.log_db_ai_conversations(str(message.author.name), int(message.author.id), str(u_message), str(res), str(message.guild.id))

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|------------DB Syncronization-------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿



async def startup_vc_purge():
    # if a generated vc is empty, delete it
    global created_vc, guild_id_

    # iterate through the list of generated vc id
    for count, vcid in enumerate(created_vc):
        try:
            guild = bot.get_guild(int(guild_id_))
            channel = guild.get_channel(int(vcid))
            members = channel.members
            if isinstance(channel, discord.VoiceChannel):
                # if the channel has 0 members then delete it
                if len(channel.members) == 0:
                    try:
                        await channel.delete()
                    except Exception:
                        print(f'Channel not found [{vcid}]')
                    # remove deleted vc from database
                    cn.execute("tigbot.db", f"DELETE FROM generated_vc WHERE vc_id={vcid}")
                    del created_vc[count]
                else:
                    pass
        # attribute error means that the channel no longer exists so skip delete
        except AttributeError:
            cn.execute("tigbot.db", f"DELETE FROM generated_vc WHERE vc_id={vcid}")
            del created_vc[count]

        else:
            pass


def db_vc_sync():  # sync the history of the generated vc from the db
    global created_vc, guild_id_
    cn.refresh_database_structures()
    v_ids = cn.select_all('tigbot.db', "SELECT vc_id FROM generated_vc")
    guild_id_ = cn.select_one('tigbot.db', "SELECT guild_id FROM generated_vc")
    for item in v_ids:
        created_vc.append(int(item))
    return
    


# activate syncing the database memory of vc creation
db_vc_sync()
# run the discord bot
bot.run(os.getenv("DISCORD_TOKEN"))
#cn.input_one('tigbot.db', 'generated_vc', ('stuff', 'sss'))