# Profile App Kubernetes Project

Hi 👋  
I am **Divya**, an enthusiastic DevOps engineer.  
This is my first Kubernetes project, built to strengthen my understanding of containerization and Kubernetes fundamentals.

## 🚀 Project Overview

This project demonstrates how to:
- Containerize a Flask application using Docker
- Deploy the application on Kubernetes
- Run MySQL inside the Kubernetes cluster
- Connect Flask to MySQL using Kubernetes Services
- Secure credentials using Kubernetes Secrets

## 🛠 Technologies Used

- Docker
- Docker Hub  
  Image: https://hub.docker.com/r/dhivlaksh03/first-flask-app
- Kubernetes (Minikube)
- Flask (Python)
- MySQL

## ☸️ Kubernetes Components Used

- **Deployment** – to manage application pods and enable rolling updates
- **Service**
  - NodePort – to access Flask application externally
  - ClusterIP – for internal MySQL communication
- **Secrets** – to store database credentials securely
- **ConfigMaps** – for database configuration

## 🧠 What I Learned from This Project

- Building and pushing Docker images to Docker Hub
- Writing optimized Dockerfiles
- Deploying applications using Kubernetes Deployments
- Understanding Services, selectors, and labels
- Difference between NodePort and ClusterIP
- Using Secrets instead of hardcoding passwords
- Understanding and using kubectl commands for managing and debugging Kubernetes resources

## ▶️ How to Run

```bash
minikube start --driver=docker
kubectl apply -f k8s/
minikube service flask-service
