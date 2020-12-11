class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song):
        if self.published:
            return "Cannot add songs. Album is published."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        elif song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        for s in self.songs:
            if self.published:
                return "Cannot remove songs. Album is published."
            else:
                if s.name == song_name:
                    self.songs.remove(s)
                    return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        return f"Album {self.name} has been published."

    def details(self):
        line_one = f"Album {self.name}\n"
        text = ""
        for s in self.songs:
            text += '== ' + s.get_info() + '\n'

        return line_one + text