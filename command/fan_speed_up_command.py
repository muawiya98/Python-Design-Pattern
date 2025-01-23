from command.command import Command

class FanSpeedUpCommand(Command):

    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.speed_up()

    def unexecute(self):
        self.fan.speed_down()