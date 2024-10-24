import discord
from discord.ext import commands
import discord.app_commands
from constant import TOKEN

intents = discord.Intents.all()

client = discord.Client(intents=discord.Intents.all())

# discordとbotの接続
intents = discord.Intents.default()
intents.message_content = True

# クライアントの作成
client = discord.Client(intents=intents)

# コマンドツリーの作成
tree = discord.app_commands.CommandTree(client)

# 起動イベント
@client.event
async def on_ready():
    print("Ready 🚀")

extensions = (
    "extensions.hoge",
    # "extensions.huga",
)

# コマンドの同期処理
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned,
            intents=discord.Intents.all(),
        )

    async def setup_hook(self):
        # await self.tree.sync(guild=None)
        for extension in extensions:
            print("Loading ",extension)
            await self.load_extension(extension)

if __name__ == "__main__":
    MyBot().run(TOKEN)