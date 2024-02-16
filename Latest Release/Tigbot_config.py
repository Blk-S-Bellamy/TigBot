#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
#⣿------------Tigbot Config File--------⣿
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿
#|---------------Channel Ids----------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

# Setting `Watching ` status (https://stackoverflow.com/questions/59126137/how-to-change-activity-of-a-discord-py-bot#59126629)
bot_status = "Bob Ross Jelqing"
Welcome_Channel_id = int(1206448622816854026)  # Channel to send welcome messages
guild_id_lst = [1206163627841818676] # guild id numbers
vc_creation_id = int(1206425843388256306) # voice channel people join to be made their own vc
vc_creation_category = "Voice Channels"

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|-------------AI Chat Config---------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

ai_channels = [1206888054766440468] # channels the ai will respond in

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|-----------Vc Creation Config-------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

# the text after the vc creators name in the title of new vc "Balkon<here>"
vc_pre_decor = "| "
# the text before the vc creators name in the title of new vc "<here>Balkon"
vc_post_decor = " ⡯⣯|>"

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|---------Server Channel Logging-----------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

# the text channel to log events in (admin only is best)
log_channel_id = int(1206424268628561971)
log_joke_calls = False
log_vc_creation = False
log_vc_deletion = False

#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|------------Database Logging--------------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

# set what is stored in the database
database_name = 'tigbot.db'  # changing will make a new database if it doesn't exist but not migrate data from the old one
db_gen_vc = True  # save to the database every time a voice channel is generated
db_bot_events = True  # save to the database bot events and errors
db_slash_commands = True  # save to the database the execution of slash commands
db_ai_conversations = True  # save to the database the conversations between ai and user

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