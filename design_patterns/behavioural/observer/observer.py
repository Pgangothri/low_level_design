from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import weakref


# ==============================
# Observer Interface
# ==============================
class Subscriber(ABC):
    @abstractmethod
    def update(self, video_title: str) -> None:
        # Each subscriber decides how it wants to react
        raise NotImplementedError


# ==============================
# Concrete Observer: Email
# ==============================
class EmailSubscriber(Subscriber):
    def __init__(self, email: str) -> None:
        # Store the receiver email
        self.email = email

    def update(self, video_title: str) -> None:
        print(f"Email sent to {self.email}: New video uploaded - {video_title}")


# ==============================
# Concrete Observer: Mobile App
# ==============================
class MobileAppSubscriber(Subscriber):
    def __init__(self, username: str) -> None:
        # Store the app username
        self.username = username

    def update(self, video_title: str) -> None:
        print(f"In-app notification for {self.username}: New video - {video_title}")


# ==============================
# Subject Interface
# ==============================
class Channel(ABC):
    @abstractmethod
    def subscribe(self, subscriber: Subscriber) -> None:
        raise NotImplementedError

    @abstractmethod
    def unsubscribe(self, subscriber: Subscriber) -> None:
        raise NotImplementedError

    @abstractmethod
    def notify_subscribers(self, video_title: str) -> None:
        raise NotImplementedError


# ==============================
# Concrete Subject: YouTubeChannel
# ==============================
class YouTubeChannel(Channel):
    def __init__(self, channel_name: str) -> None:
        # Store the channel name
        self.channel_name = channel_name

        # Store subscribers as weak references to reduce memory leak risk
        self._subscribers: "weakref.WeakSet[Subscriber]" = weakref.WeakSet()

    def subscribe(self, subscriber: Subscriber) -> None:
        # Add the observer
        self._subscribers.add(subscriber)

    def unsubscribe(self, subscriber: Subscriber) -> None:
        # Remove the observer (if present)
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def notify_subscribers(self, video_title: str) -> None:
        # Notify every active subscriber
        for subscriber in list(self._subscribers):
            subscriber.update(video_title)

    def upload_video(self, video_title: str) -> None:
        # Simulate upload
        print(f"{self.channel_name} uploaded: {video_title}\\n")

        # Trigger notifications
        self.notify_subscribers(video_title)


# ==============================
# Client Code
# ==============================
def main() -> None:
    # Create a YouTube channel (subject)
    tuf = YouTubeChannel("takeUforward")

    # Create subscribers (observers)
    mobile = MobileAppSubscriber("raj")
    email = EmailSubscriber("rahul@example.com")

    # Subscribe observers to the subject
    tuf.subscribe(mobile)
    tuf.subscribe(email)

    # Upload video and notify all observers
    tuf.upload_video("observer-pattern")


if __name__ == "__main__":
    main()
