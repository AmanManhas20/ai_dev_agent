
# ProgEM AI Dev Agent

ProgEM AI Dev Agent is an autonomous AI-powered software development assistant designed to automate the software development workflow. It accepts a programming task, analyzes the requirements, generates code, reviews the implementation, tests the solution, and provides the final output with minimal human intervention.

The project is built using a modular architecture consisting of five independent AI agents, each responsible for a specific phase of the software development lifecycle.

---

## Features

- AI-powered software development workflow
- Automatic task planning and decomposition
- Code generation using Large Language Models
- AI-based code review and optimization
- Automated testing and validation
- Modular architecture for easy scalability
- Logging and execution tracking
- Easy integration with OpenAI and other LLM providers

---

## System Architecture

```
                User Input
                     │
                     ▼
             Planner Agent
                     │
                     ▼
              Coder Agent
                     │
                     ▼
            Reviewer Agent
                     │
                     ▼
              Tester Agent
                     │
                     ▼
             Executor Module
                     │
                     ▼
               Final Solution
```

---

## Project Structure

```
ProgEM-AI-Dev-Agent/
│
├── agents/
│   ├── planner_agent.py
│   ├── coder_agent.py
│   ├── reviewer_agent.py
│   ├── tester_agent.py
│
├── core/
│   ├── llm_client.py
│   ├── executor.py
│   ├── file_manager.py
│   ├── logger.py
│
├── generated_code/
│   └── solution.py
│
├── tests/
│   └── test_cases.py
│
├── prompts/
│
├── config.py
├── requirements.txt
├── main.py
└── README.md
```

---

# Modules

## 1. Planner Agent

The Planner Agent receives the user's programming request and converts it into a structured implementation plan.

Responsibilities:

- Understand the problem statement
- Break the problem into smaller tasks
- Define implementation steps
- Generate development strategy

---

## 2. Coder Agent

The Coder Agent generates Python code based on the implementation plan provided by the Planner Agent.

Responsibilities:

- Generate clean code
- Follow Python coding standards
- Create reusable functions
- Handle edge cases

---

## 3. Reviewer Agent

The Reviewer Agent analyzes the generated code for quality and correctness.

Responsibilities:

- Detect logical errors
- Improve code readability
- Suggest optimizations
- Verify best coding practices

---

## 4. Tester Agent

The Tester Agent validates the generated solution using predefined and dynamically generated test cases.

Responsibilities:

- Execute test cases
- Detect runtime errors
- Validate expected outputs
- Report failed tests

---

## 5. Executor Module

The Executor coordinates communication between all AI agents and manages the complete workflow.

Responsibilities:

- Run agents sequentially
- Handle exceptions
- Store generated files
- Save execution logs

---

# Workflow

```
User Prompt
      │
      ▼
Planner Agent
      │
      ▼
Coder Agent
      │
      ▼
Reviewer Agent
      │
      ▼
Tester Agent
      │
      ▼
Final Output
```

---

# Technologies Used

- Python 3.10+
- OpenAI GPT Models
- ChatGPT API
- REST APIs
- JSON
- PyTest
- Logging Module

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ProgEM-AI-Dev-Agent.git
```

Move into the project

```bash
cd ProgEM-AI-Dev-Agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

Add your API key

```
OPENAI_API_KEY=your_api_key
```

Run the application

```bash
python main.py
```

---

# Example

### Input

```
Write a Python function to find the factorial of a number.
```

### Process

```
Planner → Creates plan

↓

Coder → Generates function

↓

Reviewer → Optimizes code

↓

Tester → Executes test cases

↓

Returns final solution
```

---

# Advantages

- Reduces manual coding effort
- Improves development speed
- Generates structured code
- Performs automatic code review
- Ensures code correctness through testing
- Easily extendable with additional AI agents

---

# Future Improvements

- Multi-language support (Java, C++, JavaScript)
- Docker deployment
- Web-based dashboard
- Memory-enabled AI agents
- GitHub integration
- CI/CD pipeline support
- Multi-agent collaboration
- Code documentation generation

---

# Author

**Aman**

Computer Science Engineering Student

Interested in:

- Artificial Intelligence
- Agentic AI
- Backend Development
- Python
- Java
- Software Engineering

---

# Acknowledgements

This project was developed by leveraging Large Language Models through the ChatGPT API to assist with planning, code generation, review, and testing. ChatGPT served as an AI development assistant, while the overall project architecture, module integration, workflow design, and implementation were developed as part of this project.

---

# License

This project is licensed under the MIT License.
