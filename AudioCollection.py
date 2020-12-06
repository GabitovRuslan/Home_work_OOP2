class Track:
    info_track = []

    def __init__(self, name_track, duration):
        self.name_track = name_track
        self.duration = duration

    def __str__(self):
        return f'{self.name_track} - {self.duration} мин.'

    def __le__(self, other):
        if not isinstance(other, Track):
            print('Not Track class!')
        return self.duration < other.duration

    def __eq__(self, other):
        if not isinstance(other, Track):
            print('Not Track class!')
        return self.duration == other.duration

    def __gt__(self, other):
        if not isinstance(other, Track):
            print('Not Track class!')
        return self.duration > other.duration


class Album:
    def __init__(self, name_album, group):
        self.name_album = name_album
        self.group = group
        self.track_list = []
        self.rt = []

    def add_tracks(self, track):
        self.track_list.append(track)

    def get_duration(self):
        max_time = sum(x.duration for x in self.track_list)
        print(f'Общая длина всех треков {max_time}')

    def __str__(self):
        print(f'Name group: {self.name_album}\nName album: {self.group}\nTracks:')
        for track in self.track_list:
            print(f'        {track.__str__()}')


track1 = Track('"Фантазер"', 3)
track2 = Track('"Лалал"', 5)
track3 = Track('"Тра-та"', 5)
track4 = Track('"Ра-ра-ра"', 8)
track5 = Track('"Фан"', 7)
track6 = Track('"Буум>"', 6)
album_apple = Album('На-на', 'Яблоко')
album_one = Album('ДДТ', 'Один')
album_apple.add_tracks(track1)
album_apple.add_tracks(track2)
album_apple.add_tracks(track3)
album_one.add_tracks(track4)
album_one.add_tracks(track5)
album_one.add_tracks(track6)
# album_apple.get_tracks()
# album_apple.get_tracks()
print(album_apple)
# print(album_one)
print(track3 == track2)
