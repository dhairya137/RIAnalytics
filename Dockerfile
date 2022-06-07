FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install fitz
RUN pip install pymupdf
RUN pip install nltk
RUN pip install pdftotext
RUN python -m nltk.downloader punkt  
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --no-input

CMD python manage.py runserver 0.0.0.0:8000