## Build the Docker Image
docker build -t image-to-pdf-convertor .

## Run the Docker Container
docker run --rm -v $(pwd)/images:/app/images -v $(pwd)/output:/app/output -e PDF_NAME=my_pdf image-to-pdf-convertor images
