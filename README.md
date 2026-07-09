# 🐍 MyKare - Python Notification Worker

A lightweight Python background worker that consumes appointment events from **Apache Kafka**, processes notifications asynchronously, and updates the appointment processing status in PostgreSQL.

This worker is designed to work alongside the **MyKare Spring Boot Backend** as part of an **Event-Driven Architecture**.

---

# 🚀 Project Overview

The Python Worker listens to Kafka events published by the Spring Boot backend whenever a new appointment is booked.

After receiving an event, it:

- Reads the appointment event from Kafka
- Processes the notification
- Updates the appointment processing status
- Logs the processing details

This demonstrates asynchronous background processing commonly used in modern distributed systems.

---<img width="1598" height="537" alt="Screenshot 2026-07-09 165637" src="https://github.com/user-attachments/assets/3bf565a2-ca63-4f2c-ac17-6cb301004cd3" />


# ⚡ Event Flow

```text
Patient Books Appointment
           │
           ▼
Spring Boot Backend
           │
           ▼
Publishes Event to Kafka
           │
           ▼
Apache Kafka Topic
           │
           ▼
Python Worker
           │
           ▼
Notification Processing
           │
           ▼
Update PostgreSQL Database
```

---

# ✨ Features

- Kafka Consumer
- JSON Event Processing
- PostgreSQL Integration
- Notification Service
- Processing Status Update
- Error Handling
- Event Logging

---

# 💻 Technology Stack

- Python 3.12
- Apache Kafka
- kafka-python
- PostgreSQL
- psycopg2

---

# 📂 Project Structure

```
healthcare-python-worker

│
├── consumer.py
├── config.py
├── database.py
├── notification_service.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📨 Kafka Event Example

The Spring Boot backend publishes events like:

```json
{
  "appointmentId": 15,
  "userId": 3,
  "doctorId": 6,
  "slotId": 14,
  "appointmentStatus": "BOOKED"
}
```

---

# 🔄 Processing Workflow

1. Consume Kafka Event
2. Deserialize JSON
3. Process Notification
4. Update Appointment Processing Status
5. Log Success / Failure

---

# 🗄 Database Update

The worker updates the appointment table.

Example:

```
processing_status

PENDING
        │
        ▼
NOTIFICATION_SENT
```

---

# ▶ Running the Worker

## Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Kafka

Make sure Apache Kafka is running.

Default Broker

```
localhost:9092
```

---

## Start Worker

```bash
python consumer.py
```

Console Output

```
======================================
 MyKare Python Worker Started
 Waiting for Appointment Events...
======================================
```

---

# ⚙ Configuration

Edit `config.py`

```python
KAFKA_BOOTSTRAP_SERVER = "localhost:9092"

TOPIC_NAME = "appointment-topic"

DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "studentdb"
DB_USER = "postgres"
DB_PASSWORD = "******"
```

---

# 📌 Responsibilities

The worker is responsible for:

- Consuming Kafka Events
- Notification Processing
- Updating Processing Status
- Logging Background Operations

It **does not** perform appointment booking or authentication. Those responsibilities belong to the Spring Boot backend.

---

# 🔗 Related Repositories

### Backend

Spring Boot Service

https://github.com/saikaladhar-namala/healthcare-appointment-service

---

### Frontend

React UI

https://github.com/saikaladhar-namala/healthcare-appointment-ui

---

# 🚀 Future Enhancements

- Email Notifications
- SMS Notifications
- WhatsApp Alerts
- Retry Mechanism
- Dead Letter Queue (DLQ)
- Docker Support
- Redis Integration
- Monitoring & Metrics

---

# 👨‍💻 Developed By

**Sai Kaladhar Namala**

Java Full Stack Developer

### Skills

Java • Spring Boot • Python • Apache Kafka • PostgreSQL • React.js • REST APIs • JWT • Hibernate

GitHub

https://github.com/saikaladhar-namala/

LinkedIn

https://www.linkedin.com/in/sai-kaladhar-namala-1415771a6/

---

⭐ If you found this project useful, consider giving it a Star.
