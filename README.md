# Exa Search and Contents Skill for Hermes

This directory defines the `exa-search-hermes` skill. With this skill, the Hermes agent can leverage the Exa AI API to perform deep searches and extract LLM-ready markdown from web pages.

### Folder Structure
- **`SKILL.md`**: Main definition and instructions for the agent.
- **`references/`**: Official Exa documentation for the `/search` and `/contents` endpoints.
- **`templates/`**: Example configurations, JSON payload schemas, and dependency manifests.
- **`scripts/`**: Ready-to-use Python automation scripts using the `exa-py` SDK.

### Setup

1. Copy the `.env.example` in `templates/` to `.env` in the root of the skill.
2. Provide your API key:
   ```env
   EXA_API_KEY=your_exa_api_key_here
   ```
3. Install the dependencies to run the helper scripts:
   ```bash
   pip install -r templates/requirements.txt
   # or
   npm install exa-js
   ```

You are now ready to use this skill!
