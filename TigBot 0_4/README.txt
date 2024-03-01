!! JOKES.DB MUST BE UNZIPPED BEFORE RUNNING THE BOT TO ACCESS THE JOKES !!

## DEBIAN BASED LINUX ##-----------------------------------------------------

1. run the deb_base_setup.sh in the main directory where the bot files are stored
2. if dependency installation is complete, move on to the configuration section and fill in channel id needed for th bot
3. add API keys for AI and your discord bot as seen below
4. run bot with "python3 TigBot_run.py"

## WINDOWS ##-----------------------------------------------------------------

1. install these dependencies in a virtual environment

pip install openai==0.28
pip install bs4
pip install requests
python3 -m pip install python-dotenv
pip install asycio

pip install py-cord
OR::
pip install -U py-cord --force-reinstall

2. configure the bot as seen below
3. add API keys as seen below
4. run bot with "python3 TigBot_run.py"


## CONFIG VARIABLES AND CONFIGURATION ##----------------------------------------

:CHANNEL ID SECTION:
8:"bot_status" with the status to be seen after the bots activity "Watching"
9:"Welcome_Channel_id" with the id of the text channel for welcoming members (not working yet)
10:"guild_id_lst" with a list of guild id that the bot should look in for events (limit 1 but changing soon)
11:"vc_creation_id" the voice channel id that will create a new channel if a user joins
12:"vc_creation_category" the category generated voice channels will appear in

:AI SECTION:
18:"ai_channels" channel ids of where the ai can respond to users
21:"ai_personality_prompt" the 'content' value is the personality prompt for the ai

:SERVER CHANNEL LOGGING:
41:"log_channel_id" the text channel id where logging server (if enabled) is sent


## ENV API KEY SETUP ##----------------------------------------------------------
DISCORD_TOKEN=<bot_token>
OPENAI_KEY=<openai_4_token>
