FROM python:3.7.1-alpine3.8

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /backend/

CMD ["python", "/backend/manage.py", "runserver", "0.0.0.0:8000"]