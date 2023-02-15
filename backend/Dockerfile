# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /usr/src/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk update \
    && apk add gcc libffi-dev python3-dev musl-dev mariadb-dev

# install dependencies
RUN pip install --upgrade pip
ADD ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
#RUN sed -i 's/\r$//g' /usr/src/backend/entrypoint.sh
RUN chmod +x /usr/src/backend/entrypoint.sh

# copy project
#COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/backend/entrypoint.sh"]
#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]