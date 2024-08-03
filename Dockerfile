ARG VARIANT="ubuntu-24.04"
ARG BASE="mcr.microsoft.com/vscode/devcontainers/base"
FROM --platform=linux/amd64 ${BASE}:${VARIANT}

# Install Homebrew
RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

RUN DEBIAN_FRONTEND=noninteractive sudo apt=get update && sudo apt-get install -y --no-install-recommends \
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


