FROM alpine:edge

RUN apk add --update py3-pip
RUN python3 -m venv /venv

ENV PATH="/venv/bin:$PATH"

COPY requirements.txt /usr/src/auth-service/
RUN pip install --no-cache-dir -r /usr/src/auth-service/requirements.txt

COPY auth.py  /usr/src/auth-service/


EXPOSE 5000

CMD ["python3", "/usr/src/auth-service/auth.py"]