ARG PY_VER
ARG WORKER_BASE_HASH
FROM datajoint/djbase:py${PY_VER}-debian-${WORKER_BASE_HASH}

USER root
RUN apt update && \
    apt-get install -y ssh git vim nano

# RUN pip install pyzmq==23.2.1

USER anaconda:anaconda

WORKDIR $HOME

RUN git clone --branch ccn2023 https://github.com/tdincer/workflow-calcium-imaging.git

RUN cp ./workflow-calcium-imaging/apt_requirements.txt /tmp/
RUN /entrypoint.sh echo "Installed dependencies."

RUN pip install Pygments==2.14.0

RUN pip install ./workflow-calcium-imaging --use-feature=in-tree-build

RUN git clone https://github.com/tdincer/CaImAn.git 
RUN pip install -r ./CaImAn/requirements.txt 
RUN pip install ./CaImAn --use-feature=in-tree-build

WORKDIR /main/workflow-calcium-imaging