# from spoopify_8.project.album import Album
# from spoopify_8.project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = list()

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        album.published = True
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for al in self.albums:
            if al.name == album_name:
                if al.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(al)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        line_one = f"Band {self.name}\n"
        text = ""
        for al in self.albums:
            text += f"{al.details()}"

        return line_one + text

#
# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
