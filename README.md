# MyDiscordBot
```

```

DiscordBotを自作します

**目標**：Githubへcommitした際に、通知を飛ばせるようにする。

**現在の進捗**：Githubへの接続完了。Githubの方を調査。



### 実行方法

①環境を作ります。まずはbuildから

```
docker build -t discordbot .
```

②runしてstartさせる

```sh
docker container run -itd --name ubuntu discordbot
docker start ubuntu
```

③起動後に中に入ります

```
docker container exec -it ubuntu /bin/bash
```

④コードを実行

```
python3 bot.py
```

