FROM python:3.9-slim

WORKDIR /app

# Copy the backend files
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose port 5050 for Flask
EXPOSE 5050

CMD ["python", "app.py"]