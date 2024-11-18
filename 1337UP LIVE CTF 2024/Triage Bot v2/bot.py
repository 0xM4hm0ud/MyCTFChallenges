import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
import json

load_dotenv()
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

TOKEN = os.getenv("DISCORD_TOKEN")
client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command("help")

def load_reports():
    with open("reports.json", "r") as file:
        return json.load(file)

reports = load_reports()

images_dir = 'images/'
image_files = [f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))]

@client.event
async def on_ready():
    print("The bot is ready to use!")

@client.command()
async def news(ctx):
    update_message = (
        "🚀 **Second Beta Version!** 🚀\n\n"
        "We've made some exciting changes:\n"
        "- Removed the AI component in the Triage process after some security and performance issues.\n"
        "- Added a new **!read_report** function to allow for manual triage.\n"
        "- Removed the **!anyupdate** option due to an overwhelming number of 'any update?' requests.\n"
    )
    await ctx.send(update_message)

@client.command()
async def support(ctx):
    await ctx.send("Sorry, Joe is busy right now!")

@client.command()
async def bountyplz(ctx):
    random_image = random.choice(image_files)
    image_path = os.path.join(images_dir, random_image)
    await ctx.send(file=discord.File(image_path))

@client.command()
@commands.has_role("triage")
async def read_report(ctx, report_id: str = None):
    if report_id:
        report = reports.get(report_id)

        if report:
            embed = discord.Embed(
                title=f"Report {report_id} - {report['title']}",
                description=report['description'],
                color=discord.Color.blue()
            )
            embed.add_field(name="CWE", value=report["cwe"], inline=True)
            embed.add_field(name="CVSS Score", value=report["cvss"], inline=True)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"No report found with ID {report_id}.")
    else:
        filtered_reports = {k: v for k, v in reports.items() if k != "0"}

        if filtered_reports:
            random_id = random.choice(list(filtered_reports.keys()))
            report = filtered_reports[random_id]
            embed = discord.Embed(
                title=f"Report {random_id} - {report['title']}",
                description=report['description'],
                color=discord.Color.green()
            )
            embed.add_field(name="CWE", value=report["cwe"], inline=True)
            embed.add_field(name="CVSS Score", value=report["cvss"], inline=True)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No reports are currently available.")

@client.command()
async def triage(ctx):
    try:
        await ctx.send("Sorry, we've got more than enough reports for now!")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@client.command()
async def help(ctx):
    embed = discord.Embed(title="TriageBot", url="https://www.intigriti.com/",
                          description="The official Intigriti Triage Bot!", color=0x0099ff)
    embed.set_author(name=ctx.bot.user.display_name,
                     url="https://www.intigriti.com", icon_url=ctx.bot.user.avatar)
    embed.set_thumbnail(url=ctx.bot.user.avatar)
    embed.add_field(name="**Commands**", value="**!help** - Show this menu\n**!news** - What's new?\n**!support** - Ask for support\n**!bountyplz** - Get a bounty\n**!triage** - Triage a bug", inline=True)
    embed.set_footer(text="beta v2")
    await ctx.send(embed=embed)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        return

    await client.process_commands(message)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("\nYou don't have permissions to run this command! If you are a triager, please contact IT to be assigned the triage role.")

client.run(TOKEN)
