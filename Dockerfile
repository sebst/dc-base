ARG VARIANT="ubuntu-24.04"
ARG BASE="mcr.microsoft.com/vscode/devcontainers/base"
FROM ${BASE}:${VARIANT}

RUN localedef -i en_US -f UTF-8 en_US.UTF-8

RUN DEBIAN_FRONTEND=noninteractive sudo apt-get update && sudo apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    file \
    git \
    sudo \
    unzip \
    wget \
    xz-utils && \
    sudo apt-get clean && \
    sudo rm -rf /var/lib/apt/lists/*

# Install Homebrew
RUN useradd -m -s /bin/bash linuxbrew && \
    echo 'linuxbrew ALL=(ALL) NOPASSWD:ALL' >>/etc/sudoers
USER linuxbrew
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"

USER root
ENV PATH="/home/linuxbrew/.linuxbrew/bin:${PATH}"

