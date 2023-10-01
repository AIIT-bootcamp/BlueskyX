
ARG FUNCTION_DIR="/usr/src/app"

FROM python:3.11

ARG FUNCTION_DIR

RUN mkdir -p ${FUNCTION_DIR}
WORKDIR ${FUNCTION_DIR}

RUN apt-get install gcc g++ libc-dev

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt > requirements.txt

RUN pip uninstall poetry --yes

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --target ${FUNCTION_DIR} awslambdaric

COPY ./ ${FUNCTION_DIR}

ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]

CMD [ "main.lambda_handler" ]