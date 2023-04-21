FROM python:3.10


WORKDIR /workspace

COPY src/ src/.
COPY script/ script/.
COPY poetry.lock .
COPY pyproject.toml .
COPY run.sh .
COPY Makefile .

RUN pip install poetry && poetry install

CMD [ "sh", "run.sh" ]
