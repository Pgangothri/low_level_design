from typing import List, Optional, Protocol


# ========== Video class representing a single video ==========
class Video:
    def __init__(self, title: str) -> None:
        # Store video title
        self._title = title

    def get_title(self) -> str:
        # Return the title
        return self._title


# ========== YouTubePlaylist class (Aggregate) ==========
class YouTubePlaylist:
    def __init__(self) -> None:
        # Internal list of videos
        self._videos: List[Video] = []

    def add_video(self, video: Video) -> None:
        # Add a video to playlist
        self._videos.append(video)

    def get_videos(self) -> List[Video]:
        # Expose internal list (still not ideal)
        return self._videos


# ========== Iterator interface ==========
class PlaylistIterator(Protocol):
    def has_next(self) -> bool: ...

    def next(self) -> Optional[Video]: ...


# ========== Concrete Iterator class ==========
class YouTubePlaylistIterator:
    def __init__(self, videos: List[Video]) -> None:
        # Store the reference to the list we iterate on
        self._videos = videos

        # Track current position
        self._position = 0

    def has_next(self) -> bool:
        # Check if more videos are left
        return self._position < len(self._videos)

    def next(self) -> Optional[Video]:
        # If no next element, return None
        if not self.has_next():
            return None

        # Return current element and move forward
        video = self._videos[self._position]
        self._position += 1
        return video


# ========== Main method (Client code) ==========
def main() -> None:
    # Create a playlist and add videos
    playlist = YouTubePlaylist()
    playlist.add_video(Video("LLD Tutorial"))
    playlist.add_video(Video("System Design Basics"))

    # Client directly creates the iterator using internal list (not ideal)
    iterator: PlaylistIterator = YouTubePlaylistIterator(playlist.get_videos())

    # Use the iterator to loop through the playlist
    while iterator.has_next():
        video = iterator.next()
        # Defensive check in case next() returns None
        if video is not None:
            print(video.get_title())


if __name__ == "__main__":
    main()
