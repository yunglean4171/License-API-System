import discord
from discord.ext import commands
import requests
import os
import json

file_path = os.path.abspath(os.path.dirname(__file__))
cfgpath = f"{file_path}/config.json"

with open(cfgpath, "r") as cfg:
    data = json.load(cfg)

token = data['token']
secretkey = data['secretkey']
apiurl = data['apiurl']

dclient = commands.Bot(command_prefix="!")
dclient.remove_command("help")


@dclient.event
async def on_ready():
    print(f"{dclient.user} is online [✔️]")
    await dclient.change_presence(status=discord.Status.online, activity=discord.Game(name="yunglean_#4171 license system"))

@dclient.command()
async def help(ctx):
    await ctx.channel.send("```Available commands:```***!add <license> <id> \n!delete <license> \n!check <license> <id>***")

@dclient.command()
async def add(ctx, arg1, arg2):
    response = requests.post(apiurl + f"/add/{secretkey}/{arg1}/{arg2}")
    await ctx.channel.send(f"***{response.json()}***")

@dclient.command()
async def delete(ctx, arg1):
    response = requests.delete(apiurl + f"/del/{secretkey}/{arg1}")
    await ctx.channel.send(f"***{response.json()}***")

@dclient.command()
async def check(ctx, arg1, arg2):
    response = requests.get(apiurl + f"/{arg1}/{arg2}")
    if response.json() == "true":
       await ctx.channel.send(f"__{arg1}__ - license exist with given id - __{arg2}__")
    elif response.json() == "false":
       await ctx.channel.send(f"__{arg1}__ - license does not exist with given id - __{arg2}__")

dclient.run(token)