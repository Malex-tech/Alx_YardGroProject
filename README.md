YardGro

A digital platform reducing food loss by connecting farmers, aggregators, logistics providers, and buyers in Nigeria.

YardGro creates a transparent agricultural supply chain by enabling real-time produce tracking, optimized delivery logistics, and reporting on food wastage.

1. Project Overview

YardGro is a modular, API-driven system with a Django backend (Django REST Framework). The frontend will initially use Django templates (for rapid integration testing) with React planned later.

Core Goals:

Track agricultural produce availability.

Streamline delivery and logistics workflows.

Provide dashboards and reporting on food wastage metrics.

Offer REST APIs for future mobile or third-party integrations.

2. Features

User Roles

Admin – manage platform and all users

Farmers – register farms and produce

Logistics Partners – list vehicles, routes, and capacity

Delivery Agents – handle produce transport

Buyers – request produce and deliveries

Core Functions

User registration and authentication (token-based)

Farm and produce listing with quantities and prices

Logistics routing and transporter availability

Delivery request management and status tracking

Data reporting on deliveries and food wastage

Full REST API for all operations

3. Technology Stack

Backend: Django, Django REST Framework (DRF)

Frontend (current): Django Templates

Frontend (future): React SPA

Database: SQLite for development, PostgreSQL planned for production

Version Control: GitHub

Planned Integrations:

Google Maps API (routing optimization)

Twilio / Email API (notifications)

4. Data Models

User – username, email, role, password, location, phone number

Farm – owner, farm name, location, size, produce types

Produce – farm, name, quantity, price, harvest date, status

Logistics – transporter, vehicle type, capacity, availability, route, contact

Delivery – produce, buyer, transporter, pickup/destination, status, ETA, distance

Report – user, type, content, created_at timestamp

5. API Endpoints

Endpoint	Method	Description

/api/register/	POST	Register a new user
/api/login/	POST	Login and retrieve token
/api/farms/	GET / POST	List or create farms
/api/produce/	GET / POST	List or create produce entries
/api/logistics/	GET / POST	View or create logistics offers
/api/deliveries/	GET / POST / PUT	Manage delivery records
/api/reports/	GET / POST	Submit or view reports

6. Current Progress

Project idea finalized – ✔

Repository and Django scaffold – ✔

User authentication configured – ✔

Farm, Produce, Logistics, Delivery, Report models implemented – ✔

API endpoints working and tested (Postman & templates) – ✔

Frontend using Django templates (integration phase) – ✔

7. Roadmap – 5 Week Plan

Week	Focus

1	Planning, ERD design, GitHub setup, authentication
2	Implement Farm, Produce, Logistics models
3	Add Delivery and Report systems, complete APIs
4	Integrate Django template frontend with backend
5	Dashboard, full testing, documentation & walkthrough

Next Steps:

Build dashboard summarizing deliveries, wastage, and metrics.

Implement template-level authentication (remove manual token copy).

Perform full system testing and bug fixes.

Prepare final demo video and documentation.

8. How to Run the Project (Development)

# Clone the repository

git clone <repo-url>

cd Alx_YardGroProject

# Create virtual environment and install dependencies

python -m venv venv

source venv/bin/activate        # On Windows: venv\Scripts\activate

pip install -r requirements.tx

# Run migrations

python manage.py makemigrations

python manage.py migrate

# Start development server

python manage.py runserver

API Root URLs
farms:      http://127.0.0.1:8000/api/farms/
produce:    http://127.0.0.1:8000/api/produce/
logistics:  http://127.0.0.1:8000/api/logistics/
deliveries: http://127.0.0.1:8000/api/deliveries/
reports:    http://127.0.0.1:8000/api/reports/

9. Authentication Workflow

Login to get token

curl -X POST -d "username=<your_username>&password=<your_password>" \
http://127.0.0.1:8000/api/login/


Response:

{ "access": "<ACCESS_TOKEN>", "refresh": "<REFRESH_TOKEN>" }


Use the access token for API calls

curl -H "Authorization: Bearer <ACCESS_TOKEN>" \
http://127.0.0.1:8000/api/farms/

10. Contributors

Alex Alexander – Project Lead

Open collaboration welcome! Submit pull requests or issues.