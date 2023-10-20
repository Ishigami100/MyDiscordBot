# インストールした discord.py を読み込む
import discord
import os
from dotenv import load_dotenv
from discord import Intents

# .envファイルの内容を読み込見込む
load_dotenv()

# 自分のBotのアクセストークンに置き換えてください
TOKEN = os.environ['TOKEN']
intents = Intents.default()  # 一般的なイベントを有効化
intents.messages = True # タイピングイベントを無効化
# 接続に必要なオブジェクトを生成
client = discord.Client(intents=intents)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
