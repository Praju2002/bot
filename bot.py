import discord
import config
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)

routine = {
    "Sunday": [("Maths", "7:00-8:40"), ("Instrumentation", "8:40-10:20 "), ("Project hour", "11:10-2:30")],
    "Monday":[("Maths", "7:00-8:40"), ("Instrumentation", "8:40-10:20 "), ("DBMS" ,"11:10-12:50"),("Project hour", "12:50-2:30")],
    "Tuesday":[("Instrumentation", "7:00-8:40"), ("Programming technology", "8:40-10:20 "), ("Programming technology LAB" ,"11:10-12:50"),("Project hour", "12:50-2:30")],
    "Wednesday":[("Programming technology", "7:00-8:40"), ("Microprocessor", "8:40-10:20 "), ("DBMS" ,"11:10-12:50"),("Instrumentation LAB", "12:50-2:30")],
    "Thursday":[("DBMS LAB", "7:00-8:40"), ("Microprocessor", "8:40-10:20 "), ("Programming technology" ,"11:10-12:50"),("Microprocessor LAB", "12:50-2:30")],
    "Friday":[("DBMS", "7:00-8:40"), ("Microprocessor", "8:40-10:20 "), ("Maths" ,"11:10-12:50")]
}

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.command()
async def schedule(ctx):
 header = ["Day", "Classes"]
 rows = []
 for day, classes in routine.items():
        class_info = "\n".join(["{} ({})".format(c[0], c[1]) for c in classes])
        rows.append([day, class_info])
 output = "```"
 for i, row in enumerate(rows):
        day = row[0].ljust(10)
        classes = row[1]
        if i == 0:
            output += "|".join([header[0].ljust(10), header[1].ljust(50)]) + "\n"
            output += "-" * 65 + "\n"
        output += "|".join([day, classes.ljust(50)]) + "\n"
        if i != len(rows) - 1:
            output += "\n"  # Add a line break after each day's schedule
 output += "```"
 await ctx.send(output)

bot.run(config.TOKEN)
