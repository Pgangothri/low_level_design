# Notification class
class Notification:
    # method implementing send notification functionality
    def sendNotification(self):
        print("Notification sent")


# Subclass of Notification class for Email Notification
class EmailNotification(Notification):
    def sendNotification(self):
        print("Email Notification sent")


# Subclass of Notification class for Text Notification
class TextNotification(Notification):
    def sendNotification(self):
        print("Text Notification sent")


# Main section
if __name__ == "__main__":
    """ Replaced the Notification class object
    with one of its subclass' objects """
    notification = EmailNotification()

    # Working code on the notification object
    notification.sendNotification()
