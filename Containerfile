# Use lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy script
COPY monitor.py /app

# Install Python dependency
RUN pip install requests

# Environment variables (can override with .env)
ENV MONITOR_URL=https://example.com
ENV CHECK_INTERVAL=60
ENV EMAIL_USER=youremail@gmail.com
ENV EMAIL_PASS=yourpassword
ENV EMAIL_TO=alertemail@gmail.com

# Run the monitor script
CMD ["python", "monitor.py"]
