# ======= Base type for play quality =======
class PlayQuality:
    def play(self, title: str) -> None:
        raise NotImplementedError


# Each class here represents a combination of platform and quality


class WebHDPlayer(PlayQuality):
    def play(self, title: str) -> None:
        # Web player plays in HD
        print(f"Web Player: Playing {title} in HD")


class MobileHDPlayer(PlayQuality):
    def play(self, title: str) -> None:
        # Mobile player plays in HD
        print(f"Mobile Player: Playing {title} in HD")


class SmartTVUltraHDPlayer(PlayQuality):
    def play(self, title: str) -> None:
        # Smart TV plays in Ultra HD
        print(f"Smart TV: Playing {title} in ultra HD")


class Web4KPlayer(PlayQuality):
    def play(self, title: str) -> None:
        # Web player plays in 4K
        print(f"Web Player: Playing {title} in 4K")


def main() -> None:
    # Client must pick a combined class
    player: PlayQuality = WebHDPlayer()

    # Play a movie
    player.play("Interstellar")


if __name__ == "__main__":
    main()
