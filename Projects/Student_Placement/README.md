# Placement Prediction System

A Flask web application that predicts student placement probability using academic and skill profile.

## Features
- Predicts placement probability based on student metrics
- Uses Random Forest machine learning model
- Simple, intuitive web interface

## Local Setup

1. Clone the repository
2. Create virtual environment:
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   python app.py
   ```
   
   Visit `http://localhost:5000`

## Deployment on Render

1. Push code to GitHub
2. Go to [render.com](https://render.com) and create account
3. Click "New" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Click "Create Web Service" and deploy!

## Input Features
- SSC Marks
- HSC Marks
- CGPA
- Aptitude Score
- Workshops/Certifications
- Projects Count
- Internships Count
- Soft Skills Rating
- Extracurricular Activities (Yes/No)
- Placement Training (Yes/No)

## Model Performance
- Accuracy: ~76.8%
- Model Type: Random Forest Classifier
