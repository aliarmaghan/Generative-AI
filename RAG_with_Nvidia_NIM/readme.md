# Nvidia Nim Generative AI Deployment


## Project Title

**Nvidia Nim - Generative AI Deployment with LangChain and Streamlit**

## Project Description

This project demonstrates the power of **Nvidia Nim**, a breakthrough in generative AI deployment. Nvidia Nim provides a scalable, highly efficient solution for deploying AI models via inference microservices, which makes it easier than ever to integrate advanced AI models into your applications.

With this project, you'll experience:
- How to set up and utilize Nvidia Nim for generative AI.
- Deployment of various models, such as Llama 370B, and integration with LangChain for advanced workflows.
- Practical use of Nvidia's API for AI model inference, with hands-on coding examples.
- Implementation of a **Retrieval-Augmented Generation (RAG)** application using PDF embeddings and AI model interaction.

This project integrates Nvidia's AI foundation models, alongside open-source models, to provide an advanced approach for deploying generative AI applications. The project also uses **Streamlit** for rapid web app deployment and **LangChain** for chaining AI model actions.

### Features
- **Inference Microservices**: Deploy scalable, high-performance generative AI models.
- **Model Integration**: Integrate various AI models seamlessly with Nvidia's API.
- **End-to-End RAG Application**: Build and deploy a complete Retrieval-Augmented Generation app using **PDFs** and **embeddings**.

### Technologies Used
- **Nvidia Nim**: Inference platform for deploying generative AI models.
- **LangChain**: Framework for chaining AI models and managing complex workflows.
- **Streamlit**: Easy-to-use framework for building interactive web apps.
- **PyPDF2**: For extracting text from PDF files in the RAG app.
- **OpenAI**: Used for AI model interaction.
- **Nvidia API**: To call AI models and perform inference tasks.

### Challenges Faced
- Setting up the environment for deploying generative AI models with Nvidia Nim.
- Integrating different APIs into a seamless user experience.
- Efficiently handling large-scale AI model inference and multi-modal support.

## Table of Contents
1. [How to Install and Run the Project](#how-to-install-and-run-the-project)
2. [How to Use the Project](#how-to-use-the-project)
3. [Credits](#credits)
4. [License](#license)

## How to Install and Run the Project

To get started, follow these steps to install the project and set up the environment:

### Prerequisites
- Python 3.10 or higher
- Conda for environment management
- An Nvidia account to generate an API key

### Step-by-Step Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/aliarmaghan/nvidia-nim-ai-deployment.git
   cd nvidia-nim-ai-deployment

2. **Create and Activate the Environment:**
   ```bash
      conda create -p venv python=3.10
      conda activate venv

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Generate Nvidia API Key:**

- Log in to your Nvidia account.
- Go to the API section, generate a new API key, and add it to your .env file:
   ```bash
   NVIDIA_API_KEY=your-api-key-here

6. **Run the Application**
   ```bash
      python app.py

7. **Open your browser and go to http://localhost:8501 to view the running Streamlit app.**