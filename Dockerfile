FROM python:3.8.10

RUN mkdir /app

COPY requirements.txt /app/

RUN python -m pip install --upgrade pip
RUN python -m pip install -r /app/requirements.txt

COPY . ./app/

WORKDIR /app/api_gallery/

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
