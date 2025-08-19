# Base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the full project into the container
COPY . .

# Expose the port that Django runs on
EXPOSE 8000

# Collect static files (optional for development, mandatory for production)
RUN python manage.py collectstatic --noinput

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
