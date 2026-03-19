#!/usr/bin/env python3
"""
CLI utility to perform Exa Search.
Usage: python search.py "latest developments in LLMs"
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
        print("Usage: python search.py <query>")
        sys.exit(1)

    query = sys.argv[1]
    api_key = os.environ.get("EXA_API_KEY")
    if not api_key:
        print("Error: EXA_API_KEY environment variable is not set. Please set it using EXA_API_KEY='your_key'")
        sys.exit(1)

    exa = Exa(api_key=api_key)
    
    # We use highlights to maintain token efficiency for agents, as recommended by docs.
    print(f"Searching Exa for: '{query}'...")
    try:
        # Note: In Python SDK we use snake_case for maxCharacters -> max_characters
        result = exa.search(
            query,
            num_results=5,
            contents={
                "highlights": {"max_characters": 4000}
            }
        )
        print("\n=== Results ===")
        for res in result.results:
            print(f"- {res.title} ({res.url})")
            if hasattr(res, 'highlights') and res.highlights:
                print("  Highlights:")
                for h in res.highlights:
                    print(f"    * {h}")
            print()
    except Exception as e:
        print(f"Error during search: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
