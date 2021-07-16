from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.config import Config

from BirdManager import birdmanager, strip_bird_name

import xenocanto

from os import listdir

play_image = "assets/play.png"
pause_image = "assets/pause.png"

Config.set("graphics", "height", 170)
Config.set("graphics", "width", 300)

Builder.load_file("layout.kv")


class UserInterface(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bird_manager = birdmanager()

        self.song_playing = False

    def on_enter(self):
        entry = self.ids["bird_input"].text.lower()
        if entry not in self.bird_manager.all_birds:
            self.ids["message_label"].text = "No Matching bird found"
            return
        xenocanto.download([entry, "q:a", "len:25-30"])

        self.play_pause()

        bird_song_filename = listdir(self.bird_manager.audio_drct + strip_bird_name(entry))[0]
        self.song_playing = SoundLoader.load(self.bird_manager.audio_drct + strip_bird_name(entry) +
                                          "/" + bird_song_filename)

        self.ids["message_label"].text = self.ids["bird_input"].text

        if self.song_playing:
            self.song_playing.play()

    def play_pause(self):
        if self.song_playing:
            if self.song_playing.state == 'play':
                self.song_playing.stop()
                self.ids["pause_button"].background_normal = play_image
            else:
                self.song_playing.play()
                self.ids["pause_button"].background_normal = pause_image


class MyApp(App):

    def build(self):
        return UserInterface()


if __name__ == '__main__':
    MyApp().run()
