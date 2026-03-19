#!/usr/bin/env python3
"""
CLI utility to fetch contents from Exa API.
Usage: python get_contents.py <url>
Requires EXA_API_KEY to be set in the environment.
"""
import os
import sys
try:
    from exa_py import Exa
except ImportError:
    print("Error: exa_py is not installed. Run `pip install exa-py`")
    sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python get_contents.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    api_key = os.environ.get("EXA_API_KEY")
    if not api_key:
        print("Error: EXA_API_KEY environment variable is not set. Please set it using EXA_API_KEY='your_key'")
        sys.exit(1)

    exa = Exa(api_key=api_key)
    
    print(f"Extracting content for: '{url}'...")
    try:
        # For /contents, text and highlights are top-level args.
        # Python SDK uses snake_case keys for parameters.
        result = exa.get_contents(
            [url],
            text={"max_characters": 5000},
            highlights={"max_characters": 2000}
        )
        
        # Always check statuses as mentioned in docs
        for status in result.statuses:
            if status.status == "error":
                print(f"Failed to extract {status.id} - Error: {status.error.tag}")
                return

        for res in result.results:
            print(f"\nTitle: {res.title}")
            print(f"URL: {res.url}")
            print(f"\n--- Text ---\n{res.text[:1000] if getattr(res, 'text', '') else ''}...\n")
            if hasattr(res, 'highlights') and res.highlights:
                print("--- Highlights ---")
                for h in res.highlights:
                    print(f"- {h}")
    except Exception as e:
        print(f"Error during content extraction: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
