FROM alpine:edge

RUN apk add --update py3-pip
RUN python3 -m venv /venv

ENV PATH="/venv/bin:$PATH"

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

COPY app.py /usr/src/app/
COPY models.py /usr/src/app/

COPY templates/books.html /usr/src/app/templates/
COPY templates/login.html /usr/src/app/templates/
COPY templates/wrong_login.html /usr/src/app/templates/
COPY templates/newbook.html /usr/src/app/templates/
COPY templates/addsuccess.html /usr/src/app/templates/
COPY templates/newperson.html /usr/src/app/templates/
COPY templates/addPersonSuccess.html /usr/src/app/templates/
COPY templates/borrowbook.html /usr/src/app/templates/
COPY templates/borrowSuccess.html /usr/src/app/templates/


EXPOSE 5000

CMD ["/venv/bin/python", "/usr/src/app/app.py"]
