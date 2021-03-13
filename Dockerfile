FROM python:3.8

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
WORKDIR /app/src

# RUN python3 manage.py migrate
RUN python3 manage.py collectstatic

# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
