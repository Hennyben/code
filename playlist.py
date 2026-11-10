
class song:
    def __init__(self, title, artist, duration):
        self.title=title
        self.artist=artist
        self.duration=duration

class playlist:
    def __init__(self, name):
        self.name = name
        self.playlist=[]

    def add_song(self, song):
        self.playlist.append(song)

    def get_total_duration(self):
        total = 0
        for song in self.playlist:
            total += song.duration 
        minutes = total // 60
        seconds = total % 60
        print(minutes,":",seconds)

    def find_by_artist(self, artist_name):
        for song in self.playlist:
            print(song.title)    

    def print_playlist(self):
        print(self.name)
        for song in self.playlist:
            print(song.title,song.artist)

    def load_songs(self, filename):
         with open(filename, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row:
                    new_song = song(row[0], row[1], int(row[2]))
                    self.add_song(new_song)

        

def main():
    my_playlist = playlist("My Playlist")
    my_playlist.load_songs("songs.csv")
    my_playlist.add_song(song("My Fav Song", "Megabytes", 250))
    my_playlist.print_playlist()
    my_playlist.get_total_duration()
    my_playlist.find_by_artist("Null Pointer")
