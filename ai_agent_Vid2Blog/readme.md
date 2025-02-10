# Automating Blog Creation with AI Agents Using Q AI

## Project Description
This project demonstrates the use of **Q AI**, an advanced AI agent framework, to automate the generation of structured blog pages from YouTube video content. By leveraging agent-based collaboration, this system automates repetitive tasks, streamlining the creation of high-quality blogs with minimal manual effort.

### Key Features
- **Agents as Experts**: Simulate domain-specific expertise, such as researchers and content writers.
- **Tool Integration**: Use third-party utilities like YouTubeSearchTool and OpenAI APIs for task execution.
- **Flexible Workflows**: Supports both sequential and hierarchical process flows.
- **Scalable Automation**: Efficiently handles large-scale blog creation projects with accuracy and speed.

---

## Table of Contents
1. [Installation](#installation)
2. [Usage Guide](#usage-guide)
3. [Project Workflow](#project-workflow)
4. [Credits](#credits)
5. [License](#license)

---

## Installation

### Prerequisites
- Python 3.10
- Conda or virtual environment setup
- API keys for OpenAI and YouTube tools

### Setup Instructions
1. Clone this repository:
   ```bash
        git clone https://github.com/your-repo-link.git
        cd your-repo-folder

2. Create and activate a new Conda environment:
    ```bash
        conda create -n qai_env python=3.10
        conda activate qai_env


3. Install dependencies:
    ```bash
        pip install -r requirements.txt


4. Configure your environment:
    - Add your API keys in a .env file: 
    ```bash
        OPENAI_API_KEY=your_openai_key


---
## Usage Guide

1. **Define Agents**:
- The **Researcher Agent** retrieves and summarizes YouTube video content based on a given topic.
- The **Content Writer Agent** converts the summary into an engaging blog post.

2. **Run the System**: Execute the automation with:
    ```bash
    python crew.py

3. **Output**: The generated blog is saved in new_blog_post.md.

4. **Example**: For a topic like "AI vs ML vs Data Science", the system:
  
- Fetches relevant YouTube videos.
- Extracts transcripts and generates summaries.
- Produces a well-structured markdown blog post.

---
## Project Workflow
1. **Researcher Agent**:

- Fetches YouTube videos using the YouTubeSearchTool.
- Extracts, transcribes, and summarizes video content.
- Passes processed data to the **Content Writer Agent**.

2. **Content Writer Agent**:

- Converts the summarized content into a markdown blog.

3. **Sequential Execution**:

- Tasks are executed linearly, ensuring data is processed in logical steps.

---
## Credits
This project was inspired by modern agent frameworks like **CrewAI** and utilizes tools from ****OpenAI** and **YouTubeSearchTool**.