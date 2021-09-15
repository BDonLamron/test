import requests
from discord import SyncWebhook

webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/887652449425453138/uGbGN4jxouTBPZIFsV9W2ygR9BeA2fHa2A5Tz7kdEosc9rXqxP1wvyfOX08t_7vu61DW")
webhook.send("aaaaa")