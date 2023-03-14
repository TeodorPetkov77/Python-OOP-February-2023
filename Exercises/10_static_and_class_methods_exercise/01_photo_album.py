class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for i in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = photos_count // 4 + 1 if photos_count % 4 != 0 else photos_count // 4
        return cls(pages)

    def add_photo(self, label: str):
        for index, page in enumerate(self.photos):
            if len(page) < 4:
                self.photos[index].append(label)
                return f"{label} photo added successfully on page {index + 1} " \
                       f"slot {self.photos[index].index(label)}"
        return "No more free slots"

    def display(self):
        result = "-----------\n"
        for page in self.photos:
            result += f"{' '.join(['[]' for i in range(len(page))])}\n"
            result += "-----------\n"
        return result
