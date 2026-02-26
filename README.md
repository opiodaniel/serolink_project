# 🩸 SeroLink

[cite_start]**SeroLink** is a real-time donor mapping platform designed to bridge the gap between empty hospital blood banks and willing donors in the community[cite: 3]. 

[cite_start]The primary goal is to reduce preventable deaths from **Postpartum Hemorrhage (PPH)** and other medical emergencies by ensuring that life-saving blood matches are just a few miles away[cite: 3].

## 🚀 The Core Objective
[cite_start]To create a real-time donor map that connects verified medical facilities with local donors to facilitate immediate "rescue" donations when blood banks are depleted[cite: 3].

## 🛠️ How It Works
1. [cite_start]**Onboarding:** Donors register their location and blood group; hospitals register as verified facilities[cite: 5].
2. [cite_start]**The Wait:** Donors remain active "pins" on the map while going about their daily lives[cite: 5].
3. [cite_start]**Emergency:** When a patient needs blood, doctors filter the map by **Blood Group** and **Proximity** (within a 5-mile radius)[cite: 5, 9, 11].
4. [cite_start]**Action:** The hospital contacts nearby matches directly through the app to request an immediate donation[cite: 5, 12].

## 💻 Tech Stack
- **Backend:** Django (Python) with GeoDjango for spatial logic.
- **Database:** PostgreSQL with PostGIS extension for geographic mapping.
- **Frontend:** Django Templates + Leaflet.js for interactive mapping.
- **API:** Django Rest Framework (DRF) for location-based filtering.

## 📈 Future Vision
- [cite_start]**Community Outreach:** Partnering with the Red Cross for registration drives[cite: 14].
- [cite_start]**Official Backing:** Integrating with the Ministry of Health as a mandatory tool for transfusion facilities.
- [cite_start]**National Scaling:** Expanding from pilot regions (e.g., Northern Uganda) to the entire country[cite: 16].