# Short Videos Generator

Turn lengthy videos into engaging short clips with ease! The Short Videos Generator is a powerful tool designed to extract the most captivating moments from long videos and create captivating, vertical-format short videos. Whether you need inspirational, funny, or informative content, this project harnesses the potential of Whisper ASR and ChatGPT-4 to streamline the process. 

## Table of Contents
- [How it Works](#how-it-works)
- [Examples](#examples)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

---

## How it Works

1. **Input Video**: Start by providing a link to a long video that you want to condense into shorter, engaging clips.

2. **Transcription with Whisper**: We use [Whisper ASR](https://whisper.openai.com/) to transcribe the audio from your video. Whisper is an advanced automatic speech recognition system, making the transcription highly accurate.

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

- **Inspirational/Motivational**: [Example ](#inspirationalmotivational-example)
- **Funny**: [Example ](#)
- **Informative/Documentary**: [Example ](#Informative/Documentary-example)

## Inspirational/Motivational example:


https://github.com/Hamza-Bouzoubaa/ShortVideoGenerator/assets/104928656/8c9379ff-2092-4650-b542-c829de327ba5

## Informative/Documentary example:

https://github.com/Hamza-Bouzoubaa/ShortVideoGenerator/assets/104928656/7889219a-9354-4f59-a5ee-21ed6d4c6ba9


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
   cd short-videos-generator
   ```

3. Set up your API keys for Whisper ASR and ChatGPT-4 by creating a configuration file.

4. Install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

Need help using it?:
Pls contact me on LinkedIn : https://www.linkedin.com/in/hamza-bouzoubaa-47b918224/

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the terms of the license.

We hope this project helps you create engaging short videos from long content. Feel free to contribute, report issues, or share your feedback to make it even better!
