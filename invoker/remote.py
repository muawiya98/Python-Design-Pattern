from command.no_command import NoCommand

class Remote:

    def __init__(self):
        self.on_command = []
        self.off_command = []
        self.last_command = NoCommand()
        self.party_command = NoCommand()

    def set_command(self, index, on_command, off_command):
        if (len(self.on_command)-1) >= index:
            self.on_command[index] = on_command
            self.off_command[index] = off_command
        else:
            self.on_command.append(on_command)
            self.off_command.append(off_command)

    def set_party_command(self, party_command):
        self.party_command = party_command
    
    def on_button_pressed(self, index):
        self.on_command[index].execute()
        self.last_command = self.on_command[index]

    
    def off_button_pressed(self, index):
        self.off_command[index].execute()
        self.last_command = self.off_command[index]

    def undo_command(self):
        self.last_command.unexecute()

    def party_buttom_pressed(self):
        self.party_command.execute()
        self.last_command = self.party_command


    

    