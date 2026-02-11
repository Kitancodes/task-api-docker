# FastAPI Task Service

I built this project to explore and practice modern DevOps workflows, including CI pipelines and Docker containerization. I wanted to create something real that demonstrates how I can take a codebase from development to a reproducible and deployable artifact.

## Project Overview

I created a not-so-fancy FastAPI application that allows users to manage tasks. The main goals for this project were:

    - To set up a fully functional CI pipeline that runs tests automatically.
    - To build Docker images from the application using best practices, including commit-based tagging.
    - To prepare the project for deployment with containers, so it can run consistently anywhere.

Through this process, I learned how to structure pipelines, manage Docker images, and ensure traceability with versioned builds.

## Features

    - FastAPI REST endpoints for task management.
    - Automated CI testing on each commit.
    - Dockerized application for consistent environments.
    - Multi-tag Docker builds for traceable deployments.

## My Workflow

I worked on this project with a focus on CI and Docker:

    1. I wrote unit tests and integrated them into the CI pipeline.
    2. I built Docker images locally to test the containerization process.
    3. I tagged the images with both 'latest' and the commit SHA to maintain traceable builds.
    4. I pushed the images to a container registry, making them ready for deployment.
    5. I am now preparing to implement CD to deploy containers automatically to EC2.

## What I Learned

I used this project to strengthen my understanding of modern DevOps practices:

    - How to structure a CI pipeline that tests and builds reproducible artifacts.
    - How Docker images work and the difference between images and containers.
    - How to version Docker builds for traceability and reliability.
    - How to prepare a project for deployment to cloud infrastructure.

## Next Steps

My next step is to implement Continuous Deployment. I plan to:

    - SSH into EC2 instances to pull Docker images.
    - Run containers in production-ready environments.
    - Explore automated CD pipelines for full end-to-end DevOps workflow.

## How to Run

If you want to run the project locally:

    1. Clone the repository.
    2. Install dependencies from requirements.txt.
    3. Run tests to ensure everything works.
    4. Build and run the Docker container.
    5. Access the app on the mapped port (e.g., localhost:8000).


