import nextcord
from nextcord.ext import commands
import requests

class Check(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name='check', description='Check si un id est blacklist')
  async def check_slash(self, interaction: nextcord.Interaction, id: str = nextcord.SlashOption(name="id", description="L'id de l'utilisateur")):
    data = requests.post('https://backlist-api.angel-project.repl.co/check', json={"id": id})
    if data['blacklisted']:
      await interaction.response.send_message(embed=nextcord.Embed(title='Blacklist', description=f"Cette personne est blacklist!\n{data['raison']}", color=0xe74c3c))
      return
    await interaction.response.send_message("L'utilisateur n'est pas blacklist!")

def setup(bot):
  bot.add_cog(Check(bot))
