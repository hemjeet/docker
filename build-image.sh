# python model.py

# Build the Docker image
docker build -t iris-classifier:latest .

# 3. Run container
docker run -d -p 8501:8501 iris-classifier
