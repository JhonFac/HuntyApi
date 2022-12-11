FROM martechariadna/pandas

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PATH="/scripts:${PATH}"

RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt


RUN cp /usr/share/zoneinfo/America/Bogota /etc/localtime
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add --update --no-cache libxslt openblas libstdc++ dos2unix
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc g++ linux-headers libc-dev libxml2-dev libxslt-dev libffi-dev python3-dev \
    libressl-dev libxml2 libxslt-dev libjpeg-turbo-dev zlib-dev \
    gfortran build-base freetype-dev libpng-dev openblas-dev \
    && pip install --upgrade pip \
    && apk del .tmp-build-deps \
    && pip install -r requirements.txt 

RUN cp /usr/share/zoneinfo/America/Bogota /etc/localtime

RUN mkdir /code
WORKDIR /code
COPY . /code/
