# EmailNotification handles sending emails
class EmailNotification:
    def send(self, to, message):
        print("Checking rate limits for:", to)
        print("Validating email recipient:", to)
        formatted = message.strip()
        print("Logging before send:", formatted, "to", to)

        # Compose Email
        composedMessage = "<html><body><p>" + formatted + "</p></body></html>"

        # Send Email
        print("Sending EMAIL to", to, "with content:\n" + composedMessage)

        # Analytics
        print("Analytics updated for:", to)


# SMSNotification handles sending SMS messages
class SMSNotification:
    def send(self, to, message):
        print("Checking rate limits for:", to)
        print("Validating phone number:", to)
        formatted = message.strip()
        print("Logging before send:", formatted, "to", to)

        # Compose SMS
        composedMessage = "[SMS] " + formatted

        # Send SMS
        print("Sending SMS to", to, "with message:", composedMessage)

        # Analytics (custom)
        print("Custom SMS analytics for:", to)


if __name__ == "__main__":
    # Create objects for both notification services
    emailNotification = EmailNotification()
    smsNotification = SMSNotification()

    # Sending email notification
    emailNotification.send("example@example.com", "Your order has been placed!")

    print()

    # Sending SMS notification
    smsNotification.send("1234567890", "Your OTP is 1234.")
