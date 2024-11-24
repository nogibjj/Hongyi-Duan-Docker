# Hongyi-Duan-Docker

[![Python CI/CD with Docker](https://github.com/nogibjj/Hongyi-Duan-Docker/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Hongyi-Duan-Docker/actions/workflows/cicd.yml)

This repository demonstrates the use of Docker for containerizing Python applications. It includes a `Dockerfile` for building a Docker image and instructions for running the containerized application. The project highlights the power of Docker for creating portable, consistent environments for application development and deployment.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Usage](#usage)
  - [Build the Docker Image](#build-the-docker-image)
  - [Run the Docker Container](#run-the-docker-container)
- [Key Files](#key-files)
- [Project Details](#project-details)
- [Future Work](#future-work)
- [License](#license)
- [Contact](#contact)

---

## Overview

The primary goal of this project is to showcase the creation and deployment of Dockerized Python applications. By containerizing the application, developers ensure consistency across environments, simplify dependencies management, and streamline deployment processes.

---

## Features

- **Dockerfile**: Defines a step-by-step process to build the Docker image.
- **Customizable Environment**: Enables users to easily modify and rebuild the container with updated dependencies or code changes.
- **Platform Independence**: Ensures the application runs consistently across all environments where Docker is available.

---

## Getting Started

### Prerequisites

Before getting started, make sure you have the following:

1. Install Docker on your system. You can follow the [Docker Installation Guide](https://docs.docker.com/get-docker/).
2. Clone this repository:
   ```bash
   git clone https://github.com/nogibjj/Hongyi-Duan-Docker.git
   cd Hongyi-Duan-Docker
   ```

### Setup

To set up the environment:

- Review the `Dockerfile` and ensure all dependencies required for your Python application are included.
- Modify the `requirements.txt` file (if applicable) to include additional Python libraries.

---

## Usage

### Build the Docker Image

Build the Docker image from the `Dockerfile`:
```bash
docker build -t hongyi-duan-docker .
```

- The `-t` flag tags the image with a name (`hongyi-duan-docker` in this case).
- The `.` indicates the build context, which is the current directory.

### Run the Docker Container

Run the Docker container using the created image:
```bash
docker run --rm -it hongyi-duan-docker
```

- The `--rm` flag ensures the container is automatically removed after it stops.
- The `-it` flags enable an interactive terminal for the container.

### Docker Configuration
<img width="1274" alt="767697491904e8512de9c8666c5b45c" src="https://github.com/user-attachments/assets/942623c9-6c6b-462f-a291-0b8117f64113">
<img width="1274" alt="439665df5c48b5db15198c6344e4015" src="https://github.com/user-attachments/assets/f839e5aa-920b-4d52-81ef-59c29855209f">

---

## Key Files

### `Dockerfile`

The `Dockerfile` is a script with instructions for creating the Docker image. Key sections include:

1. **Base Image**: Specifies the starting environment (e.g., `python:3.9-slim`).
2. **Dependencies Installation**: Installs required Python libraries and tools.
3. **Copying Files**: Transfers application files into the container.
4. **Command Execution**: Sets the default command to run the application.

### Application Code

The repository includes application scripts and resources necessary for running the containerized application. All relevant files are copied into the container during the image build process.

---

## Project Details

This project demonstrates:

1. Best practices for creating a Dockerfile.
2. Efficient management of dependencies and environments using Docker.
3. A template for containerizing Python applications for deployment.

---

## Future Work

Potential improvements to the project:

- **Extend the Dockerfile**: Add more dependencies or tools as required.
- **Multi-Stage Builds**: Optimize for production-ready Docker images.
- **Integrate Docker Compose**: Simplify multi-container application deployments.
- **CI/CD Integration**: Automate Docker builds and deployments using pipelines.
