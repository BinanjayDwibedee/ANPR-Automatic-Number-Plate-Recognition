# 🚘 ANPR (Automatic Number Plate Recognition) System using Django

This project is a complete Automatic Number Plate Recognition (ANPR) system built using **Python**, **Django**, **OpenCV**, and **EasyOCR**. It captures frames from uploaded videos, extracts vehicle number plates using OCR, and stores both the image and text in a database. An Excel report is generated with the extracted data and saved in the `media/` folder.

---
## 🙋‍♂️ Author

**Binanjay Dwibedee**   
[GitHub](https://github.com/BinanjayDwibedee/ANPR-Automatic-Number-Plate-Recognition-) | [LinkedIn](https://www.linkedin.com/in/binanjaydwibedee/)


## 🛠 Features

- 🎥 Upload video for processing
- 📸 Extract frames (every 30th frame) using OpenCV
- 🔍 Detect and read number plates using EasyOCR
- 🗃 Save captured images and extracted text in a database
- 📄 Generate Excel report with images and number plate text
- 🌐 Simple web interface with Django

---

## 🚀 Technologies Used

- Python 3.12
- Django 5.x
- OpenCV
- EasyOCR
- Pillow
- openpyxl

---

## 📁 Project Structure

anpr_project/
├── anpr_project/        # Django settings and root URLs
├── detector/            # Main app
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── templates/
├── media/               # Saved frames and Excel report
├── manage.py
├── requirements.txt
└── README.md


## ⚙️ Setup Instructions

```bash
# Clone repo
git clone https://github.com/yourusername/anpr_project.git
cd anpr_project

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Start server
python manage.py runserver 0.0.0.0:8000

## 📸 Demo

![Demo Screenshot](media/sample_frame.png)

![image](https://github.com/user-attachments/assets/d589f5c3-369a-4bd0-8787-62520b5e3dfd)

