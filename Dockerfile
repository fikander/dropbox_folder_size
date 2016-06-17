FROM python:latest

RUN mkdir -p /home/dropbox-folder-size
ENV HOME /home/dropbox-folder-size

WORKDIR /home/dropbox-folder-size
ADD . .

RUN pip3 install -r requirements.txt

#CMD ["tail","-f","/dev/null"]
CMD python src/main.py
