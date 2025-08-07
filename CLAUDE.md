# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flask web application starter template built with Python 3. The project serves a simple "Hello World" web page and is configured to run in a Nix-based development environment managed by Firebase Studio.

## Development Environment

### Virtual Environment Setup
- The project uses a Python virtual environment located at `.venv/`
- Always activate the virtual environment before running Python commands:
  ```bash
  source .venv/bin/activate
  ```

### Dependencies
- Dependencies are managed via `requirements.txt`
- After adding new packages, update requirements.txt and install:
  ```bash
  pip install -r requirements.txt
  ```

### Running the Application
- Use the development server script:
  ```bash
  ./devserver.sh
  ```
- The server runs on the port specified by the `$PORT` environment variable (defaults to 80)
- Debug mode is enabled for development

## Project Structure

```
├── main.py                 # Flask application entry point
├── requirements.txt        # Python dependencies
├── devserver.sh           # Development server startup script
├── src/
│   └── index.html         # Main web page
├── web-bundles/           # BMad-Method framework resources
│   ├── agents/            # AI agent configurations
│   ├── expansion-packs/   # Additional development packs
│   └── teams/             # Team configurations
└── GEMINI.md              # Gemini AI development guidelines
```

## Key Files

### main.py
- Simple Flask application with a single route ("/")
- Serves the static HTML file from `src/index.html`
- Uses environment variable `PORT` for server configuration

### devserver.sh
- Bash script that activates the virtual environment
- Runs Flask development server with debug mode enabled
- Uses the Flask app factory pattern with `--app main`

### src/index.html
- Basic HTML5 template with "Hello World" content
- Served as the main landing page

## Development Guidelines

### Python/Flask Best Practices
- Follow PEP 8 style guide for Python code
- Use environment variables for configuration (especially secrets)
- Consider using Flask Blueprints for larger applications
- Implement proper input validation and security measures

### Security Considerations
- Never hardcode secrets in the code
- Use environment variables and `.env` files for sensitive data
- Validate all user input
- Consider using Flask-WTF or Marshmallow for form validation

### Performance Recommendations
- For production, use a WSGI server like Gunicorn
- Implement caching for expensive operations
- Load AI models once at startup, not per request
- Consider using task queues for long-running operations

## BMad-Method Framework

The project includes the BMad-Method framework resources in `web-bundles/`:
- **Agents**: Specialized AI agent configurations for different roles
- **Expansion Packs**: Additional development packs for game development and infrastructure
- **Teams**: Pre-configured team setups for different project types

These resources provide structured approaches for development workflows and team collaboration.

## Testing

The project doesn't currently have a test suite. Consider adding:
- Pytest for unit and integration tests
- Test coverage for Flask routes and application logic
- End-to-end testing for web functionality