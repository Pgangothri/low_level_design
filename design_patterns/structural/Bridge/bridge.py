from abc import ABC, abstractmethod

# ======== Implementor Interface =========
class VideoQuality(ABC):
    @abstractmethod
    def load(self, title: str) -> None:
        pass

# ============ Concrete Implementors ==============
class SDQuality(VideoQuality):
    def load(self, title: str) -> None:
        print(f"Streaming {title} in SD Quality")

class HDQuality(VideoQuality):
    def load(self, title: str) -> None:
        print(f"Streaming {title} in HD Quality")

class UltraHDQuality(VideoQuality):
    def load(self, title: str) -> None:
        print(f"Streaming {title} in 4K Ultra HD Quality")

# ========== Abstraction ==========
class VideoPlayer(ABC):
    def __init__(self, quality: VideoQuality) -> None:
        # Composition: platform holds a quality implementation
        self.quality = quality

    @abstractmethod
    def play(self, title: str) -> None:
        pass

# =========== Refined Abstractions ==============
class WebPlayer(VideoPlayer):
    def play(self, title: str) -> None:
        print("Web Platform:")
        self.quality.load(title)

class MobilePlayer(VideoPlayer):
    def play(self, title: str) -> None:
        print("Mobile Platform:")
        self.quality.load(title)

def main() -> None:
    # Playing on Web with HD Quality
    player1 = WebPlayer(HDQuality())
    player1.play("Interstellar")

    print()

    # Playing on Mobile with Ultra HD Quality
    player2 = MobilePlayer(UltraHDQuality())
    player2.play("Inception")

    print()

    # Runtime flexibility: swap quality without changing platform class
    player3 = WebPlayer(SDQuality())
    player3.play("The Dark Knight")

if __name__ == "__main__":
    main()