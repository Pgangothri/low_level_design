# ========== RealVideoDownloader Class ==========
class RealVideoDownloader:
    def download_video(self, video_url: str) -> str:
        # caching logic missing
        # filtering logic missing
        # access logic missing
        print(f"Downloading video from URL: {video_url}")

        content = f"Video content from {video_url}"
        print(f"Downloaded Content: {content}")
        return content


def main() -> None:
    print("User 1 tries to download the video.")

    # Client directly creates and uses the real downloader
    downloader1 = RealVideoDownloader()
    downloader1.download_video("https://video.com/proxy-pattern")

    print()
    print("User 2 tries to download the same video again.")

    # Another client again creates the real downloader
    downloader2 = RealVideoDownloader()
    downloader2.download_video("https://video.com/proxy-pattern")


if __name__ == "__main__":
    main()
