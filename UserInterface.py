from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.audio import SoundLoader

from BirdManager import birdmanager, strip_bird_name

import xenocanto

from os import listdir


class UserInterface(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bird_manager = birdmanager()
        self.cols = 1
        self.add_widget(Label(text="Bird Song Player"))
        search_grid = GridLayout()
        search_grid.cols = 2
        search_grid.add_widget(Label(text="Enter bird name:"))

        self.bird_input = TextInput(multiline=False)
        self.bird_input.bind(on_text_validate=self.on_enter)
        search_grid.add_widget(self.bird_input)
        self.add_widget(search_grid)

        self.message_label = Label(text="")
        self.add_widget(self.message_label)

    def on_enter(self, instance):
        entry = self.bird_input.text.lower()
        if entry not in self.bird_manager.all_birds:
            self.message_label.text = "No Matching bird found"
            return
        xenocanto.download([entry, "q:a", "len:25-30"])

        bird_song_filename = listdir(self.bird_manager.audio_drct + strip_bird_name(entry))[0]
        bird_song_file = SoundLoader.load(self.bird_manager.audio_drct + strip_bird_name(entry) +
                                          "/" + bird_song_filename)

        self.message_label.text = "Playing the bird song of " + self.bird_input.text

        if bird_song_file:
            bird_song_file.play()


class MyApp(App):

    def build(self):
        return UserInterface()


if __name__ == '__main__':
    MyApp().run()
