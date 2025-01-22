
class HomeTheaterFacade:
    
    def __init__(self, amp, tuner, dvd, cd, projector, screen, light, popper):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd
        self.projector = projector
        self.screen = screen
        self.light = light
        self.popper = popper

    def watch_movie(self, movie):
        print("Get ready to watch a movie")
        self.popper.cn()
        self.popper.pop()
        self.light.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen()
        self.amp.on()
        self.amp.set_dvd(self.dvd)
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)
    
    def end_movie(self):
        print('Shutting movie theater down...')
        self.popper.off()
        self.light.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()
    
    def listen_to_cd(self, cd_title):
        print('Get ready for an audiopile experence...')
        self.light.on()
        self.amp.on()
        self.amp.set_volume(5)
        self.amp.set_cd(self.cd)
        self.amp.set_surround_sound()
        self.cd.on()
        self.cd.play(cd_title)

    def end_cd(self):
        print('Shutting down CD...')
        self.amp.off()
        self.amp.set_cd(self.cd)
        self.cd.eject()
        self.cd.off()

    def listen_to_radio(self, frequency):
        print('Tuning in the airwaves...')
        self.tuner.on()
        self.tuner.set_frequency(frequency)
        self.amp.on()

    def end_radio(self):
        print('Shutting down the tuner...')
        self.tuner.off()
        self.amp.off()


        




