header_identifier = 13241241434555123123  # not yet important

# contains databases and their tables. the keys define the database names, the values are lists with the pre-defined table names from "custom_tables"

# !!DB NAMES MUST END IN .db OR CONFIG IS NOT VALID!!
# contains all databases the user wants to create and a list with the tables to be put in each
custom_databases = {'jokes.db': ['jokes', 'total_req'], 'tigbot.db': ['ai_logs', 'bot_logs', 'generated_vc', 'generated_vc_hist', 'user_data', 'user_message_log', 'message_blacklist', 'image_blacklist', 'restrictions', 'command_calls', 'proxy_userdata', 'proxy_history']}

# keys are defining table names, values are the names of defined variables from "custom_vars"
custom_tables = {'jokes': ['joke', 'type'],
                 'total_req': ['num_of_req', 'event'],
                 'ai_logs': ['username', 'userid', 'user_ai_prompt', 'ai_response', 'guild_id','timestamp'],
                 'bot_logs': ['event_type', 'event', 'guild_id', 'guild_name', 'timestamp'],
                 'generated_vc': ['vc_name', 'vc_id', 'guild_id'],
                 'generated_vc_hist': ['event', 'vc_name', 'vc_id', 'username', "userid", 'guild_id', 'timestamp'],
                 'user_data': ["username", "nickname", 'userid', 'join_date', "restriction", 'guild_id', 'timestamp'],
                 'user_message_log': ["username", "userid", "message", "message_id", "channel_id", "guild_id", 'timestamp'],
                 'message_blacklist': ["banned_text", "triggered_restriction", 'subject_roles', 'exempt_roles', 'guild_id', 'timestamp'],
                 'image_blacklist': ["banned_image_hash", "triggered_restriction", 'subject_roles', 'exempt_roles', 'guild_id', 'timestamp'],
                 'restrictions': ["restriction", "restriction_length", "progressing", "progression_time", "progression_increment", 'guild_id'],
                 'command_calls': ["command", "userid", "permission_level", "message", "message_id", 'guild_id', 'timestamp'], # user calls of commands
                 'proxy_userdata': ["event", 'event_id', "userid", 'username', 'timestamp'],
                 'proxy_history': ['sender_id', 'reciever_id', 'timestamp']
                }

# custom variables for table construction. the keys are the variable names, the values are the type of data being stored from "vars_types".
custom_vars = {"reciever_id": "str",   # the username of a user
               "sender_id": "str",   # the username of a user
               "username": "str",   # the username of a user
               "nickname": "str",  # the discord username of a user
               "userid": "str", # the userid of a discord user
               "timestamp": "str",  # the time of an event in unix form
               "ai_response": "str",  # the response of the ai to the user
               "user_ai_prompt": "int",  # the index of the user comment that was responded to
               "event_type": "str",  # the type of log event
               "event": "str",  # the event message or traceback
               "vc_name": "str",    # the name of the generated vc
               "vc_id": "int",  # the id of the generated vc
               "join_date": "int",  # the unix timestamp of the user join date
               "user_status": "str",  # the current state of the user from bot interactions
               "permission_level": "str",  # the permission level of the user at the last update
               "banned_text": "str",  # the permission level of the user at the last update
               "triggered_restriction": "str",  # the result of breaking the rules
               "banned_image_hash": "str",  # the permission level of the user at the last update
               "subject_roles": "str",  # the roles that a rule applies to
               "exempt_roles": "str",   # the roles that are exempted from a rule
               "message": "str",    # the message data
               "message_id": "int",    # the message data from a particular user
               "message_sender": "str",    # the user who sent the message
               "restriction": "str",    # the restriction/punishment for an action
               "restriction_length": "str",  # the amount on time and metric for the punishment
               "progressing": "int",    # 1 or 0 signifies if the punishment gets worse with every offence
               "progression_time": "str",    # the time after which a punishment progression resets and the metric (sec, minute, hour, day, year)
               "progression_increment": "str",    # the increment of the restriction upon punishment within the set time period (sec, minute, hour, day, year)
               "channel_id": "int",    # the id of a discord channel
               "guild_id": "int",    # the id of the guild an event occurred
               "guild_name": "str",    # the name of a guild (server)
               "command": "str",    # the name of a command called
               "num_of_req": "str",    # the name of a command called
               "joke": "str",    # the name of a command called
               "type": "str",    # the name of a command called
               "event_id": "str",    # the name of a command called
               "other": "str",  # stores other information that is not yet determined
              }

# default available variables types for variable construction. All sqlite3 data types are represented
vars_types = {"str": "TEXT",
              "int": "INTEGER",
              "float": "REAL",
              "null": "NULL",
              "images": "BLOB"
              }


