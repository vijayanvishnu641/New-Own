# Implement By https://github.com/jusidama18
# Based on this https://github.com/DevsExpo/FridayUserbot/blob/master/plugins/updater.py

import sys
import subprocess
import heroku3

from datetime import datetime
from os import environ, execle, path, remove

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from pyrogram import filters

from bot import app, OWNER_ID, UPSTREAM_REPO, UPSTREAM_BRANCH
from bot.helper import runcmd, get_text, HEROKU_URL
from bot.helper.telegram_helper.bot_commands import BotCommands

REPO_ = UPSTREAM_REPO
BRANCH_ = UPSTREAM_BRANCH

# Update Command

@app.on_message(filters.command(BotCommands.UpdateCommand) & filters.user(OWNER_ID))
async def update_it(client, message):
    msg_ = await message.reply_text("`Updating Please Wait!`")
    try:
       if len(UPSTREAM_REPO) == 0:
         raise TypeError
       except:
         UPSTREAM_REPO = None
    try:
       if len(UPSTREAM_BRANCH) == 0:
         raise TypeError
    except:
       UPSTREAM_BRANCH = 'master'

    if UPSTREAM_REPO is not None:
       if ospath.exists('.git'):
         srun(["rm", "-rf", ".git"])

       update = srun([f"git init -q \
                     && git config --global user.email e.anastayyar@gmail.com \
                     && git config --global user.name mltb \
                     && git add . \
                     && git commit -sm update -q \
                     && git remote add origin {UPSTREAM_REPO} \
                     && git fetch origin -q \
                     && git reset --hard origin/{UPSTREAM_BRANCH} -q"], 
       await msg_.edit(f"`Updated Sucessfully! \n\nCheck your config with` `/{BotCommands.ConfigMenuCommand}`")
