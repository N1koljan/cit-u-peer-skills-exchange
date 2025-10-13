# CIT-U Peer-to-Peer Skills Exchange Platform

## 📝 Short Description
The **CIT-U Peer-to-Peer Skills Exchange Platform** is a web-based system that enables students to exchange and share skills securely within the CIT University community. It allows users to create profiles, list the skills they can offer, request skills from others, and communicate effectively through an integrated system. It encourages collaboration, peer learning, and skill development among students.

---

## 🎯 Objectives
The project aims to develop a functional platform that enables students to exchange skills through secure access, user profiles, and interactive features while ensuring active participation through onboarding and meaningful exchanges during testing. By utilizing available tools, resources, and volunteer participants, the system will remain feasible and realistic within scope. The goal is to deliver a reliable, user-friendly solution that fosters collaboration, knowledge sharing, and personal growth among students — with development and validation completed within the project timeline and strong user satisfaction achieved upon rollout.

---

## 📚 Scope
The project scope covers the development of a **responsive web application** accessible via desktop and mobile browsers, featuring:
- Secure student login  
- User profile creation  
- Real-time skill listings and requests  
- Peer-to-peer exchanges (voluntary, barter, or low-cost)  
- Communication tools  
- Search and skill-matching  
- Basic feedback and rating system  

**Out of scope:**
- Third-party payment gateway integration  
- Large-scale deployment beyond CIT-U  
- Advanced AI-driven recommendation systems  

---

## 👥 Stakeholders
| Role | Name | CIT-U Email |
|------|------|--------------|
| Product Owner | Michael Grant Libato | michaelgrant.libato@cit.edu |
| Business Analyst | John Luis Leanda | johnluis.leanda@cit.edu |
| Business Analyst | Melody Ann Garbo | melodyann.garbo@cit.edu |
| Scrum Master | Godwin Labaya | godwin.labaya@cit.edu |
| Developer | Gerard Grant Estela | gerardgrant.estela@cit.edu |
| Developer | Homer Fernandez | homer.fernandez@cit.edu |
| Developer | Nicole John Inoc | nicolejohn.inoc@cit.edu |

---

## 💻 Tech Stack Used
**Frontend:** React.js, Tailwind CSS  
**Backend:** Django REST Framework  
**Database:** PostgreSQL  
**Other Tools:** Docker, GitHub, Visual Studio Code, Postman, PyCharm  

---

## ⚙️ Setup and Run Instructions

### 🧩 Prerequisites
- Python 3.10+  
- Node.js 18+  
- PostgreSQL  
- Git  
- PyCharm IDE *(recommended)*  

---

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/N1koljan/cit-u-peer-skills-exchange.git
cd cit-u-peer-skills-exchange
```
2️⃣ Backend Setup (Django)
```bash
cd backend
python -m venv venv
venv\Scripts\activate      # For Windows
# or
source venv/bin/activate   # For macOS/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Backend runs by default at: http://127.0.0.1:8000/
```
3️⃣ Frontend Setup (React)
```bash
cd frontend
npm install
npm start

Frontend runs by default at: http://localhost:3000/
```
4️⃣ Access the Application
Open your browser and go to:
```bash
👉 http://localhost:3000
```
🌐 Deployed Link
If deployed, the live version of the project can be accessed at:
🔗 https://cit-u-peer-skills-exchange.vercel.app
