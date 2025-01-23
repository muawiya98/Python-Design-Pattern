from command.command import Command

class LightOnCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.ON()

    def unexecute(self):
        self.light.OFF()