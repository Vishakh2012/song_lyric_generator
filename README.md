# song_lyric_generator

![Ed Sheeran]([https://i.imgur.com/YOUR_IMAGE_URL.png](https://unsplash.com/photos/-6NNB_qpjhI))

Welcome to the Ed Sheeran Song Lyrics Generator repository! This project is an AI-powered lyrics generator that has been trained on Ed Sheeran's songs dataset. With the use of LSTM (Long Short-Term Memory) neural networks, this application can generate song lyrics in the style of Ed Sheeran.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Docker Image](#docker-image)
- [Contributing](#contributing)
- [License](#license)


## Features

- Generate song lyrics in the style of Ed Sheeran.
- LSTM-based architecture for creative lyric generation.
- Easy-to-use Flask-based backend application.
- Dockerized for seamless deployment as a container.

## Getting Started

To get started with the Ed Sheeran Song Lyrics Generator on your local machine, follow these instructions.

### Prerequisites

- Docker

### Installation

1. **Clone this repository to your local machine:**

```bash
git clone https://github.com/your-username/sheeran_lyrics_generator.git
cd ed-sheeran-lyrics-generator
```
2.**Build the Docker image:**

```bash

docker build -t ed-sheeran-lyrics-generator .
```

**Usage**

Run the Docker container:

```bash

docker run -p 5000:5000 ed-sheeran-lyrics-generator
```

Open your web browser and navigate to http://localhost:5000 to access the Ed Sheeran Song Lyrics Generator.

**Docker Image**

You can also run the Ed Sheeran Song Lyrics Generator as a Docker container using the pre-built Docker image vishakh1234/eg. To do so, follow these steps:

Pull the Docker image:

```bash

docker pull vishakh1234/eg
```

Run the Docker container:

```bash

docker run -p 5000:5000 vishakh1234/eg
```

Open your web browser and navigate to http://localhost:5000 to access the Ed Sheeran Song Lyrics Generator.

## **Contributing**

We welcome contributions to enhance the Ed Sheeran Song Lyrics Generator. Feel free to open issues, create pull requests, or suggest improvements. Please refer to our Contributing Guidelines for more information.
License

Enjoy generating Ed Sheeran-style song lyrics with the Ed Sheeran Song Lyrics Generator! If you have any questions or feedback, please don't hesitate to reach out.

Disclaimer: This project is for educational and entertainment purposes only. The generated lyrics may not accurately reflect Ed Sheeran's work and are purely a result of AI text generation.
