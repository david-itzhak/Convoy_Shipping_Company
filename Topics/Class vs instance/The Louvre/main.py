class Painting:
    museum = 'Louvre'

    def __init__(self, title_: str, artist_: str, year_: int):
        self.title_: str = title_
        self.artist_: str = artist_
        self.year_: int = year_
        print(f'"{self.title_}" by {self.artist_} ({self.year_}) hangs in the {Painting.museum}.')


title: str = input()
artist: str = input()
year: int = int(input())

some_painting = Painting(title, artist, year)