import discord
from discord.ext import commands
import os

# ---------- Configuration ----------
TOKEN = os.environ.get("DISCORD_TOKEN", "Bot-Token")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "608963234534572920"))  # target channel ID
USERNAME = "Michael Jackson"           # display name shown in the message
PHOTO_PATH = "Michael-Jackson.jpg"          # path to the photo file
MESSAGE_TEXT = "I think so!"   # text to send with the photo
# ----------------------------------

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("Bot is ready.")

    # --- Set the bot's username and avatar ---
    if os.path.exists(PHOTO_PATH):
        with open(PHOTO_PATH, "rb") as f:
            icon = f.read()
        await bot.user.edit(username=USERNAME, avatar=icon)
        print(f"Avatar set to {PHOTO_PATH} and username changed to '{USERNAME}'.")
    else:
        print(f"Photo file not found: {PHOTO_PATH} — skipping avatar update.")

    # --- Send the message ---
    await send_message()


async def send_message():
    """Send a plain text message to the designated channel."""
    channel = bot.get_channel(CHANNEL_ID)
    if channel is None:
        channel = await bot.fetch_channel(CHANNEL_ID)

    if channel is None:
        print(f"Could not find channel with ID {CHANNEL_ID}. Check your configuration.")
        return

    await channel.send(content=MESSAGE_TEXT)
    print(f"Message sent to #{channel.name}.")


@bot.command(name="sendmsg")
async def sendmsg_command(ctx):
    """Manually trigger: !sendmsg"""
    await send_message()


if __name__ == "__main__":
    if TOKEN == "YOUR_BOT_TOKEN_HERE":
        raise SystemExit("Set the DISCORD_TOKEN environment variable first.")
    bot.run(TOKEN)