class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song):
        if song.single is True:
            return f"Cannot add {song.name}. It's a single"
        if self.published is True:
            return f"Cannot add songs. Album is published."
        if song in self.songs:
            return f"Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published is False:
            for song in self.songs:
                if song.name == song_name:
                    self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
            else:
                return "Song is not in the album."
        else:
            return "Cannot remove songs. Album is published."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        else:
            return f"Album {self.name} is already published."

    def details(self):
        return f"Album {self.name}\n" + "\n".join([f'== {song_info.get_info()}' for song_info in self.songs]) + "\n"
