from abc import ABC, abstractmethod
from typing import Dict


class VideoDownloader(ABC):
    @abstractmethod
    def download_video(self, video_url: str) -> str:
        pass


# ========== RealVideoDownloader Class ==========
class RealVideoDownloader(VideoDownloader):
    def download_video(self, video_url: str) -> str:
        print(f"Downloading video from URL: {video_url}")
        return f"Video content from {video_url}"


# =============== Proxy With Cache ====================
class CachedVideoDownloader(VideoDownloader):
    def __init__(self) -> None:
        # Real downloader is created once and reused
        self._real_downloader = RealVideoDownloader()

        # Cache stores downloaded content by URL
        self._cache: Dict[str, str] = {}

    def download_video(self, video_url: str) -> str:
        # If present, return cached content
        if video_url in self._cache:
            print(f"Returning cached video for: {video_url}")
            return self._cache[video_url]

        # Cache miss, call the real downloader
        print("Cache miss. Downloading...")
        content = self._real_downloader.download_video(video_url)

        # Store for future requests
        self._cache[video_url] = content
        return content


def main() -> None:
    # Client depends only on the interface
    downloader: VideoDownloader = CachedVideoDownloader()

    print("User 1 tries to download the video.")
    downloader.download_video("https://video.com/proxy-pattern")

    print()
    print("User 2 tries to download the same video again.")
    downloader.download_video("https://video.com/proxy-pattern")


if __name__ == "__main__":
    main()
