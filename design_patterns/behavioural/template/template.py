# Abstract class defining the template method and common steps
class NotificationSender:
    def send(self, to, raw_message):
        # Template method
        self.rate_limit_check(to)
        self.validate_recipient(to)
        formatted = self.format_message(raw_message)
        self.pre_send_audit_log(to, formatted)

        composed_message = self.compose_message(formatted)
        self.send_message(to, composed_message)

        self.post_send_analytics(to)

    def rate_limit_check(self, to):
        print(f"Checking rate limits for: {to}")

    def validate_recipient(self, to):
        print(f"Validating recipient: {to}")

    def format_message(self, message):
        return message.strip()  # Just trims whitespaces

    def pre_send_audit_log(self, to, formatted):
        print(f"Logging before send: {formatted} to {to}")

    # Abstract methods to be implemented by subclasses
    def compose_message(self, formatted_message):
        raise NotImplementedError

    def send_message(self, to, message):
        raise NotImplementedError

    def post_send_analytics(self, to):
        print(f"Analytics updated for: {to}")


# Concrete class for Email notifications
class EmailNotification(NotificationSender):
    def compose_message(self, formatted_message):
        return f"{formatted_message}"

    def send_message(self, to, message):
        print(f"Sending EMAIL to {to} with content:\n{message}")


# Concrete class for SMS notifications
class SMSNotification(NotificationSender):
    def compose_message(self, formatted_message):
        return f"[SMS] {formatted_message}"

    def send_message(self, to, message):
        print(f"Sending SMS to {to} with message: {message}")

    def post_send_analytics(self, to):
        print(f"Custom SMS analytics for: {to}")


# Client code
def main():
    email_sender = EmailNotification()
    email_sender.send("john@example.com", "Welcome to TUF+!")

    sms_sender = SMSNotification()
    sms_sender.send("9876543210", "Your OTP is 4567.")


if __name__ == "__main__":
    main()
