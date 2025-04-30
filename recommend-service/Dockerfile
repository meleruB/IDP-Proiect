FROM alpine:edge

RUN apk add --update py3-pip
RUN python3 -m venv /venv

ENV PATH="/venv/bin:$PATH"

COPY requirements.txt /usr/src/recommend-service/
RUN pip install --no-cache-dir -r /usr/src/recommend-service/requirements.txt

COPY recommend.py /usr/src/app/


EXPOSE 5000

CMD ["python3", "/usr/src/recomend-service/recommend.py"]