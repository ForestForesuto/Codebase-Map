FROM python:3.11

WORKDIR /root

RUN pip install uv

COPY pyproject.toml /root/

COPY . .

RUN uv pip install --system .

CMD [ "python", "-m", "codebase_map.main" ]