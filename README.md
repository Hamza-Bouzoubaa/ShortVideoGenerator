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

- **Inspirational/Motivational**: [Example 1](#), [Example 2](#), [Example 3](#)
- **Funny**: [Example 1](#), [Example 2](#), [Example 3](#)
- **Informative/Documentary**: [Example 1](#), [Example 2](#), [Example 3](#)

Feel free to share your own examples and use cases with the community.

---

## Requirements

Before using the Short Videos Generator, make sure you have the following requirements in place:

- An internet connection to access the necessary APIs and services.
- A Whisper ASR API key, which you can obtain from [Whisper ASR](https://whisper.openai.com/).
- Access to ChatGPT-4 API for content selection.
- Video editing software for finalizing the generated short videos.

---

## Installation

To install the Short Videos Generator, follow these steps:

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/yourusername/short-videos-generator.git
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

## Usage

1. Run the script by providing the link to the long video:

   ```bash
   python generate_short_videos.py --video-link https://www.example.com/your-long-video
   ```

2. Follow the on-screen prompts to select the type of content you want (Inspirational/Motivational, Funny, Informative/Documentary).

3. Wait for the Short Videos Generator to process the video, cut, edit, and generate the short videos.

4. Find the generated short videos in the output folder and feel free to share them on your favorite platforms.

---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the terms of the license.

We hope this project helps you create engaging short videos from long content. Feel free to contribute, report issues, or share your feedback to make it even better!
