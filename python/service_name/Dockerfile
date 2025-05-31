FROM public.ecr.aws/lambda/python:3.11

RUN pip install poetry

WORKDIR ${LAMBDA_TASK_ROOT}

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install

COPY src ./src

CMD ["src.index.handler"]
