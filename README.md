# PRSK Story Summarizer
This Python application scrapes, stores, and summarizes event stories from Project Sekai: Colorful Stage using a GPT4All LLM.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features
- Scrape story and chapter data and texts from an archive website: [Sekai Viewer](https://sekai.best/storyreader/eventStory)
- Refresh stories when new stories are released
- Store story and chapter data, texts, and summaries in SQLite database for minimal wait times.
- Use GPT4All (Meta-Llama-3-8B-Instruct) for summary generation.
- Generate summaries for individual chapters or all chapters in a story.
- Read full story texts.

## Installation
1. Clone the repository
```bash
git clone https://github.com/DeathEel/prsk_story_summarizer.git
cd prsk_story_summarizer
```

2. Create and activate a Python virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage
1. Run the main script
```bash
python main.py
```

2. Follow the CLI prompts to select stories and chapters or to manually reload data.
- Summaries will be generated locally using GPT4All
- All data, including the summaries, are stored in the SQLite database located in `data/prsk_stories.db`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [GPT4All](https://github.com/nomic-ai/gpt4all) for open source LLM support.
