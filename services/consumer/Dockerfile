# Pull from official base image
FROM python:3.8.2

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install app dependencies
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY ../.. /usr/src/app/

# Run the application
CMD python app.py