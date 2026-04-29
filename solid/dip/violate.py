# Class implementing the recommendations based on recently added
class RecentlyAdded:
    # Method to get the recommendations
    def getRecommendations(self):
        print("Showing recently added content...")


# Class implementing the overall Recommendation Engine
class RecommendationEngine:
    def __init__(self):
        self.recommender = RecentlyAdded()

    def recommend(self):
        self.recommender.getRecommendations()
