from nextcord.ext import commands
import nextcord
import logging
import logging.config
import datetime
from os import listdir
from os import listdir
from os.path import isfile, join
from helper import log, loadJson, dumpJson, guilds


exclude_cogs = []

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})
filenamelog = f"./logs/logfile {str(datetime.datetime.now()).replace(':','.')}.txt"
logging.basicConfig(level=logging.DEBUG, filename=filenamelog, filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")

intents = nextcord.Intents.all()
client = commands.Bot(intents = intents)

@client.event
async def on_ready():
	"""
	Mensaje de feedback cuando el bot esta activo
	"""
	await client.wait_until_ready()
	log('MAIN','======================================================================')
	log('MAIN',f'        [ {client.user} ] listo para trabajar!')
	log('MAIN','======================================================================')

	activity = nextcord.Game("Vox Studio Bot, me creó @hugme#8792")
	await client.change_presence(activity = activity)


if __name__=='__main__':
	for cog in listdir('./cogs'):
		if cog.endswith('.py') == True and cog[:-3] not in exclude_cogs:
			client.load_extension(f'cogs.{cog[:-3]}')

client.run("")
