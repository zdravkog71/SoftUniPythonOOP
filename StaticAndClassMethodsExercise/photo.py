import math

class PhotoAlbum:
    PHOTOS_PER_PAGE = 4
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
        self.page_slot_index = 1

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = math.ceil(photos_count / cls.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        max_index = self.pages * PhotoAlbum.PHOTOS_PER_PAGE
        if self.page_slot_index <= max_index:
            page = math.ceil(self.page_slot_index / PhotoAlbum.PHOTOS_PER_PAGE)
            self.photos[page - 1].append(label)
            self.page_slot_index += 1
            return f"{label} photo added successfully on page {page} slot {(self.page_slot_index - 1) % PhotoAlbum.PHOTOS_PER_PAGE}"
        return "No more free slots"

    def display(self):
        message = f"{'-' * 11}\n"
        for page in self.photos:
            message += " ".join(str([]) for _ in page)
            # if page:
            #     " ".join([[] for _ in range(len(page))]).strip()
            # for pic in page:
            #     message += "[] "
            # message = message.strip()
            message += f"\n{'-' * 11}\n"
        return message


# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())

album = PhotoAlbum(1)
album.add_photo("baby")
album.add_photo("first grade")
album.add_photo("eight grade")
album.add_photo("party with friends")
print(album.photos)
print(album.display())