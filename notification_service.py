import time


class NotificationService:

    @staticmethod
    def send_notification(appointment_id, user_id):

        print("========================================")
        print("Sending Notification...")
        print(f"Appointment Id : {appointment_id}")
        print(f"User Id        : {user_id}")

        time.sleep(3)

        print("Notification Sent Successfully")
        print("========================================")