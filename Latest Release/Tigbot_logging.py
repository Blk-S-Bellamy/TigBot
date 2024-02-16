#⣿¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⣿
#|--------------Logging Functions-----------|
#⣿▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄⣿

from datetime import datetime  # importing date-time
import Tigbot_config as tc
import CNDBL_0_4 as cn  # importing database manager
import asyncio


# log created voice channels to the "generated_vc_hist" table
async def log_db_gen_vc(event, chnl_name, chnl_id, member_name, member_id, guild_id):
    if tc.db_gen_vc is True:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cn.input_one('tigbot.db', 'generated_vc_hist', (event, str(chnl_name), int(chnl_id), member_name, str(member_id), int(guild_id), now))
    else:
        pass
    return


# log bot events to the "bot_logs" table
async def log_db_bot_events(event_type, event, guild_id, guild_name):
    if tc.db_bot_events is True:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cn.input_one('tigbot.db', 'bot_logs', (event_type, str(event), int(guild_id), str(guild_name), now))
    else:
        pass
    return


# log execution of slash commands to "command_calls" table
async def log_db_slash_commands(member_id, permission_level, message, message_id, guild_id):
    if tc.db_slash_commands is True:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cn.input_one('tigbot.db', 'command_calls', (int(member_id), str(permission_level), str(message), int(message_id), int(guild_id), now))
    else:
        pass
    return


# log ai conversations to "ai_logs" table
async def log_db_ai_conversations(username, userid, user_ai_prompt, ai_response, guild_id):
    if tc.db_ai_conversations is True:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cn.input_one('tigbot.db', 'ai_logs', (str(username), int(userid), str(user_ai_prompt), str(ai_response), int(guild_id), now))
    else:
        pass
    return