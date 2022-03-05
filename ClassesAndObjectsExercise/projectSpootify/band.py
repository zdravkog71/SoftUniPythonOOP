from ClassesAndObjectsExercise.projectSpootify.album import Album
from ClassesAndObjectsExercise.projectSpootify.song import Song

class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        for album in self.albums:
            if album.name == album_name:
                if album.published:
                    return f"Album has been published. It cannot be removed."
                else:
                    self.albums.remove(album)
                    return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        message = f"Band {self.name}\n"
        for album in self.albums:
            message += f"{album.details()}\n"
        return message


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
album1 = Album("The Sound of Perseverance")
song1 = Song("Scavenger of Human Sorrow", 6.56, False)
print(album1.add_song(song1))
print(album1.add_song(song1))