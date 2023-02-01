FROM python:3.8

RUN pip install numpy pandas tabulate

WORKDIR /app
COPY generate_random_df.py generate_random_df.py

ENTRYPOINT ["python", "generate_random_df.py"]