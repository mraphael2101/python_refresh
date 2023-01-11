"""
Polymorphism is the ability to treat a class differently, depending on which
subclass is implemented

Polymorphism allows us to access overridden methods and attributes that have
the same name as the parent class
"""


class AudioFile:
    """
    Did you notice how the __init__ method in this parent class is able to
    access the ext class variable from the different subclasses? That's Polymorphism
    """
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid File Format")

        self.filename = filename


class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print("Playing {} as mp3".format(self.filename))


class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print("Playing {} as wav".format(self.filename))


"""
Python goes an extra step past allowing a subclass of an object to be treated
like a parent class with the Duck typing concept: If it walks like a duck or 
swims like a duck, it's a duck

Duck typing which allows us to use any object that provides the required 
behaviour without forcing it to be a subclass i.e. when multiple-inheritance 
appears to be a valid solution we can use duck typing to mimic one of the 
multiple superclasses. Thereby reducing the need for Polymorphic objects as 
a result of the above.

Another flexible characteristic of Duck typing is that it only needs to
fulfill the interface that is actually accessed and not the entire interface
"""


"""
The below example does not extend AudioFile, but it can be interacted with
in Python using the exact same interface
"""


class OggFile:
    # This is an example of Duck typing
    def __init__(self, filename):
        if not filename.endswith("ogg"):
            raise Exception("Invalid File Format")

        self.filename = filename

    def play(self):
        print("Playing {} as ogg".format(self.filename))


def main():
    mp3 = MP3File("myfile.mp3")
    mp3.play()
    wav = WavFile("myfile.wav")
    wav.play()
    ogg = OggFile("myfile.error")
    ogg.play()


if __name__ == "__main__":
    main()
