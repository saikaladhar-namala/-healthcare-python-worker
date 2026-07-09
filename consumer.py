import json

from kafka import KafkaConsumer

from config import KAFKA_BOOTSTRAP_SERVER, TOPIC_NAME
from notification_service import NotificationService
from database import update_appointment_status

print("======================================")
print(" MyKare Python Worker Started ")
print(" Waiting for Appointment Events...")
print("======================================")

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
    auto_offset_reset="latest",
    enable_auto_commit=True,
    group_id="appointment-worker"
)
for message in consumer:

    try:

        raw = message.value.decode("utf-8")

        print(raw)

        event = json.loads(raw)

        appointment_id = event["appointmentId"]

        user_id = event["userId"]

        NotificationService.send_notification(
            appointment_id,
            user_id
        )

        update_appointment_status(
            appointment_id,
            "NOTIFICATION_SENT"
        )

        print("Completed")

    except Exception as ex:

        print(f"Skipping Invalid Message : {ex}")

    try:

        raw_message = message.value.decode("utf-8")

        print("\nReceived:")
        print(raw_message)

        event = json.loads(raw_message)

        appointment_id = event["appointmentId"]
        user_id = event["userId"]

        print(f"Processing Appointment : {appointment_id}")

        NotificationService.send_notification(
            appointment_id,
            user_id
        )

        update_appointment_status(
            appointment_id,
            "NOTIFICATION_SENT"
        )

        print("Processing Completed Successfully")

    except Exception as ex:

        print(f"Error : {ex}")