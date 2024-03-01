#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|---------Bot Information---------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

VERSION="TigBot0.4"
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
import discord  # Pycord
import importlib
import urllib.error
import urllib.request
import TigBot_config as tc
import TigBot_logging as tl
import discord.ext.commands as commands
import CNDBL_0_4 as cn  # importing database manager
import random

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
    # await set_bot_status()  # set the bot status
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
#|-----------DB Requests Section------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿





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
#|--------------Main-Functions--------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿


# request a joke and if the joke db is gone, request through api (src is how the joke is sourced)
def fetchjoke(src):
    # the list of joke categories in the database lol
    joke_indexes = []
    db_size = cn.select_one("jokes.db", "SELECT Count(*) FROM jokes")

    # ensure that the id has not been selected in the last 100 times
    complete = False
    while not complete:
        s_index = random.randrange(1, int(db_size), 1)
        if s_index in joke_indexes:
            pass
        else:
            complete = True
        # remove the 101th entry if it is added
        if len(joke_indexes) >= 101:
            del joke_indexes[-1]

    if src == "random":

        joke = cn.select_one('jokes.db', f"SELECT joke FROM jokes WHERE rowid={s_index}")
        san = joke.replace('#','"')
        joke = san.replace("^","'")

        joke = f"```css\n{joke}\n[joke: {s_index}]\n```"
        return joke
    else:
        return "-BLANK-"


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


# /randjoke command response
@bot.slash_command(guild_ids=guild_id_lst, name = "randjoke", description = "Ask and recieve a random joke!")
async def randjoke(ctx):
    joke = fetchjoke('random')
    await ctx.respond(joke)
    await log_jcall(ctx.author.name, ctx.channel, "randjoke")


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


# purge a number of messages from a channel if you have admin or an admin role
@bot.slash_command(guild_ids=guild_id_lst, name = "util", description = "utilities for administration")
async def util(ctx):
    auth = ctx.author
    send = ""

    # a list of utility functions
    util_dict = {0: ["Refresh Config", refresh_config],
                 1: ["Show Database Size", database_size],
                 2: ["Show Last Startup", last_startup],
                }

    # trigger the typing response for the user
    async def send_typing_interval():
        while True:
            await ctx.channel.trigger_typing()

    # This will make sure the user gave a correct response
    def check(msg):
        util_keys = util_dict.keys()
        # check if user input is in the options and if not wait for correct input
        try:
            if int(msg.content) in util_keys and msg.author == auth:
                in_dict = True
                # informing the user the selected option is running
                send = util_dict[int(msg.content)]
            else:
                in_dict = False
        except (TypeError, ValueError):
                in_dict = False
        return msg.author == ctx.author and msg.channel == ctx.channel and in_dict

    async def del_last(ctx):
        # search last messages to delete original reply from the bot
        found = False
        async for sent in ctx.channel.history(limit=10):
            if sent.content[0:5] == "```py" and sent.author.id == bot.user.id and found is False:
                # print(sent.content)
                de = await ctx.fetch_message(sent.id)
                await de.delete()
                found = True


    # if a user has permission to execute the command
    if await admin_check(ctx) is True:
        util_str = ""  # contains list of options for the user.
        # turn the dict of options into a string to be printed 
        for count, item in enumerate(util_dict.values()):
            util_str += f"\n{count}: {item[0]}"
        
        botm = await ctx.respond(f"```py\nChoose an option by number: {util_str}```")  # bot response
        send_typing_task = asyncio.create_task(send_typing_interval())

        # try to recieve a reply from a user
        try:
            msg = await bot.wait_for("message", check=check, timeout=30)
            await msg.delete()
            await del_last(ctx)
    
            
            # inform the user the command is being run
            t1 = util_dict[int(msg.content)]
            t2 = t1[0]
            send_typing_task.cancel()
            inform = await t1[1](ctx)
            if inform != None:
                await ctx.respond(inform)
            else:
                pass


        except asyncio.TimeoutError:
            send_typing_task.cancel()
            await ctx.respond(f"```arm\nSORRY, you took too long to respond and your command has timed out!\n```")
            await del_last(ctx)
            
            return

    # if the user does not have permission to do a command
    else:
        await ctx.respond(f"```py\nYou need Admin to execute this command\n```")


# refreshes the config and anything that would change with the refresh
async def refresh_config(ctx):
    importlib.reload(tc)
    await set_bot_status()  # set the bot status
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # set date-time
    cn.input_one('tigbot.db', 'bot_logs', ("utility", 'refresh config', 0, 0, now))
    return "```diff\n+config reloaded\n+bot status updated\n```"


# returns to the user the size of the database
async def database_size(ctx):
    cn.input_one('tigbot.db', 'bot_logs', ("utility", 'show database size', 0, 0, now))  # database log the command execution
    
    try:  # fetch main database size if it exists
        main_s = os.path.getsize(tc.database_name)
        m_kb = main_s / 1000
        m_mb = m_kb / 1000
        m_gb = m_mb / 1000
        main_det = f"+{tc.database_name}+\n-[kb] {m_kb}\n-[mb] {m_mb}\n-[gb] {m_gb}"
    except FileNotFoundError:
        main_det = f"⣿¤{tc.database_name}¤⣿ NOT FOUND"

    try:  # fetch joke database size if it exists
        joke_s = os.path.getsize(tc.joke_database)
        j_kb = joke_s / 1000
        j_mb = j_kb / 1000
        j_gb = j_mb / 1000
        joke_det = f"+{tc.joke_database}+\n-[kb] {j_kb}\n-[mb] {j_mb}\n-[gb] {j_gb}"
    except FileNotFoundError:
        joke_det = f"⣿¤{tc.joke_database}¤⣿ NOT FOUND"

    return f"```diff\n{main_det}\n\n{joke_det}\n```"


# returns to the user the last time the bot was started up
async def last_startup(ctx):
    size = os.path.getsize(tc.database_name)
    su = cn.select_one('tigbot.db', "SELECT timestamp FROM bot_logs WHERE event='startup' ORDER BY ROWID DESC LIMIT 1;")
    cn.input_one('tigbot.db', 'bot_logs', ("utility", 'show last startup', 0, 0, now))
    return f"```diff\n+Last startup is\n-{su}\n```"


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
    u_msg = message.content
    bot_name = bot.user.name .replace(' ', '_').replace(r'[^\w\s]', '')
    username = message.author.display_name.replace(' ', '_').replace(r'[^\w\s]', '')
    # stop if message is authored by a bot OR has an https req in it.
    if message.author.bot or "https:" in u_msg:
        return
    elif message.content.startswith(IGNORE_PREFIX) or message.channel.id not in CHANNELS:
        return
    elif bot.user.id not in [mention.id for mention in message.mentions]:
        return

    # typing appearance for the bot
    async def send_typing_interval():
        while True:
            await message.channel.trigger_typing()
            await asyncio.sleep(tc.ai_sleep_time)
    send_typing_task = asyncio.create_task(send_typing_interval())

    add_c = []
    conversation = []
    # the initial ai personality prompt
    conversation.append(tc.ai_personality_prompt)

    # get the history of the conversation in the channel
    async for msg in message.channel.history(limit=tc.ai_conv_history):
        # case that the input is a bot add the message as 'assistant'
        if msg.author.id == bot.user.id:
            # append the line to the history
            add_c.append({
                'role': 'assistant',
                'name': bot_name,
                'content': msg.content,
            })

        # case that the input message is not from the bot or any bots
        elif not msg.author.bot:
            # remove the @ from user messages
            try:
                if msg.content[0] == '<' and ">" in msg.content[5:26]:
                    trash, pss = msg.content.split(">", 1)
                else:
                    pss = msg.content
            except IndexError:
                pss = msg.content
            # append to the conversation
            add_c.append({
            'role': 'user',
            'name': username,
            'content': pss,
            })

    conversation.extend(add_c[::-1])

    try:
        # request the api for chat completion
        response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=conversation)
        
    # catch errors related to token length
    except (openai.error.InvalidRequestError,
           ):
        await message.reply("```sh\nPlease try sending a shorter message, if the issue persist inform staff!\n```")
        send_typing_task.cancel()
        return
    
    # catch mosty authentication errors 
    except (openai.error.APIError,
            openai.error.InvalidAPIType,
            openai.error.OpenAIError,
            openai.error.APIError,
            openai.error.AuthenticationError,
            ):
        await message.reply("```sh\nThe API key for chat GPT is incorrect OR authentication has failed for another reason\n```")
        print('::ERROR:: The API key for chat GPT is incorrect OR authentication has failed for another reason')
        send_typing_task.cancel()
        return

    # catch any other errors and bail to prevent crashing
    except Exception:
        await message.reply("```sh\nAn unknown error has taken place, if the issue persist inform staff!\n```")
        print('::ERROR:: An unknown error has taken place, if the issue persist inform staff!')
        send_typing_task.cancel()
        return
    
    
    # cancel the typing task
    send_typing_task.cancel()
    # the bot message from the response
    bot_message = response.choices[-1].message.content
    # send the bot message to the channel in chunks
    chunk_size_limit = 2000
    res = ''
    for i in range(0, len(bot_message), chunk_size_limit):
        chunk = bot_message[i:i + chunk_size_limit]
        await message.reply(chunk)
        res += str(chunk)

    await tl.log_db_ai_conversations(str(message.author.name), int(message.author.id), str(u_msg), str(bot_message), str(message.guild.id))


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
    

def run():
    db_vc_sync()  # activate syncing the database memory of vc creation
    try:
        bot.run(os.getenv("DISCORD_TOKEN"))  # run the discord bot
    except (discord.errors.LoginFailure):
        print("::ERROR:: discord token provided in .env is not correct or a connection has failed")
        exit()


run()

