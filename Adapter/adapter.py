
class MediaPlayer:
    def play_audio(self, filename):
        raise NotImplementedError("Subclasses must implement this method")


class Mp3Player:
    def play_mp3(self, filename):
        print(f"Playing MP3 file: {filename}")


class Mp4Player:
    def play_mp4(self, filename):
        print(f"Playing MP4 file: {filename}")


class Mp4ToMediaPlayerAdapter(MediaPlayer):
    def __init__(self, mp4_player: Mp4Player):
        self.mp4_player = mp4_player

    def play_audio(self, filename):
        
        self.mp4_player.play_mp4(filename)


class AudioClient:
    def __init__(self, player: MediaPlayer):
        self.player = player

    def play(self, filename):
        self.player.play_audio(filename)


if __name__ == "__main__":

    mp3_player = Mp3Player()
    audio_client = AudioClient(mp3_player)
    print("Playing with MP3 Player:")
    mp3_player.play_mp3("song.mp3")  


    mp4_player = Mp4Player()
    mp4_adapter = Mp4ToMediaPlayerAdapter(mp4_player)
    audio_client = AudioClient(mp4_adapter)
    print("\nPlaying with MP4 Player via Adapter:")
    audio_client.play("video.mp4")  
