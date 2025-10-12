CIT-U Peer-to-Peer Skills Exchange Platform

Short Description

The CIT-U Peer-to-Peer Skills Exchange Platform is a web-based system that enables students to exchange and share skills securely within the CIT University community. The platform allows users to create profiles, list the skills they can offer, request skills from others, and communicate effectively through an integrated system. It encourages collaboration, peer learning, and skill development among students.

Objectives

The project aims to develop a functional platform that enables students to exchange skills through secure access, user profiles, and interactive features while ensuring active participation through onboarding and meaningful exchanges during testing. By utilizing available tools, resources, and volunteer participants, the system will remain feasible and realistic within scope. The goal is to deliver a reliable, user-friendly solution that fosters collaboration, knowledge sharing, and personal growth among students, with development and validation completed within the project timeline and strong user satisfaction achieved upon rollout.

Scope

The project scope covers the development of a responsive web application accessible via desktop and mobile browsers, featuring secure student login, user profile creation, real-time skill listings and requests, peer-to-peer exchanges (voluntary, barter, or low-cost), communication tools, search and skill-matching, and a basic feedback and rating system. Out of scope are third-party payment gateway integration, large-scale deployment beyond CIT-U, and advanced AI-driven recommendation systems.

Stakeholders
Product Owner: Michael Grant Libato
Business Analyst: John Luis Leanda & Melody Ann Garbo
Scrum Master: Godwin Labaya
Development Team: Gerard Grant Estela, Homer Fernandez, Nicole John Inoc
End Users: CIT-U Students, Faculty, or Admins

Tech Stack Used

Frontend: React.js, Tailwind CSS
Backend: Django REST Framework
Database: PostgreSQL
Other Tools: Docker, GitHub, Visual Studio Code, Postman, PyCharm

Setup and Run Instructions
Prerequisites

Python 3.10+
Node.js 18+
PostgreSQL
Git
PyCharm IDE (recommended)

1. Clone the Repository
git clone https://github.com/N1koljan/cit-u-peer-skills-exchange.git
cd cit-u-peer-skills-exchange

2. Backend Setup (Django)
cd backend
python -m venv venv
venv\Scripts\activate      # For Windows
# or
source venv/bin/activate   # For macOS/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Backend runs by default at http://127.0.0.1:8000/

3. Frontend Setup (React)
Open a new terminal window:
cd frontend
npm install
npm start


Frontend runs by default at http://localhost:3000/

4. Access the Application
Visit http://localhost:3000
in your browser.

Team Members
Name	Role	CIT-U Email
Michael Grant Libato	Product Owner	michaelgrant.libato@cit.edu
John Luis Leanda	Business Analyst	johnluis.leanda@cit.edu
Melody Ann Garbo	Business Analyst	melodyann.garbo@cit.edu
Godwin Labaya	Scrum Master	godwin.labaya@cit.edu
Gerard Grant Estela	Developer	gerardgrant.estela@cit.edu
Homer Fernandez	Developer	homer.fernandez@cit.edu
Nicole John Inoc	Developer	nicolejohn.inoc@cit.edu
Deployed Link

If deployed, the live version of the project can be accessed at:
https://cit-u-peer-skills-exchange.vercel.app
