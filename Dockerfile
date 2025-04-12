FROM alpine:edge

RUN apk add --update py3-pip
RUN python3 -m venv /venv

ENV PATH="/venv/bin:$PATH"

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

COPY app.py /usr/src/app/
COPY templates/books.html /usr/src/app/templates/
COPY templates/login.html /usr/src/app/templates/
COPY templates/wrong_login.html /usr/src/app/templates/


EXPOSE 5000

CMD ["python3", "/usr/src/app/app.py"]