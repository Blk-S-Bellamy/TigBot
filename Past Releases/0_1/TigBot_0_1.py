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
load_dotenv()

VERSION="Gubbins_dev0.1"
"""
⣝⡵⡯⣯⣝⡵⡯⣯⣝⡵⡯⣯⣝⡵⡯⣯⣝⡵⢾
¤|        __         |¤
¤|     -=(¤ '.       |¤
¤|        '.-.\      |¤
¤|        /|  \\     |¤
¤|        '|  ||     |¤
¤|         ▄\_):,    |¤
¤|  PROGRAMMED BY:   |¤
⣝⡵⡯|ßlk-S-Bellamy|⣝⡵⡯⢾

══https://github.com/Blk-S-Bellamy?tab=repositories══
"""

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|--------------Config Variables------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿
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
bot = discord.Bot()


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
#|-------------Discord Functions------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

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
                    print("ERROR: CHANNEL PASSED IN 'on_voice_state_update' IS NOT A VC!")


#bot.run("MTIwNjE2MzA5OTgyMDc1Njk5Mg.GsSZue.QW3-70Up-HSQSoWuH3Uh0u7H25G4tjSOQNa8EE")
bot.run(os.getenv("DISCORD_TOKEN"))