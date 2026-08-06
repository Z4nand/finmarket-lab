FROM pytorch/pytorch:2.11.0-cuda12.8-cudnn9-devel

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install --yes --no-install-recommends wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install \
        --no-cache-dir \
        --break-system-packages \
        setuptools wheel \
    && python -m pip install \
        --no-cache-dir \
        --break-system-packages \
        --no-build-isolation \
        -r /tmp/requirements.txt

EXPOSE 8888
CMD ["bash"]
