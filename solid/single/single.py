# Each class should have only one reason to change, meaning it should have only one responsibility.
# Notification class
class Notification:
    # method implementing send notification functionality
    def sendNotification(self):
        print("Notification sent")


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
