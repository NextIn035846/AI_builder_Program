# Basic Chatbot using LangGraph Framework with Groq Chat Model

## Overview

This repository demonstrates how to build a basic chatbot using the  framework, integrating the Groq Chat Model as the language backend. The project is a simple yet effective starting point for anyone who wants to create conversational AI applications leveraging modern graph-based orchestration and powerful LLMs.

## Features

- 🗨️ Conversational chatbot with context handling
- ⚡ Powered by the Groq Chat Model for fast and accurate responses
- 🕸️ Built using LangGraph: a flexible, graph-based orchestration framework for LLM applications
- 🧩 Modular and easy to extend

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/NextIn035846/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   The main dependencies are:
   - `langgraph`
   - `groq` (or the official Groq chat model Python package)
   - `langchain` (optional, if you use it for chains/tools)

## Usage

1. **Run the chatbot**
   ```bash
   python chatbot.py
   ```

   You will see a prompt where you can start chatting with the bot.

## Example

```
You: Hello!
Bot: Hi! How can I assist you today?
```

## Customization

- **Enhance the conversational logic:** Add more nodes or tools using LangGraph’s features.
- **Change the LLM:** Substitute Groq with another supported model by changing the initialization.

---

Feel free to fork, modify, and build upon this template for your own chatbot projects!
