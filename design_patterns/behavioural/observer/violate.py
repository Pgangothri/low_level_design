# ==============================
# Naive Subject: YouTubeChannel
# ==============================
class YouTubeChannel:
    def upload_new_video(self, video_title: str) -> None:
        # Upload the video
        print(f"Uploading: {video_title}\\n")

        # Manually notify users (hardcoded)
        print("Sending email to user1@example.com")
        print("Pushing in-app notification to user3@example.com")


# ==============================
# Client Code
# ==============================
def main() -> None:
    # Create a channel and upload a new video
    channel = YouTubeChannel()
    channel.upload_new_video("Design Patterns in Python")


if __name__ == "__main__":
    main()
