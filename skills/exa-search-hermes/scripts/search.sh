#!/bin/bash
# Basic cURL wrapper for Exa Search
# Usage: ./search.sh "latest LLM models"

if [ -z "$EXA_API_KEY" ]; then
  echo "Error: EXA_API_KEY environment variable is not set"
  exit 1
fi

QUERY=$1
if [ -z "$QUERY" ]; then
  echo "Usage: $0 <query>"
  exit 1
fi

curl -X POST "https://api.exa.ai/search" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $EXA_API_KEY" \
  -d '{
    "query": "'"$QUERY"'",
    "numResults": 5,
    "contents": {
      "highlights": {
        "maxCharacters": 4000
      }
    }
  }'
