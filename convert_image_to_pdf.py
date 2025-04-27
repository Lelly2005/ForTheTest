import sys
import img2pdf
import os

# אם לא נמסר נתיב
if len(sys.argv) < 2:
    print("Please provide a file or directory path.")
    sys.exit(1)

pdfname = os.getenv("PDF_NAME", default="output")
filepath = sys.argv[1]

# ודא שהתיקיה output קיימת, אם לא צור אותה
if not os.path.exists("output"):
    os.makedirs("output")

# אם הנתיב הוא תיקיה
if os.path.isdir(filepath):
    imgs = []
    for fname in os.listdir(filepath):
        if not fname.lower().endswith(".jpg"):
            continue
        path = os.path.join(filepath, fname)
        if os.path.isdir(path):
            continue
        imgs.append(path)

    # אם לא נמצאו תמונות
    if not imgs:
        print(f"No valid JPG images found in {filepath}.")
        sys.exit(1)

    # הדפסת התמונות שנמצאו
    print(f"Images being processed: {imgs}")
    
    with open(f"output/{pdfname}.pdf", "wb") as f:
        f.write(img2pdf.convert(imgs))

# אם הנתיב הוא קובץ
elif os.path.isfile(filepath):
    if filepath.lower().endswith(".jpg"):
        with open(f"output/{pdfname}.pdf", "wb") as f:
            f.write(img2pdf.convert(filepath))
    else:
        print("The provided file is not a JPG image.")
else:
    print("Please input a valid file or directory.")
