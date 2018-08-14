from apollo.services import SyncModels


class OnReady:

    def __init__(self, bot):
        self.bot = bot


    async def on_ready(self):
        print(f"{self.bot.user.name} - Ready")
        SyncModels(self.bot).call()
