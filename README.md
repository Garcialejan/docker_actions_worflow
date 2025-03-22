# FastAPI Dockerized App with GitHub Actions
This repository demonstrates the practical application of GitHub Actions by automating the deployment process for a FastAPI application. The project includes a Docker image that is automatically updated whenever changes are made to the FastAPI app.

## Project Overview
The goal of this project is to showcase how to integrate GitHub Actions into a development workflow to automate tasks such as building, testing, and deploying a FastAPI application. Additionally, the project utilizes Docker to containerize the application, ensuring consistency across different environments.

Key components of the project:
- A FastAPI application serving as the backend.
- A Dockerfile defining the container environment for the application.
- A GitHub Actions workflow that automates the creation and updating of the Docker image whenever changes are pushed to the main branch.

## Features
- **Automated CI/CD Pipeline** : Every time code is pushed to the repository, the GitHub Actions workflow triggers, ensuring the application is tested and the Docker image is rebuilt.
- **FastAPI Backend** : A lightweight and efficient framework for building APIs.
- **Dockerization** : The application is packaged into a Docker container, making it easy to deploy in any environment.
- **Version Control Integration** : Changes to the application automatically trigger updates to the Docker image.

## How It Works
1) Code Commit & Push : Whenever you commit and push changes to the repository, GitHub Actions listens for these events.
2) Trigger Workflow : The defined GitHub Actions workflow is triggered.
3) Run Tests : The workflow runs tests on the updated codebase to ensure everything works as expected.
4) Build Docker Image : If tests pass, the workflow builds a new Docker image based on the updated code.
5) Update Image : The newly built Docker image is pushed to a container registry (e.g., Docker Hub or GitHub Container Registry).

## Prerequisites
Before getting started, ensure you have the following tools installed on your local machine:
- Git : For version control.
- Python : Required for running the FastAPI application locally.
- Docker : To build and test the Docker image locally.
- GitHub Account : To host the repository and use GitHub Actions.