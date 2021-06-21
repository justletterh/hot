from dep import *

token = read("./token.txt")
pfx = "h."
client = commands.Bot(case_insensitive=True,command_prefix=pfx,intents=discord.Intents.all(),help_command=commands.DefaultHelpCommand(no_category="Default"))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='h'),status=discord.Status('dnd'))
    print(f"We Have Logged In As @{client.user.name}#{client.user.discriminator} <@!{client.user.id}>!!!")

class Fun(commands.Cog):
    @commands.command(pass_context=True,name="ping",brief="Pong!!!")
    async def _ping(self,ctx):
        await ctx.send("Pong!!!")

    @commands.command(pass_context=True,name="pong",brief="Ping!!!")
    async def _pong(self,ctx):
        await ctx.send("Ping!!!")
    
    @commands.command(pass_context=True,name="owo",brief=owo("I must scream"))
    async def _owo(self,ctx):
        msg=ctx.message.content[len(pfx+"owo "):]
        await ctx.send(owo(msg))

class Lifestyle(commands.Cog):
    @commands.command(pass_context=True,name="h",brief="h")
    async def _h(self,ctx):
        await ctx.message.add_reaction(u'\U0001f1ed')
        h=await ctx.send("h")
        await h.add_reaction(u'\U0001f1ed')

client.add_cog(Lifestyle())
client.add_cog(Fun())
client.load_extension("jishaku")

client.run(token)