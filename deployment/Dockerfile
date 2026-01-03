# Base image
FROM python:3.12-slim

WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r deployment/requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Start the Streamlit app
CMD ["streamlit", "run", "ui/dashboard_ui.py", "--server.port=8501", "--server.address=0.0.0.0"]
