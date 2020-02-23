FROM python
ENV PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN mkdir /code
RUN mkdir -p /media/documents

COPY src /code

RUN apt-get install -y git wget curl gcc libglib2.0-0 libsm6 libxext6 libxrender-dev
RUN pip install django numpy opencv-python scipy pillow

EXPOSE 80
ENTRYPOINT ["python3", "/code/manage.py", "runserver", "0.0.0.0:80"]
