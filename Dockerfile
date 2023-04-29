FROM python:3.11.1
WORKDIR /
COPY ./requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "eshop/manage.py", "runserver"]
