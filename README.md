# OllamaRAGApp

## How to Use This Repository

## Step 1: Download and Install Ollama

First, download and install Ollama from the following GitHub repository:

[Ollama GitHub Repository](https://github.com/mayankchugh-learning/OllamaRAGApp.git)

## Step 2: install ollama and Pull the Models

Follow these steps to pull the necessary models:

1. Pull the Mistral model: `ollama run mistral`
2. Pull the Nomic-Embed-Text model: `ollama pull nomic-embed-text`

## Step 3: Create and activate Conda envirnoment

```bash
conda create -p ollamaRagenv python=3.8 -y
```

## Step 4: Install Dependencies

```bash
source activate ./ollamaRagenv
```
## Step 5: Clone the Project and Run

```bash
pip install -r requirements.txt 
```

## Step 5: Run the application using Streamlit:

```bash
streamlit run app.py
```

## How to Use

### Question

- Text area 1: Copy and paste the URLs you want searched based on.
- Write your query in question section.
- Click on Query Documents.

## Using a Different Model

If you want to use a different model, pull it using: `ollama run <model>`
Then, modify the code line:
`python model_local = Ollama(model="mistral")`
to
`python model_local = Ollama(model="new-model")`

## Based on This Tutorial

This guide is based on the tutorial provided by Sri Laxmi Beapc on LinkedIn:

[How to Build a RAG Chatbot Using Ollama to Serve LLMs Locally](https://www.linkedin.com/pulse/how-build-rag-chatbot-using-ollama-serve-llms-locally-sri-laxmi-beapc?utm_source=share&utm_medium=member_ios&utm_campaign=share_via)
