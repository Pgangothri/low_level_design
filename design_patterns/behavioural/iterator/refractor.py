from typing import Iterator, List, Optional, Protocol


# ========== Video class representing a single video ==========
class Video:
    def __init__(self, title: str) -> None:
        # Store video title
        self._title = title

    def get_title(self) -> str:
        # Return the title
        return self._title


# ========== Iterator interface (defines traversal contract) ==========
class PlaylistIterator(Protocol):
    def has_next(self) -> bool: ...

    def next(self) -> Optional[Video]: ...


# ========== Concrete Iterator class ==========
class YouTubePlaylistIterator:
    def __init__(self, videos: List[Video]) -> None:
        # Store the list reference
        self._videos = videos

        # Track current index
        self._position = 0

    def has_next(self) -> bool:
        # Check if we still have elements
        return self._position < len(self._videos)

    def next(self) -> Optional[Video]:
        # Return None when iteration finishes
        if not self.has_next():
            return None

        # Return current item and move forward
        video = self._videos[self._position]
        self._position += 1
        return video


# ================ Playlist interface ================
# Acts as a contract for collections that are iterable
class Playlist(Protocol):
    def create_iterator(self) -> PlaylistIterator: ...


# ========== YouTubePlaylist class (Aggregate) ==========
# Collection provides iterator, client never sees internal list
class YouTubePlaylist:
    def __init__(self) -> None:
        # Internal list of videos
        self._videos: List[Video] = []

    def add_video(self, video: Video) -> None:
        # Add a video to playlist
        self._videos.append(video)

    def create_iterator(self) -> PlaylistIterator:
        # Each call returns a new iterator (independent traversal state)
        return YouTubePlaylistIterator(self._videos)


# ========== Main method (Client code) ==========
def main() -> None:
    # Create a playlist and add videos to it
    playlist = YouTubePlaylist()
    playlist.add_video(Video("LLD Tutorial"))
    playlist.add_video(Video("System Design Basics"))

    # Client simply asks for an iterator
    iterator = playlist.create_iterator()

    # Iterate through the playlist using the provided interface
    while iterator.has_next():
        video = iterator.next()
        # Defensive check in case next() returns None
        if video is not None:
            print(video.get_title())


if __name__ == "__main__":
    main()
