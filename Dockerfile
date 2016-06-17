FROM python:latest

RUN mkdir -p /home/dropbox-file-size
ENV HOME /home/dropbox-file-size

WORKDIR /home/dropbox-file-size
ADD . .

RUN pip3 install -r requirements.txt

#CMD ["tail","-f","/dev/null"]
CMD python src/main.py
