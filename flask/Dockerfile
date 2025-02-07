FROM python:3.9
WORKDIR /file
ADD file.py /file
ADD requirements.txt /file
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python","file.py"]
