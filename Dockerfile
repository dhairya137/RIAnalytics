# FROM python:3.8-slim-buster
FROM dhairya137/py3.8sm-poppler20:v1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install wget build-essential cmake libfreetype6-dev pkg-config libfontconfig-dev libjpeg-dev libopenjp2-7-dev -y
RUN wget https://poppler.freedesktop.org/poppler-data-0.4.9.tar.gz \
    && tar -xf poppler-data-0.4.9.tar.gz \
    && cd poppler-data-0.4.9 \
    && make install \
    && cd .. \
    && wget https://poppler.freedesktop.org/poppler-20.08.0.tar.xz \
    && tar -xf poppler-20.08.0.tar.xz \
    && cd poppler-20.08.0 \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make \
    && make install \
    && ldconfig
CMD tail -f /dev/null
# RUN apt-get update && apt-get install -y poppler-utils
# RUN apt-get install pkg-config

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