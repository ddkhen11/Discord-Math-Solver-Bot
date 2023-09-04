# Discord Math Solver Bot

## Overview

This Discord bot is designed to solve mathematical problems by leveraging the Wolfram Alpha API. The bot converts the returned result to LaTeX format using the OpenAI API, generates an image from the LaTeX code, and sends it back to the Discord channel. 

## Features

- 📚 **Rich Math Solving Capabilities**: Utilizes Wolfram Alpha's powerful computation engine to solve a wide array of mathematical problems.
- 📝 **LaTeX Support**: Transforms the result into LaTeX code for better readability.
- 🖼️ **Image Rendering**: Converts LaTeX code into an easily sharable image.
- 🎮 **Discord Integration**: Easily accessible through Discord commands.

## Structure

Here's a brief overview of the main components:

- `main.py`: The main entry point for the bot. Initializes the Discord bot and handles user interactions.
- `get_result.py`: Utilizes the Wolfram Alpha API to get the solution for the problem.
- `result_to_latex.py`: Processes the result from Wolfram Alpha and converts it into LaTeX format through the OpenAI API.
- `latex_to_image.py`: Takes the LaTeX code and renders it into an image.
- `add_white_background.py`: Adds a white background to the image for better readability.
- `keep_alive.py`: Ensures that the bot stays running.

## Dependencies

- Python 3.x
- discord.py
- Wolfram Alpha API
- OpenAI API

## Setup

1. **Clone the repository**
    ```bash
    git clone https://your-repository-link-here.git
    ```

2. **Navigate to the project directory**
    ```bash
    cd your-project-directory
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**
    Create a `.env` file in the project root and add your Wolfram Alpha and OpenAI API keys:
    ```env
    WOLFRAM_API_KEY=your_wolfram_alpha_api_key_here
    OPENAI_API_KEY=your_openai_api_key_here
    ```

5. **Run the bot**
    ```bash
    python main.py
    ```

## Usage

To interact with the bot, use the `!solve` command followed by your query in the Discord chat:

```
!solve antiderivative of 1/(x^3+1)
```

The bot will process your request and reply with an image containing the solution.

## Future Improvements

- Support for more types of queries.
- Error handling for unsupported or incorrect queries.
