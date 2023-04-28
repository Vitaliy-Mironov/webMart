FROM python:3.11.1
WORKDIR /
COPY ./requirements.txt .
RUN pip install --update pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "webmart/manage.py", "runserver"]
