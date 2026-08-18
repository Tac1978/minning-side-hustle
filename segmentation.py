#!/usr/bin/env python3
"""
Market Research & Opportunity Discovery - Market & Niche Segmentation (Step 1)

Generates market categories, subcategories, niches, and sub-niches across three core markets:
Health, Wealth, and Relationships.
"""

import argparse
import sys
from typing import Dict, List, Any, Optional

# Structured Market Segmentation Data
MARKET_DATA: Dict[str, Dict[str, Dict[str, Dict[str, List[str]]]]] = {
    "Health": {
        "Physical Health & Fitness": {
            "Alternative Medicine": {
                "Herbal Remedies": [
                    "Adaptogenic Herbs for Stress Management",
                    "Herbal Teas for Digestive Health",
                    "Medicinal Mushroom Extracts for Immunity"
                ],
                "Acupuncture & Eastern Medicine": [
                    "Community Acupuncture for Chronic Pain",
                    "Traditional Chinese Medicine for Women's Hormonal Health",
                    "Cupping Therapy for Athletic Recovery"
                ]
            },
            "Strength & Conditioning": {
                "Functional Fitness": [
                    "Kettlebell Workouts for Desk Workers",
                    "Calisthenics for Older Adults",
                    "Mobility Training for Powerlifters"
                ],
                "Endurance Training": [
                    "Ultramarathon Preparation",
                    "Zone 2 Cardio for Longevity",
                    "Open-Water Swimming Techniques"
                ]
            },
            "Nutrition & Dietetics": {
                "Specialized Diets": [
                    "Ketogenic Diet for Neurological Health",
                    "Plant-Based Nutrition for Endurance Athletes",
                    "Low-FODMAP Diet for IBS Management"
                ],
                "Metabolic Health": [
                    "Continuous Glucose Monitoring Optimization",
                    "Intermittent Fasting Protocols for Shift Workers",
                    "Insulin Resistance Reversal Strategies"
                ]
            }
        },
        "Mental Health & Well-being": {
            "Mindfulness & Meditation": {
                "Sleep Hygiene Practices": [
                    "Circadian Rhythm Alignment for Insomniacs",
                    "Non-Sleep Deep Rest (NSDR) Protocols",
                    "Biohacking Bedroom Environments"
                ],
                "Stress Reduction": [
                    "Breathwork Techniques for Anxiety Relief",
                    "Somatic Exercises for Trauma Release",
                    "Nature Therapy & Forest Bathing"
                ]
            },
            "Cognitive Performance": {
                "Nootropics & Brain Health": [
                    "Natural Cognitive Enhancers for Age-Related Decline",
                    "Focus Protocols for Adult ADHD",
                    "Memory Retention Strategies for Students"
                ],
                "Neurofeedback": [
                    "EEG Training for Peak Work Performance",
                    "Brainwave Entrainment for Deep Work"
                ]
            }
        }
    },
    "Wealth": {
        "Personal Finance & Wealth Management": {
            "Debt Elimination": {
                "Student Loan Management": [
                    "Refinancing Strategies for Medical Professionals",
                    "Public Service Loan Forgiveness Navigation",
                    "Income-Driven Repayment Plan Optimization"
                ],
                "Consumer Credit Repair": [
                    "Credit Score Optimization for First-Time Homebuyers",
                    "Medical Debt Negotiation Techniques",
                    "Credit Card Debt Snowball Automation"
                ]
            },
            "Investing & Asset Allocation": {
                "Real Estate Investing": [
                    "Short-Term Rental Automation (Airbnb/VRBO)",
                    "House Hacking for Young Professionals",
                    "Commercial Real Estate Syndication for Passive Investors"
                ],
                "Passive Income & Dividend Investing": [
                    "High-Yield Dividend Growth Portfolios",
                    "Index Fund DCA (Dollar-Cost Averaging) Strategies",
                    "Covered Call ETF Income Strategies"
                ]
            }
        },
        "Entrepreneurship & Business Development": {
            "E-Commerce": {
                "Print-on-Demand (POD)": [
                    "Eco-Friendly Apparel POD for Niche Communities",
                    "Custom Merchandise for Content Creators",
                    "Digital Art Prints for Minimalist Home Decor"
                ],
                "Amazon FBA & Private Label": [
                    "Organic Pet Products FBA",
                    "Sustainable Kitchenware Private Labeling",
                    "Ergonomic Home Office Equipment"
                ]
            },
            "Digital Services & Content Creation": {
                "Freelance & Agency Growth": [
                    "AI Prompt Engineering Consulting for SMBs",
                    "B2B Copywriting for SaaS Companies",
                    "Fractional CMO Services for Local Services"
                ],
                "Affiliate Marketing": [
                    "Technical Software Review Sites",
                    "Outdoor Gear Recommendation Blogs",
                    "Financial Technology Comparison Platforms"
                ]
            }
        },
        "Career & Skill Advancement": {
            "Tech Careers": {
                "Cybersecurity": [
                    "Cloud Security Certification Preparation",
                    "Ethical Hacking for FinTech Systems",
                    "Incident Response Training for Remote Teams"
                ],
                "Data Science & AI": [
                    "Machine Learning Engineering for Healthcare",
                    "Data Analytics Bootcamps for Career Changers",
                    "Business Intelligence Dashboarding"
                ]
            }
        }
    },
    "Relationships": {
        "Romantic Relationships": {
            "Dating & Matchmaking": {
                "Dating Advice for Men": [
                    "Profile Optimization for Introverted Men",
                    "Conversation Starters for Long-Distance Dating",
                    "Overcoming Social Anxiety in First Dates"
                ],
                "Dating Advice for Women": [
                    "Setting Boundaries in Early Stages of Dating",
                    "Navigating Online Dating in Your 30s and 40s",
                    "Identifying High-Value Partners"
                ]
            },
            "Relationship Maintenance & Communication": {
                "Couples Therapy & Marriage Enrichment": [
                    "Conflict Resolution for Newlyweds",
                    "Rebuilding Intimacy After Children",
                    "Financial Alignment for Co-habitating Couples"
                ],
                "Long-Distance Relationships": [
                    "Virtual Date Ideas and Bonding Activities",
                    "Transition Planning for Moving In Together",
                    "Communication Schedules for Busy Professionals"
                ]
            }
        },
        "Family & Parenting": {
            "Early Childhood Parenting": {
                "Toddler Behavior & Development": [
                    "Gentle Parenting Strategies for Tantrums",
                    "Montessori-Inspired Home Environments",
                    "Speech & Language Development Games"
                ],
                "Sleep Training": [
                    "Gentle Sleep Training for Infants",
                    "Transitioning Toddlers from Crib to Bed",
                    "Night Weaning Strategies for Nursing Mothers"
                ]
            },
            "Co-Parenting & Blended Families": {
                "Post-Divorce Co-Parenting": [
                    "Communication Apps & Boundaries for High-Conflict Exes",
                    "Blended Family Integration Activities",
                    "Supporting Children Through Family Transitions"
                ]
            }
        },
        "Social & Interpersonal Skills": {
            "Professional Networking & Socializing": {
                "Executive Communication": [
                    "Public Speaking Confidence for Engineers",
                    "Small Talk & Networking for Remote Executives",
                    "Salary Negotiation Communication"
                ]
            },
            "Friendship & Community Building": {
                "Adult Friendship Formation": [
                    "Making Friends After Moving to a New City",
                    "Community Building for Work-From-Home Professionals",
                    "Interest-Based Social Club Organization"
                ]
            }
        }
    }
}


def format_segmentation(
    data: Dict[str, Any],
    indent: int = 0
) -> str:
    """
    Recursively formats the taxonomy hierarchy into standard Markdown bulleted lists.

    Standard Output Format:
    - [Core Market]
      - [Category]
        - [Subcategory]
          - [Niche]
            - [Sub-Niche]
    """
    lines = []
    prefix = " " * indent
    if isinstance(data, dict):
        for key, value in data.items():
            lines.append(f"{prefix}- {key}")
            lines.append(format_segmentation(value, indent + 2))
    elif isinstance(data, list):
        for item in data:
            lines.append(f"{prefix}- {item}")
    return "\n".join(filter(None, lines))


def filter_segmentation(
    query: str,
    data: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Filters the taxonomy data for a specific query/focus.
    Returns only matching branches down the hierarchy.
    If match is at a subcategory or lower level, returns hierarchy starting from that matched level.
    """
    if data is None:
        data = MARKET_DATA

    q = query.strip().lower()
    if not q:
        return data

    filtered: Dict[str, Any] = {}

    for market, categories in data.items():
        if q in market.lower():
            filtered[market] = categories
            continue

        matching_categories: Dict[str, Any] = {}
        for cat, subcategories in categories.items():
            if q in cat.lower():
                matching_categories[cat] = subcategories
                continue

            matching_subcategories: Dict[str, Any] = {}
            for subcat, niches in subcategories.items():
                if q in subcat.lower():
                    matching_subcategories[subcat] = niches
                    continue

                matching_niches: Dict[str, Any] = {}
                for niche, subniches in niches.items():
                    if q in niche.lower():
                        matching_niches[niche] = subniches
                        continue

                    matching_subniches = [
                        sn for sn in subniches if q in sn.lower()
                    ]
                    if matching_subniches:
                        matching_niches[niche] = matching_subniches

                if matching_niches:
                    matching_subcategories[subcat] = matching_niches

            if matching_subcategories:
                matching_categories[cat] = matching_subcategories

        if matching_categories:
            filtered[market] = matching_categories

    return filtered


def get_segmentation_output(query: Optional[str] = None) -> str:
    """
    Generates formatted segmentation output for a general or focused query.
    """
    if query:
        data = filter_segmentation(query)
    else:
        data = MARKET_DATA

    if not data:
        return f"No market segmentation found matching query: '{query}'"

    return format_segmentation(data)


def main():
    parser = argparse.ArgumentParser(
        description="Generate Market & Niche Segmentation across Health, Wealth, and Relationships."
    )
    parser.add_argument(
        "query",
        nargs="?",
        default=None,
        help="Optional specific focus query (e.g., 'alternative medicine', 'wealth')"
    )
    parser.add_argument(
        "-q", "--focus",
        dest="focus_flag",
        default=None,
        help="Optional specific focus query flag"
    )

    args = parser.parse_args()
    query = args.focus_flag or args.query

    output = get_segmentation_output(query)
    print(output)


if __name__ == "__main__":
    main()
