FROM python:3.8.3-slim-buster

ARG GIT_HASH
ENV GIT_HASH=${GIT_HASH:-dev}
ENV TINI_VERSION="v0.19.0"

ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

RUN pip install -U \
    pip \
    setuptools \
    wheel

WORKDIR /project

RUN useradd -m -r user && \
    chown user /project

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN chown user /tini
USER user

ENTRYPOINT ["/tini", "--"]
