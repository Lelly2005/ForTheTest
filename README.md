## Build the Docker Image
docker build -t image-to-pdf-convertor .

## Run the Docker Container
docker run --rm -v /mnt/c/Users/ללי\ מאירספלד/Downloads/image_to_pdf\ \(1\)/images:/app/images -v /mnt/c/Users/ללי\ מאירספלד/Downloads/image_to_pdf\ \(1\)/output:/app/output -e PDF_NAME=my_pdf pexels-pixabay-33101 python /app/convert_image_to_pdf.py images
