class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        print("-" * 20)
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy Birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there."])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells."])

mm = Song(["Well the FCC",
           "Won't let me be",
           "Or let me be me",
           "So let me see",
           "They try to shut me down on MTV",
           "But it feels so empty",
           "WITHOUT ME."])

coldPlay = ["I hear Jerusalem bells are ringing", 
            "Roman cavalry choirs are singing."]

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

mm.sing_me_a_song()
# this doesn't work but I'm unsure why
# error says the 'str' object has no attribute, sing_me_a_song()
coldPlay.sing_me_a_song()
# the below DOES work in that it prints but not using class, Song
print(coldPlay)

'''
Notes for Exercise 40: Modules, Classes, and Objects
1. I still don't really understand why the
   def__init__() function is necessary in the class
   Need to investigate further. Possibly on YouTube?
2. asdf
'''