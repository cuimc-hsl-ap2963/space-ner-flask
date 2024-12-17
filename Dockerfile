FROM python:3.11

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Add debug statements
RUN echo "Installed packages:" && pip3 freeze
RUN echo "Listing files in the container:" && ls -la /app

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]