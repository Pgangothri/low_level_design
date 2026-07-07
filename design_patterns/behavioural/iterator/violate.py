from typing import List


# A simple Video class with title
class Video:
    def __init__(self, title: str) -> None:
        # Store video title
        self._title = title

    def get_title(self) -> str:
        # Return the title
        return self._title


# YouTubePlaylist class holds a list of Video objects
class YouTubePlaylist:
    def __init__(self) -> None:
        # Internal list of videos
        self._videos: List[Video] = []

    def add_video(self, video: Video) -> None:
        # Add a video to playlist
        self._videos.append(video)

    def get_videos(self) -> List[Video]:
        # Expose internal list (this is the main design issue)
        return self._videos


# Client Code
def main() -> None:
    playlist = YouTubePlaylist()
    playlist.add_video(Video("LLD Tutorial"))
    playlist.add_video(Video("System Design Basics"))

    # Loop through videos and print titles
    for v in playlist.get_videos():
        print(v.get_title())


if __name__ == "__main__":
    main()
