# This page contains the event logs and designated outputs

import os
import discord
import datetime
import main

current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

log_exists = any('log.txt' in filename for filename in os.listdir(current_directory))
if not log_exists:
    with open('log.txt', 'w') as log_file:
        print("'log.txt' has been created in the current directory.")
else:
    print("'log.txt' already exists in the current directory.")

# This function generates a new log file at 1000 lines
def new_log_file():
    return

# This function logs the servers that the bot is currently in
def curr_servers():
    with open('log_file', 'a'):
        log_file.write('CURRENT SERVERS:\n')

# This function logs information on the commands executed
def commands(event, user):
    current_datetime = datetime.datetime.utcnow()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f'{event} - {user} - {formatted_datetime}\n'
    print(formatted_datetime)
    with open('log_file', 'a'):
        log_file.write("COMMANDS:\n")
        log_file.write(log_entry + '\n\n')

commands(event, user)

# This function logs when a new member joins the server
def new_member():
    with open('log_file', 'a'):
        log_file.write('NEW MEMBERS:\n')

# This function logs when a member leaves the server
def lost_member():
    with open('log_file', 'a'):
        log_file.write('LOST MEMBERS:\n')