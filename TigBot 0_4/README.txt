!! JOKES.DB MUST BE UNZIPPED BEFORE RUNNING THE BOT TO ACCESS THE JOKES !!

install these dependencies in a virtual environment 

pip install openai==0.28
pip install bs4
pip install requests
python3 -m pip install python-dotenv
pip install asycio

pip install -U py-cord --force-reinstall
OR::
pip install py-cord


then fill in the tigbot config variables:
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

.env setup:
DISCORD_TOKEN=<bot_token>
OPENAI_KEY=<openai_4_token>

then execute TigBot_run.py with:

Linux/Windows
python TigBot_run.py
OR:
python3 TigBot_run.py
