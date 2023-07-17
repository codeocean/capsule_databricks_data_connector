# hash:sha256:a58fd362e3a6a59eee9a42e250f2eb6623a132a802d7a4e895bc1e1d0c26ea48
FROM registry.apps.codeocean.com/codeocean/mambaforge3:22.11.1-4-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN pip install -U --no-cache-dir \
    databricks-sql-connector==2.7.0
