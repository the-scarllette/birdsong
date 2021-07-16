# BirdSong
Birdsong is a small program that plays bird songs. You enter in the name of the bird, and it plays it's song.

## Usages
The program takes a users entry and checks it against the list of bird names in masterbirdlist.txt. If the bird name is
found, it searches for recordings of that bird's song using the xeno-canto api. If any are found, it downloads them and
plays the first one found.

UserInterface.py handles the events and front-end logic.

BirdManager.py manages searching for bird songs and downloadng them.

layout.ky describes the GUI and aesthetics of the program.

## Limitations
There are two big limitations to the project in it's current state:

**Precise Bird Names**
<br>The program only plays the song if you enter in the common american name for a specific bird. For example if you
enter 'eagle' the program won't play a song, but putting in 'bald eagle' plays the correct song for that bird.</br>

**Limited Bird Names**
<br>Right now the program can only play the songs of about 170 birds. This is due to the fact that it validates an entry
by checking it against the stored list of bird names in masterbirdlist.txt. Updating this list or finding another way to
validate the entries would allow the program to play a wider range of bird songs.</br>

## References
The GUI was built using [Kivy](https://kivy.org/#home).

The bird songs are downloaded from the [xeno-canto](https://www.xeno-canto.org/) website, a collaborative database
that collects and categorises bird songs. The program uses the Pytho xeno-canto API wrapper which you can find
[here](https://github.com/ntivirikin/xeno-canto-py).

Pixel art for the pause and play buttons was made using [Piskel](https://www.piskelapp.com/).

The heading font is the Playball font from [fontsc](https://www.fontsc.com/).

## Project Roadmap and Status
The main aditions I would like to add to the project would be:
- Increasing the number of birds that the program can play
- A nicer GUI
- Making an Android smartphone version of the project.

My main focus is turning the project into a smartphone app, but after reaching the milestone of the project reaching a
level of functionality I am going to return to focusing on my other projects and work on this only on occasion.

## Acknowledgements
If I didn't play Elizabeth Hargrave's wonderful board game Wingspan I wouldn't have made this at all. You can find
Wingspan [here](https://stonemaiergames.com/games/wingspan/) and Eizabeth's website
[here](https://www.elizhargrave.com/).

## Liscense
[MIT](https://choosealicense.com/licenses/mit/)