import sys
from discord.ext import commands
from modules import Cohere
sys.path.append("..")


class Grammar(commands.Cog):
    """Bot Information"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def translate(self, ctx, language):
        reply = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        message = f"The translated message into {language} is {Cohere.get_translation(language, reply.content)}"
        await ctx.reply(message)

    @commands.command()
    async def correct(self, ctx):
        reply = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        message = f"The corrected grammar is:{Cohere.get_corrected_grammar(reply.content)}"
        await ctx.reply(message)

async def setup(client):
    await client.add_cog(Grammar(client))
