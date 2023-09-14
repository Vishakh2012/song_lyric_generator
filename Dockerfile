FROM tensorflow/tensorflow

WORKDIR /usr/src/app

COPY . .

ENV FLASK_APP=sg.py

RUN pip install -r requirements.txt




EXPOSE 5000

CMD flask run --host 0.0.0.0 