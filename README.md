# Short Videos Generator

Turn lengthy videos into engaging short clips with ease! The Short Videos Generator is a powerful tool designed to extract the most captivating moments from long videos and create captivating, vertical-format short videos. Whether you need inspirational, funny, or informative content, this project harnesses the potential of Whisper ASR and ChatGPT-4 to streamline the process. 

## Table of Contents
- [How it Works](#how-it-works)
- [Examples](#examples)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#Usage)
- [License](#license)

---

## How it Works

1. **Input Video**: Start by providing a link to a long video that you want to condense into shorter, engaging clips.

2. **Transcription with Whisper**: I use [Open AI](https://whisper.openai.com/) to transcribe the audio from your video. Whisper is an advanced automatic speech recognition system, making the transcription highly accurate.

3. **ChatGPT-4 for Content Selection**: The transcriptions and timestamps are then fed into ChatGPT-4. This model, powered by OpenAI's GPT-3.5 architecture, excels at understanding and generating human-like text.

4. **Clip Selection**: ChatGPT-4 analyzes the transcriptions and timestamps to find the most suitable moments in the video. It identifies content for three types: 
    - Inspirational/Motivational
    - Funny
    - Informative/Documentary

5. **Clip Generation**: Once ChatGPT-4 has determined the moments, the project cuts and edits the video to extract these clips, ensuring they are visually engaging and in a vertical screen format.

6. **Subtitles**: Accurate subtitles are generated for each clip, enhancing the accessibility and impact of the content.

7. **Output**: You get a set of short videos ready for sharing on various platforms, each focused on the chosen theme.

---

## Examples

Here are some examples of short videos generated using the Short Videos Generator:

- **Inspirational/Motivational**: [Example ](#Inspirationalmotivational-example)
- **Funny**: [Example ](#)
- **Informative/Documentary**: [Example ](#InformativeDocumentary-example)

## Inspirational/Motivational example:



https://github.com/Hamza-Bouzoubaa/ShortVideoGenerator/assets/104928656/4f8b8a5f-85fd-4822-9043-095a1ff74265




## Informative/Documentary example:



https://github.com/Hamza-Bouzoubaa/ShortVideoGenerator/assets/104928656/7070e339-ba9e-480e-8a16-0527e2f84fcf





---

## Requirements

Before using the Short Videos Generator, make sure you have the following requirements in place:

- An internet connection to access the necessary APIs and services.
- An open AI API key can be obtained from [Whisper ASR](https://openai.com/).
- Install all requirements.
- Access to ChatGPT-4 API for content selection.
- Video editing software for finalizing the generated short videos.

---

## Installation

To install the Short Videos Generator, follow these steps:

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/Hamza-Bouzoubaa/ShortVideoGenerator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd shortvideogenerator
   ```

3. Set up your API keys for Whisper ASR and ChatGPT-4 by creating a configuration file.

4. Install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---
## Usage
To use the Short Videos Generator, follow these steps:

Open the main.py file.

Modify the variables OpenAIKEY, TikTokSessionID, and VideoURL with your own values.

Run the modified main.py to start the generation process.

```python
from VideoPipeline import pipeline

OpenAIKEY = "YourKey"
TikTokSessionID = "YourID"
VideoURL = "VideoURL"

pipeline(OpenAIKEY, TikTokSessionID, VideoURL)
```

Need help using it?: 
Pls, contact me on LinkedIn: https://www.linkedin.com/in/hamza-bouzoubaa-47b918224/

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the terms of the license.

I hope this project helps you create engaging short videos from long content. Feel free to contribute, report issues, or share your feedback to make it even better!
