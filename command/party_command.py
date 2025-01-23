from command.command import Command

class PartyCommand(Command):

    def __init__(self, commandes):
        self.commandes = commandes

    def execute(self):
        for command in self.commandes:
            command.execute()
        
    def unexecute(self):
        for ind in range(len(self.commandes)-1, -1, -1):
            self.commandes[ind].unexecute()
