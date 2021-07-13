from random import choice


def strip_bird_name(to_strip):
    return ''.join([x.capitalize() for x in to_strip.split()])


class birdmanager:

    def __init__(self):
        self.all_birds_filename = "masterbirdlist.txt"
        self.used_birds_filename = "usedbirdlist.txt"
        self.audio_drct = "dataset/audio/"

        with open(self.all_birds_filename, "r") as f:
            self.all_birds = f.read().splitlines()

    def add_used_bird(self, bird_to_add):
        with open(self.used_birds_filename, "a") as f:
            f.write(bird_to_add + "\n")

    def choose_bird(self):
        with open(self.all_birds_filename, "r") as f:
            birds = f.read().splitlines()
        with open(self.used_birds_filename, "r") as f:
            used_birds = f.read().splitlines()

        while True:
            bird = choice(birds)
            if bird not in used_birds:
                break

        return bird

    def is_valid_bird(self, to_check):
        return to_check in self.all_birds

