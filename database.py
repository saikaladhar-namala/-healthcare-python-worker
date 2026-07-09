import psycopg2
from config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)

def get_connection():

    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


def update_appointment_status(appointment_id, status):

    connection = None
    cursor = None
    try:

        connection = get_connection()
        cursor = connection.cursor()

        query = """
            UPDATE appointment  SET processing_status = %s, updated_date = CURRENT_TIMESTAMP WHERE appointment_id = %s
        """

        cursor.execute(query, (status, appointment_id))
        connection.commit()
        print(
            f"Appointment {appointment_id} updated successfully to '{status}'."
        )

    except Exception as ex:
        print(f"Database Error : {ex}")

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()