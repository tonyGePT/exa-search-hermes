---
name: exa-search-hermes
description: Conduct high-quality AI-native searches and extract LLM-ready content using the Exa API. Suitable for deep research, factual lookups, and structured data extraction.
---

# Exa Search and Contents Skill for Hermes

This skill integrates the Exa API, allowing the Hermes agent to perform advanced web searches and extract clean, LLM-ready markdown content from any URL.

## Triggers
- When the user asks to search the web for information about recent events, companies, people, or research papers.
- When the user provides URLs and asks to extract text, summaries, or highlights from them.
- When deep research with structured data extraction is requested.

## Capabilities

### 1. Search (`/search` endpoint)
Perform natural language searches with semantic query capabilities.
- **Search Types**: `auto`, `fast`, `instant`, `deep`, `deep-reasoning`.
- **Content filtering**: Exclude/include domains, filter by category (`company`, `people`, `research paper`, `news`, etc.).
- **Response modes**: Full text, highlights (token efficient), and LLM-generated summaries.

### 2. Contents (`/contents` endpoint)
Extract content from one or more URLs.
- Can handle JS-rendered pages and PDFs.
- Can generate highlights and summaries directly from URLs.
- Supports subpage crawling.

## Integration Details

- **Language/SDK**: Python (`exa-py`), Node (`exa-js`), or raw cURL/HTTP requests.
- **Auth**: Requires an `EXA_API_KEY` defined in the environment or passed via header `x-api-key`.
- **Helper Scripts**: Available in the `scripts/` directory for fast CLI testing or sub-agent execution.
- **Templates**: Example schemas and `.env.example` setup in `templates/`.
- **References**: Full endpoint documentation is provided in the `references/` directory.

## Best Practices & Common Pitfalls
- **Avoid Deprecated Params**: Do NOT use `useAutoprompt`, `numSentences`, `highlightsPerUrl`, `tokensNum`, or `livecrawl: "always"`.
- **Nesting Rules**:
  - For the **`/search`** endpoint: `text`, `highlights`, and `summary` **must** be nested inside `contents`.
  - For the **`/contents`** endpoint: `text`, `highlights`, and `summary` are **top-level** parameters.
- **Token Efficiency**: Use `highlights` (e.g. `{"highlights": {"maxCharacters": 4000}}`) as the default setup for agent operations, as it is 10x more token-efficient than full text.
- **Category Filters**: The `category: "company"` or `category: "people"` filters do not support date filters, text filters, or `excludeDomains`.
- **Error Checking**: The `/contents` endpoint returns a 200 HTTP status even if individual URLs fail. Always check the `statuses` array in the response to determine if a URL was successfully extracted.
