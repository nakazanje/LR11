FROM python:3.10.0  AS builder
LABEL author="sergey"
COPY requirements.txt .

RUN pip install --upgrade pip
RUN mkdir /source
COPY /service /service
RUN pip install --target /source -r requirements.txt


FROM python:3.10.0-slim  AS working
COPY --from=builder /source/ /source/
COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder /service /service

WORKDIR /service

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /source

CMD python manage.py makemigrations  && \
python manage.py migrate  && \
python manage.py collectstatic --noinput && \
python manage.py runserver 0.0.0.0:8000 --insecure