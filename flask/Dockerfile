FROM python:3.9
WORKDIR /app
COPY file.py /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python","file.py"]
EXPOSE 80
