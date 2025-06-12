# PRSK Story Summarizer
This Python application scrapes, stores, and summarizes event stories from Project Sekai: Colorful Stage using a Hugging Face Transformers LLM.

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
- Use [IBM-Granite/Granite-3.3-8B-Instruct](https://huggingface.co/ibm-granite/granite-3.3-8b-instruct) for summary generation.
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
- Summaries will be generated locally using a Hugging Face Transformers LLM.
- Internet connection is required to download the LLM.
- No internet connection is required during generation once the LLM is downloaded.
- Ensure you have sufficient RAM (12GB+) to run the model locally.
- The model will be downloaded to the `llm/` directory.
- All data, including the summaries, are stored in the SQLite database located in `data/prsk_stories.db`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [Sekai Viewer](https://sekai.best/storyreader/eventStory) - for archiving and maintaining access to Project Sekai: Colorful Stage story content.
- [IBM-Granite](https://huggingface.co/ibm-granite/granite-3.3-8b-instruct) - for providing the open-source Granite-3.3-8B-Instruct language model via Hugging Face.
