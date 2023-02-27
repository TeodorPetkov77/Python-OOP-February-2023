class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        else:
            return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str):
        for album in self.albums:
            if album.name == album_name:
                if album.published is True:
                    return f"Album has been published. It cannot be removed."
                else:
                    return f"Album {album_name} has been removed."
        else:
            return f"Album {album_name} is not found."

    def details(self):
        return f"Band {self.name}\n" + "\n".join([f'{album_info.details()}' for album_info in self.albums]) + "\n"


