FROM python:3.9
RUN mkdir /code
WORKDIR /code

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD main.py .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
