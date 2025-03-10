# Chat with SQL Database

A Streamlit-based application that allows users to interact with various SQL databases using natural language queries powered by LangChain and Groq LLM.

## Features

- Support for multiple database types:
  - SQLite3
  - MySQL
  - SQL Server
- Natural language querying of databases
- Interactive chat interface
- Real-time streaming responses
- Secure database connection handling
- Windows Authentication support for SQL Server

## Prerequisites

- Python 3.x
- Groq API Key
- Required database drivers:
  - ODBC Driver 17 for SQL Server (if using SQL Server)
  - MySQL Connector (if using MySQL)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/aliarmaghan/Generative-AI.git
cd Generative-AI/Chat_with_sqldb
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Select your database type from the sidebar:
   - SQLite3 Database (local)
   - MySQL Database
   - SQL Server

3. For MySQL or SQL Server, provide the connection details:
   - Host/Server name
   - Username (if required)
   - Password (if required)
   - Database name

4. Click the "Connect to Database" button

5. Once connected, you can start asking questions about your database in natural language

## Example Queries

- "Show me all tables in the database"
- "What is the total number of records in the students table?"
- "Find the average age of students"

## Environment Variables

- `GROQ_API_KEY`: Your Groq API key for LLM access
- `HF_TOKEN`: Hugging Face token (if required)

## Security Notes

- Database credentials are handled securely and not stored
- Windows Authentication is supported for SQL Server
- Passwords are masked in the interface
- SQLite database is opened in read-only mode

## Dependencies

Key dependencies include:
- streamlit
- langchain
- langchain_groq
- sqlalchemy
- pyodbc
- python-dotenv
- mysql-connector (for MySQL connections)

## Contributing

Feel free to submit issues and enhancement requests!

## License

[MIT License](LICENSE)