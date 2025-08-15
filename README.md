# YardGro

**YardGro** is a digital platform designed to reduce food loss and wastage in Nigeria by connecting farmers, aggregators, logistics providers, and buyers.  
The platform enables real-time produce tracking, optimised delivery logistics, and monitoring to create a transparent agricultural supply chain.

---

## **Project Overview**

YardGro is being developed as a modular, API-driven system with a Django backend (Django REST Framework) and a frontend that will be integrated later using either React or Django templates.

The platform aims to:
- Track agricultural produce availability.
- Streamline delivery and logistics processes.
- Provide dashboards and reporting for wastage metrics.
- Support future mobile app integration via REST APIs.

---

## **Features**

### **User Roles**
- **Admin** (platform owner)  
- **Farmers** – list farms and produce  
- **Logistics Partners** – register vehicles, routes, and capacity  
- **Delivery Agents** – handle delivery of produce  
- **Buyers** – request and receive deliveries  

### **Key Functions**
- User registration and login (Token authentication)
- Farm and produce listing
- Logistics vehicle routing and availability
- Delivery request and status tracking
- Reporting on deliveries and wastage
- REST API endpoints for all core operations

---

## **Technology Stack**
- **Backend:** Django, Django REST Framework (DRF)  
- **Frontend (Planned):** React or Django templates (to be decided after integration test)  
- **Database:** SQLite (development), PostgreSQL (production planned)  
- **Version Control:** GitHub  

**Optional future integrations:**  
- Google Maps API (routing optimisation)  
- Twilio or Email API (notifications)  

---

## **Models Implemented**
1. **User** – username, email, role, password, location, phone number  
2. **Farm** – owner, farm name, location, size, produce types  
3. **Produce** – farm, name, quantity, price, harvest date, status  
4. **Logistics** – transporter, vehicle type, capacity, availability, route, contact  
5. **Delivery** – produce, buyer, transporter, pickup location, destination, status, ETA, distance  
6. **Report** – user, report type, content, created_at  

---

## **API Endpoints (Initial Draft)**

| Endpoint         | Method | Description                   |
|------------------|--------|-------------------------------|
| `/api/register/`  | POST   | User registration             |
| `/api/login/`     | POST   | User login/token authentication |
| `/api/farms/`     | GET/POST | List/Create farms             |
| `/api/produce/`   | GET/POST | List/Create produce           |
| `/api/logistics/` | GET/POST | View & create logistics offers |
| `/api/deliveries/`| GET/POST/PUT | Create & update delivery       |
| `/api/reports/`   | GET/POST | Submit and view reports        |

---

## **Progress**

- **Project idea finalized** – ✔  
- **Repository created** – ✔  
- **Django project scaffolded** – ✔  
- **User authentication setup** – ✔  
- **Farm model and endpoints added** – ✔  
- **Produce, Logistics, Delivery, and Report apps created** – ✔ (in progress adding serializers/views)  

---

## **5-Week Plan**

| Week | Focus |
|------|--------|
| **1** | Planning, ERD design, Django project setup, GitHub, user authentication |
| **2** | Implement models for Farm, Produce, and Logistics |
| **3** | Add Delivery and Report systems, complete API endpoints |
| **4** | Integrate frontend (React or Django template) |
| **5** | Full testing, build dashboard, record walkthrough, submit final project |

---

## **Next Steps**
- Complete DRF serializers and views for Produce, Logistics, Delivery, and Reports.  
- Add URL routing for all new apps.  
- Test endpoints using Postman or DRF browsable API.  
- Start frontend integration testing (React vs Django templates).  
- Prepare reporting dashboard and metrics.

---


##  **Contributors
  Alex Alexander (Project Lead)
  Open collaboration and contributions welcome!

## **How to Run the Project (Development)**

```bash
# Clone the repository
git clone <repo-url>
cd Alx_YardGroProject

# Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start development server
python manage.py runserver

