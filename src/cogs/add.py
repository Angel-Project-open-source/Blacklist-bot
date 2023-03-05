import nextcord
from nextcord.ext import commands
import requests, os
token = os.environ['tokan']

class Add(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name='blacklist', description='Blacklist quelqu\'un')
  async def Blacklist_slash(self, interaction: nextcord.Interaction, id: str = nextcord.SlashOption(name="id", description="L'id de l'utilisateur"), raison: str = nextcord.SlashOption(name="raison", description="La raison du blacklistement")):
    if interaction.channel.id != 1081813642808414228: return
    requests.post('https://backlist-api.angel-project.repl.co/add', json={"id": id, 'raison': raison, 'token': token})
    await interaction.response.send_message("Fait!")

def setup(bot):
  bot.add_cog(Add(bot))
