from command.command import Command

class LightOffCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.OFF()

    def unexecute(self):
        self.light.ON()