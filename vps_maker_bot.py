
import os
import requests
import discord
from discord.ext import commands

TOKEN = "YOUR_DISCORD_BOT_TOKEN"  # Replace with your bot token
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

def get_public_ipv4():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        return response.json().get("ip", "IPv4 not found")
    except:
        return "Error fetching IPv4"

@bot.command()
async def create_vps(ctx, user: discord.Member, ram: str, cpu: str, disk: str):
    """ Creates a VPS with given resources and sends details to the specified user """
    
    # Simulating VPS creation (Replace with actual VPS deployment logic)
    ipv4_address = get_public_ipv4()
    ssh_access = f"ssh root@{ipv4_address}"

    message = f"""
    ✅ VPS Created! ✅
    - User: {user.mention}
    - RAM: {ram} GB
    - CPU: {cpu} Cores
    - Disk: {disk} GB
    - IPv4: `{ipv4_address}`
    - SSH Access: `{ssh_access}`

    📩 Check your DM for login details!
    """
    
    await ctx.send(message)
    await user.send(f"Your VPS Details:\n{message}")

bot.run(TOKEN)
