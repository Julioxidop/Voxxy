import nextcord
from nextcord.ext import commands
from helper import log, guilds, loadJson, dumpJson

#Builds, Modder, Plugins, Modelos, Comandos, Animaciones
#emoji: rol_id
info = {
    "🏗":1087193706517499985, 
    "⚙":1087193819860185178, 
    "🔑":1087193888290246796,
    "🕹":1087193767385251963,
    "💾":1087263343473070111,
    "📟":1087453360501825586
    }

class Autorol(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        log('MAIN', 'Cog AUTOROL cargado.')
    
    @nextcord.slash_command(name='autorol', description='Enviar el mensaje para añadir autoroles', guild_ids=guilds)
    async def revertir(self, interaction: nextcord.Interaction):
        msgstr = "**¡Hola! Esto lo hacemos para saber que puedes hacer y de que eres capaz.**\nPorfavor elije tu especialidad para acceder a tu trabajo:"
        for emoji in list(info.keys()):
            rol = interaction.guild.get_role(info[str(emoji)])
            msgstr = f"{msgstr}\n{emoji} {rol.name}"
        msg = await interaction.channel.send(msgstr)
        for emoji in list(info.keys()):
            await msg.add_reaction(emoji)
        data = loadJson('data.json')
        data['autorol'].append(msg.id)
        dumpJson('data.json', data)
        await interaction.send("Mensaje enviado", ephemeral=True)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: nextcord.RawReactionActionEvent):
        data = loadJson('data.json')['autorol']
        if payload.message_id in data and payload.member.bot == False:
            guild = await self.client.fetch_guild(payload.guild_id)
            rol = guild.get_role(info[str(payload.emoji)])
            await payload.member.add_roles(rol)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: nextcord.RawReactionActionEvent):
        data = loadJson('data.json')['autorol']
        if payload.message_id in data:
            guild = await self.client.fetch_guild(payload.guild_id)
            rol = guild.get_role(info[str(payload.emoji)])
            member = await guild.fetch_member(payload.user_id)
            await member.remove_roles(rol)
    
    @nextcord.message_command(name = 'Actualizar', guild_ids=guilds, default_member_permissions=8198)
    async def actualizar(self, interaction: nextcord.Interaction, ctx):
        msgstr = "**¡Hola! Esto lo hacemos para saber que puedes hacer y de que eres capaz.**\nPorfavor elije tu especialidad para acceder a tu trabajo:"
        for emoji in list(info.keys()):
            rol = interaction.guild.get_role(info[str(emoji)])
            msgstr = f"{msgstr}\n{emoji} {rol.name}"
        await ctx.edit(content=msgstr)
        for emoji in list(info.keys()):
            await ctx.add_reaction(emoji)

    
def setup(client):
    client.add_cog(Autorol(client))
