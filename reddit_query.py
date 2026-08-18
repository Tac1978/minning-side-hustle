#!/usr/bin/env python3
"""
Reddit Search Query Generator (Step 2)

Formats search query strings for exploring user pain points on Reddit
for a chosen market segment, based on standard parameters in FRAMEWORK.md.
"""

import argparse
import sys

REDDIT_QUERY_TEMPLATE = """"{market}" (
    site:reddit.com
    inurl:comments|inurl:thread
    | intext:"I think"|"I feel"|"I was"|"I have been"|"I experienced"|"my experience"|"in my opinion"|"IMO"|
    "my biggest struggle"|"my biggest fear"|"I found that"|"I learned"|"I realized"|"my advice"|
    "struggles"|"problems"|"issues"|"challenge"|"difficulties"|"hardships"|"pain point"|
    "barriers"|"obstacles"|"concerns"|"frustrations"|"worries"|"hesitations"|"what I wish I knew"|"what I regret"
)"""


def format_reddit_query(market_segment: str) -> str:
    """
    Formats the Reddit search query string for the specified market segment.
    """
    if not market_segment or not market_segment.strip():
        raise ValueError("Market segment must not be empty.")

    return REDDIT_QUERY_TEMPLATE.format(market=market_segment.strip())


def main():
    parser = argparse.ArgumentParser(
        description="Generate Reddit search query for a market segment based on FRAMEWORK.md"
    )
    parser.add_argument(
        "market_segment",
        type=str,
        help="Market segment to explore (e.g. 'Herbal Remedies', 'Continuous Glucose Monitoring Optimization')"
    )

    args = parser.parse_args()
    try:
        query_str = format_reddit_query(args.market_segment)
        print(query_str)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
