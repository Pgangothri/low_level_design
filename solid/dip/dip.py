from abc import ABC, abstractmethod


# Interface provided for classes to implement different recommendation strategies
class RecommendationStrategy(ABC):
    @abstractmethod
    def getRecommendations(self):
        pass


# Class implementing recommendations based on recently added
class RecentlyAdded(RecommendationStrategy):
    def getRecommendations(self):
        print("Showing recently added content...")


# Class implementing recommendations based on trending now
class TrendingNow(RecommendationStrategy):
    def getRecommendations(self):
        print("Showing trending content...")


# Class implementing recommendations based on Genre
class GenreBased(RecommendationStrategy):
    def getRecommendations(self):
        print("Showing content based on your favorite genres...")


# Class implementing the Recommendation Engine (High - level module)
class RecommendationEngine:
    def __init__(self, strategy: RecommendationStrategy):
        self.strategy = strategy

    def recommend(self):
        self.strategy.getRecommendations()


# Main driver code
if __name__ == "__main__":
    strategy = TrendingNow()  # could also be RecentlyAdded or GenreBased
    engine = RecommendationEngine(strategy)
    engine.recommend()
