from receiver.fan import Fan
from receiver.light import Light
from command.fan_speed_down_command import FanSpeedDownCommand
from command.fan_speed_up_command import FanSpeedUpCommand
from command.light_off_command import LightOffCommand
from command.light_on_command import LightOnCommand
from invoker.remote import Remote
from command.party_command import PartyCommand



class CommandTester:

    def run(self):
        remote = Remote()
        fan = Fan("Room1")
        light = Light("Room1")

        light_on = LightOnCommand(light)
        light_off = LightOffCommand(light)

        fan_up = FanSpeedUpCommand(fan)
        fan_down = FanSpeedDownCommand(fan)

        remote.set_command(0, light_on, light_off)
        remote.set_command(1, fan_up, fan_down)

        
        remote.on_button_pressed(0)
        remote.off_button_pressed(0)
        remote.undo_command()

        print(50*"*")

        remote.on_button_pressed(1)
        remote.on_button_pressed(1)
        remote.on_button_pressed(1)
        remote.undo_command()
        remote.undo_command()
        remote.undo_command()
        remote.undo_command()

        remote.off_button_pressed(1)

        print(50*"*")
        command_list = [light_on, fan_up]
        party_command = PartyCommand(command_list)
        remote.set_party_command(party_command)
        remote.party_buttom_pressed()
        remote.undo_command()



if __name__=="__main__":
    command_tester = CommandTester()
    command_tester.run()