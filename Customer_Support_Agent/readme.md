# Intelligent Customer Support Agent

## Project Description
This project demonstrates how to build an intelligent customer support agent using LangGraph, a framework for orchestrating complex workflows with language models. The agent is capable of categorizing customer queries, analyzing sentiment, generating appropriate responses, and escalating issues when necessary. This solution showcases how AI can streamline customer service processes, ensuring efficiency and customer satisfaction.

### Key Features:
- **Query Categorization**: Classifies customer inquiries into categories (Technical, Billing, General).
- **Sentiment Analysis**: Identifies the emotional tone of customer queries (Positive, Neutral, Negative).
- **Dynamic Responses**: Generates relevant responses tailored to the query category and sentiment.
- **Issue Escalation**: Routes critical or negatively toned queries to human agents for further resolution.
- **Graph-based Workflow**: Employs LangGraph to create a modular, extensible workflow for the support process.

### Why LangGraph?
LangGraph simplifies the development of complex, AI-driven workflows by structuring tasks as interconnected nodes. It ensures flexibility, scalability, and maintainability while leveraging powerful language models.

---

## Table of Contents
1. [Installation and Setup](#installation-and-setup)
2. [Usage Instructions](#usage-instructions)
3. [System Workflow](#system-workflow)
4. [Future Enhancements](#future-enhancements)
5. [Credits](#credits)
6. [License](#license)

---

## Installation and Setup
Follow these steps to install and run the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/langgraph-support-agent.git
   cd langgraph-support-agent
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up API Key**:
   - Create a `.env` file in the project root.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

5. **Run the Application**:
   Execute the Python script to process sample queries or test your own:
   ```bash
   python main.py
   ```

---

## Usage Instructions
### Processing a Query
Use the `run_customer_support` function to process customer queries:

```python
query = "My internet connection keeps dropping. Can you help?"
result = run_customer_support(query)
print(result)
```

### Expected Output
The output will include the query category, sentiment, and a generated response:
```json
{
  "category": "Technical",
  "sentiment": "Negative",
  "response": "This query has been escalated to a human agent due to its negative sentiment."
}
```

---

## System Workflow
The workflow leverages LangGraph to manage the following steps:

1. **Categorization**: Classifies the query into predefined categories.
2. **Sentiment Analysis**: Assesses the sentiment of the query.
3. **Dynamic Routing**: Directs queries based on their category and sentiment.
4. **Response Generation**: Produces context-specific replies.
5. **Escalation**: Escalates unresolved or negative sentiment queries.

![Workflow Diagram](workflow-diagram.png) *(Auto-generated with LangGraph)*

---

## Future Enhancements
- **Integration with Live Databases**: Connect with customer databases for personalized support.
- **Multi-Language Support**: Extend NLP capabilities to handle multilingual queries.
- **Advanced Analytics**: Add features for tracking query trends and sentiment metrics.
- **Voice-to-Text Integration**: Allow for spoken customer interactions to be processed.

---

## Credits
This project was developed by [Md Ali Armaghan](https://github.com/md-ali-armaghan).

### Special Thanks:
- [LangGraph](https://github.com/langgraph) for the workflow management framework.
- [OpenAI](https://openai.com) for their robust language models.
- **Tutorial References**:
  - LangChain documentation
  - OpenAI API examples

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Badges
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![OpenAI](https://img.shields.io/badge/API-OpenAI-blue)
![LangGraph](https://img.shields.io/badge/langgraph-1.0.0-green)

---

## Contribution Guidelines
We welcome contributions from the community! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with detailed information about your changes.

---

## Tests
Run the following command to execute tests:
```bash
pytest tests/
```

