# מציין את בסיס התמונה שלך
FROM python:3.12-slim

# הגדרת תיקיית העבודה בתוך הקונטיינר
WORKDIR /app

# מעתיק את קבצי requirements.txt ויוצר את ההתקנות הדרושות
COPY requirements.txt .
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org -r requirements.txt

# מעתיק את קובץ ההסבר והקוד שלך
COPY convert_image_to_pdf.py .

# מעתיק את תיקיית התמונות
COPY images /app/images

# התקנה של img2pdf
RUN pip install img2pdf

# הגדרת פקודת ברירת מחדל
CMD ["python", "/app/convert_image_to_pdf.py", "images"]
