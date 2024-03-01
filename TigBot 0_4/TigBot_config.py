#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
#⣿------------Tigbot Config File--------⣿
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿
#|---------------Channel Ids----------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

# Setting `Watching ` status (https://stackoverflow.com/questions/59126137/how-to-change-activity-of-a-discord-py-bot#59126629)
bot_status = "you intently"
Welcome_Channel_id = int()  # Channel to send welcome messages
guild_id_lst = [] # guild id numbers that the bot is effective in
vc_creation_id = int() # voice channel people join to be made their own vc
vc_creation_category = ""

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|-------------AI Chat Config---------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

ai_channels = [] # text channel id's the ai will respond in
ai_sleep_time = 3  # th time the ai waits before responding to a question
ai_conv_history = 8  # the amount of previous messages provided to chat gpt as conversational context
ai_personality_prompt = {
                         'role': 'system',
                         'content': 'you are a helpful bot called Mr. Tig. You are a little grumpy at times but also helpful'
                        }


#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|-----------Vc Creation Config-------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

# the text after the vc creators name in the title of new vc "Balkon<here>"
vc_pre_decor = "🔊・"
# the text before the vc creators name in the title of new vc "<here>Balkon"
vc_post_decor = "'s VC"

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|---------Server Channel Logging-----------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

# the text channel to log events in (admin only is best)
log_channel_id = int()  # text channel ID
log_joke_calls = False
log_vc_creation = False
log_vc_deletion = False

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|------------Database Logging--------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

# set what is stored in the database
database_name = 'tigbot.db'  # not advised to try and change in versions <= 0_4 
joke_database = 'jokes.db'  # not advised to try and change in versions <= 0_4 
db_gen_vc = True  # save to the database every time a voice channel is generated
db_bot_events = True  # save to the database bot events and errors
db_slash_commands = True  # save to the database the execution of slash commands
db_ai_conversations = True  # save to the database the conversations between ai and user

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|---------------Dictionaries---------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿


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
══{VERSION}══
══https://github.com/Blk-S-Bellamy?tab=repositories══
"""