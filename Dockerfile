FROM ubuntu

WORKDIR /app

COPY hello /app/
COPY req.txt /app/




SHELL [ "/bin/bash","-c" ]
RUN apt-get-update && apt-get-install -y python3 python3-pip python3-venv

RUN python3 -m venv venv1 && \
source venv1/bin/activate && \
pip install -r req.txt

EXPOSE 8000

CMD source venv1/bin/activate && python3 manage.py runserver 0.0.0.0:8000

