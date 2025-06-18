# 🐔 Chicken Disease Classification

A deep learning-based web application for classifying chicken fecal images to detect **Coccidiosis**, a common poultry disease. This project leverages transfer learning with VGG16, modular training pipelines, MLOps tools like DVC, and provides a user-friendly Flask interface.

---

## 📋 Project Overview

Early detection of chicken diseases like **Coccidiosis** is crucial for reducing mortality and ensuring poultry health. This project implements an end-to-end pipeline for:

- **Data ingestion**
- **Model training**
- **Model evaluation**
- **Deployment-ready web app**
- **CI/CD and Docker integration**

---

## ⚙️ Features

- 🧠 **Image Classification** using deep learning (CNN/VGG16)
- 🛠️ Modular architecture with clean codebase under `cnnClassifier/`
- 🔁 **DVC integration** for data and pipeline versioning
- 🌐 Flask-based **web app** with UI for training and predictions
- 📦 Dockerized for easy deployment
- 🔄 GitHub Actions for CI/CD

---

## 📂 Project Structure
├── config/ # Configuration YAMLs
├── src/cnnClassifier/ # Core modules (data loader, model builder, trainer, etc.)
├── templates/ # HTML files for web UI
├── app.py # Flask web app
├── main.py # Model training pipeline
├── params.yaml # Hyperparameters & config paths
├── dvc.yaml # DVC pipeline definition
├── requirements.txt # Project dependencies
├── Dockerfile # Docker container spec
├── setup.py # Project packaging
└── .github/workflows/ # CI/CD GitHub Actions



---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/anurag192/chicken-disease-classification.git
cd chicken-disease-classification

### 2. Create environment and install dependencies
conda create -n chicken python=3.8 -y
conda activate chicken
pip install -r requirements.txt

python main.py


