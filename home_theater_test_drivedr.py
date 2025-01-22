from amplifier import Amplifier
from tuner import Tuner
from DVD_player import DVDPlayer
from CD_player import CDPlayer
from porjector import Projector
from theater_lights import TheaterLights
from screen import Screen
from popcorn_popper import PopcornPopper
from home_theater_facade import HomeTheaterFacade


class HomeTheaterTestDriver:

    def run(self):
        amp = Amplifier('Top-o-Line Amplifier')
        tuner = Tuner('Top-o-Line AM/FM Turner', amp)
        dvd = DVDPlayer('Top-o-Line DVD Player', amp)
        cd = CDPlayer('Top-o-Line CD Player', amp)
        projector = Projector('Top-o-Line Projector', dvd)
        light = TheaterLights('Theater Ceilling Lights')
        screen = Screen('Theater Screen')
        popper = PopcornPopper('Poppcoen Popper')

        home_theater = HomeTheaterFacade(amp, tuner, dvd, cd, projector, screen, light, popper)

        home_theater.watch_movie('Raiders of the Lost Ark')
        home_theater.end_movie()
        



if __name__=="__main__":
    home_theater_test_driver = HomeTheaterTestDriver()
    home_theater_test_driver.run()