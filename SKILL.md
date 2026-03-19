---
name: exa-search-hermes
description: Allow Hermes Agent to conduct high-quality AI-native searches and extract LLM-ready content using the Exa API. Suitable for deep research, factual lookups, and structured data extraction.
version: 1.0.0
metadata:
  hermes:
    tags: [search, web, research, data-extraction]
    category: search
required_environment_variables:
  - name: EXA_API_KEY
    prompt: Exa API key
    help: Get a key from https://dashboard.exa.ai/api-keys
    required_for: full functionality
---

# Exa Search and Contents Skill for Hermes

## When to Use
- When the user asks to search the web for information about recent events, companies, people, or research papers.
- When the user provides URLs and asks to extract text, summaries, or highlights from them.
- When deep research with structured data extraction is requested.
- As an alternative or powerful fallback when standard web scraping fails or is inefficient.

## Procedure
1. **Understand the User Request**: Determine if the goal is a general search (`/search`) or retrieving contents from specific URLs (`/contents`).
2. **Select the Endpoint**:
   - **Search**: Make a call using the `EXA_API_KEY` to the `/search` endpoint. For searches, you **must** wrap desired extraction modes (`text`, `highlights`, `summary`) inside the `contents` property (e.g., `{"contents": {"highlights": {"maxCharacters": 4000}}}`).
   - **Contents**: When extracting from specific URLs, use the `/contents` endpoint. For this endpoint, `text`, `highlights`, and `summary` are **top-level** parameters.
3. **Execute the Request**: Use the provided helper scripts in the `scripts/` directory or run a cURL/HTTP request.
   - Example Search: `python scripts/search.py "query"`
   - Example Contents: `python scripts/get_contents.py <url>`
4. **Parse and Synthesize**: Read the extracted token-efficient markdown text or highlights, and format the final answer for the user based on their specific request.

## Pitfalls
- **Avoid Deprecated Parameters**: Do NOT use `useAutoprompt`, `numSentences`, `highlightsPerUrl`, `tokensNum`, or `livecrawl: "always"`.
- **Nesting Rules Confusion**:
  - For the **`/search`** endpoint: `text`, `highlights`, and `summary` **must** be nested inside `contents`.
  - For the **`/contents`** endpoint: `text`, `highlights`, and `summary` are **top-level** parameters.
- **Context Window Flooding**: Default to using `highlights` (e.g., `{"highlights": {"maxCharacters": 4000}}`) instead of `text`. It extracts the most relevant excerpts and is 10x more token-efficient for agents.
- **Category Filter Restrictions**: The `category: "company"` or `category: "people"` filters do not support date filters, text filters, or `excludeDomains`.
- **Silent URL Failures**: The `/contents` endpoint returns an HTTP 200 even if individual URLs fail to extract. Always check the `statuses` array in the response to verify success.

## Verification
- Confirm that the search effectively retrieved valid document URLs answering the user's query.
- Verify that retrieved text from URLs is in plain text/markdown format and answers the user's ultimate objective without encountering an authentication or `CRAWL_NOT_FOUND` error.
