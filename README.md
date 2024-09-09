---

# Cloudflare AI API

This project provides an API using FastAPI to interact with Cloudflare's AI services. The API includes functionalities for text summarization, translation, and a chatbot, all powered by Cloudflare AI.

## Features

- **Text Summarization**: Condense long pieces of text into shorter summaries.
- **Text Translation**: Translate text from one language to another.
- **Chatbot**: A friendly assistant that responds to user queries.

## Endpoints

### 1. Summarization

**Endpoint:** `/summarize/`

**Method:** `POST`

**Description:** Summarizes the input text.

**Request Body:**
```json
{
  "input_text": "Your text here",
  "max_length": 50
}
```

**Response:**
```json
{
  "summary": "Summarized text here."
}
```

### 2. Translation

**Endpoint:** `/translate/`

**Method:** `POST`

**Description:** Translates the input text from one language to another.

**Request Body:**
```json
{
  "text": "Text to translate",
  "source_lang": "en",
  "target_lang": "fr"
}
```

**Response:**
```json
{
  "translation": "Translated text here."
}
```

### 3. Chatbot

**Endpoint:** `/chat/`

**Method:** `POST`

**Description:** Interact with the chatbot.

**Request Body:**
```json
{
  "message": "Your message here"
}
```

**Response:**
```json
{
  "response": "Chatbot reply here."
}
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/benedictdebrah/Demo2.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the root directory.
   - Add your Cloudflare API token:
     ```
     API_TOKEN=your_token_here
     ```

4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

5. Access the API documentation:
   - Navigate to `http://localhost:8000/docs` to see interactive API documentation.

