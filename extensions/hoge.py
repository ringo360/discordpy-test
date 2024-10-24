import discord
from discord.ext import commands
from discord import app_commands

# cogの読み込み
class __Cog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

        # cogの起動処理
        @commands.Cog.listener()
        async def on_ready(self):
            print("Cog ready!")

        @app_commands.command(name="example", description="test")
        async def est(interaction: discord.Interaction):
            await interaction.response.send_message('It works! ✨')

async def setup(bot):
    print('hoge is ready 🔥')
