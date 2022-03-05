from ClassesAndObjectsExercise.projectSpootify.song import Song

class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = songs
        self.published = False
        self.album_songs = [song for song in self.songs]

    def add_song(self, song):
        if song in self.album_songs:
            return f"Song is already in the album."

        if self.published:
            return "Cannot add songs. Album is published."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        else:
            self.album_songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."



    def remove_song(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."
        else:
            for song in self.album_songs:
                if song.name == song_name:
                    self.album_songs.remove(song)
                    return f"Removed song {song_name} from album {self.name}."
            return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        else:
            return f"Album {self.name} is already published."

    def details(self):
        message = f"Album {self.name}\n"
        for song in self.album_songs:
            message += f"== {song.get_info()}\n"
        return message


