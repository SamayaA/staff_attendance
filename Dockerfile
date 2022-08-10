FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /workers

COPY ./requirements.txt /workers/requirements.txt
RUN pip install -r /workers/requirements.txt

COPY . /workers

# EXPOSE 8000

# CMD ["python", "manage.py", "migrate"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
