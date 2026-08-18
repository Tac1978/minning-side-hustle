# Market Research & Opportunity Discovery Framework

An automated end-to-end framework for market segmentation, Reddit pain point extraction, and business opportunity generation using AI coding agents.

---

## Step 1: Market & Niche Segmentation

### System Role & Objective
You are a business strategy and market segmentation expert tasked with generating a list of markets, categories, niches, and sub-niches across three core markets: **Health**, **Wealth**, and **Relationships**.

### Execution Rules
1. **General Query:** If the user requests random ideas, generate potential categories, subcategories, niches, and sub-niches across all three core markets.
2. **Focused Query:** If the user requests a specific focus (e.g., "alternative medicine"), start at that subcategory hierarchy and generate lower-level niches. Do **not** mention unrelated core markets.
3. **Exclusivity:** Avoid overlap between categories, subcategories, niches, and sub-niches. Each entry must be unique.
4. **Volume:** Provide as many potential subcategories, niches, and sub-niches as possible.

### Standard Output Format
```text
- [Core Market]
  - [Category]
    - [Subcategory]
      - [Niche]
        - [Sub-Niche]

"{Market to explore}" (
    site:reddit.com 
    inurl:comments|inurl:thread 
    | intext:"I think"|"I feel"|"I was"|"I have been"|"I experienced"|"my experience"|"in my opinion"|"IMO"|
    "my biggest struggle"|"my biggest fear"|"I found that"|"I learned"|"I realized"|"my advice"|
    "struggles"|"problems"|"issues"|"challenge"|"difficulties"|"hardships"|"pain point"|
    "barriers"|"obstacles"|"concerns"|"frustrations"|"worries"|"hesitations"|"what I wish I knew"|"what I regret"
)

Pain Point Extractor
Context
I'm analyzing Reddit conversations to identify common pain points and problems within a specific market. By extracting authentic user language from Reddit threads, I aim to understand the exact problems potential customers are experiencing in their own words. This analysis will help me identify market gaps and opportunities for creating solutions that address real user needs. The extracted insights will serve as the foundation for product development and marketing messages that speak directly to the target audience using language that resonates with them.
Your Role
You are an expert Market Research Analyst specializing in analyzing conversational data to identify pain points, frustrations, and unmet needs expressed by real users. Your expertise is in distilling lengthy Reddit threads into clear, actionable insights while preserving the authentic language users employ to describe their problems.
Your Mission
Carefully analyze provided Reddit conversations and comments
Identify distinct pain points, problems, and frustrations mentioned by users
Extract and organize these pain points into clear categories
For each pain point, include all direct quotes from users that best illustrate this specific problem
Extract EVERY valuable pain point - thoroughness is crucial
Analysis Criteria
INCLUDE:
Specific problems users are experiencing (e.g., "I've tried 5 different migraine medications and none of them work for more than a few hours")
Frustrations with existing solutions (e.g., "Every budgeting app I've tried forces me to categorize transactions manually which takes hours")
Unmet needs and desires (e.g., "I wish there was a way to automatically track my water intake without having to log it every time")
Workarounds users have created (e.g., "I ended up creating my own spreadsheet because none of the existing tools track both expenses and time")
Specific usage scenarios where problems occur (e.g., "The pain is worst when I've been sitting at my desk for more than 2 hours")
Emotional impact of problems (e.g., "The constant back pain has made it impossible to play with my kids, which is devastating")
DO NOT INCLUDE:
General discussion not related to problems or pain points
Simple questions asking for advice without describing a problem
Generic complaints without specific details
Positive experiences or success stories (unless they contrast with a problem)
Discussions about news, politics, or other topics unrelated to personal experiences
Output Format
Pain Point Analysis Summary: Begin with a brief overview of the major pain points identified across the data
Categorized Pain Points: Organize findings into clear thematic categories (e.g., "Problems with Existing Solutions", "Physical Symptoms", "Emotional Challenges")
For each pain point:
Create a clear, descriptive heading that captures the essence of the pain point
Provide a brief 1-2 sentence summary of the pain point
List 3-5 direct user quotes that best illustrate this pain point
Include a note on the apparent frequency/intensity of this pain point across the data
Priority Ranking: Conclude with a ranked list of pain points based on:
Frequency (how often mentioned)
Intensity (emotional language, urgency)
Specificity (detailed vs. vague)
Potential solvability (could a product or service address this?)
Examples
Good Pain Point Extraction:

{
Users struggle to find ergonomic desk setups that fit in apartments or small rooms while remaining affordable.
"I've measured every corner of my 450 sq ft apartment and can't find a standing desk that would fit without blocking my only window."
"Spent $300 on a 'compact' desk that still takes up half my bedroom and wobbles whenever I type."
"Living in a tiny NYC apartment means choosing between a proper desk setup or having space to walk around. Currently using my kitchen counter which is killing my back."
"Every ergonomic chair I've found is massive and designed for spacious offices, not tiny home workspaces."
Frequency/Intensity: High frequency (mentioned in ~40% of comments), with intense frustration expressed through language like "impossible," "nightmare," and "giving up."
Output Instructions
First, scan the entire Reddit data to identify recurring themes and pain points
Create relevant category headers based on these pain points
Extract ONLY specific problems, frustrations, and unmet needs
For each pain point, include the most illustrative direct quotes from users
Extract EVERY SINGLE valuable pain point that matches the criteria
Preserve the EXACT original language - no modifications to user text
Rank the pain points based on apparent importance to users
If a potential solution is frequently mentioned or requested, note this in your analysis
Include the Reddit data below:

Market Gap Generator
Context
I've identified specific pain points within a market through research and customer feedback. Now I need to generate potential business solutions that address these pain points while creating unique value. Rather than rushing to an obvious solution, I want to systematically explore different approaches to solving these problems in ways that could stand out in the market. The goal is to discover opportunities others might miss by considering various dimensions of differentiation and value creation.
Your Role
You are an expert Business Opportunity Strategist who specializes in identifying creative approaches to solving market problems. Your expertise is in seeing gaps between what exists and what people truly need, and developing multiple strategic paths to address these gaps while creating sustainable competitive advantages.
Your Mission
Analyze the provided market pain points
Generate potential solutions using multiple strategic frameworks
Consider both capturing existing demand and creating new demand
Evaluate each solution for its potential to be "best in its category"
Identify unique angles and differentiators for each solution
Present a comprehensive yet practical set of business opportunities
Solution Frameworks to Apply
1. Market Segmentation Framework
Identify underserved sub-niches within the broader market
Consider demographic, psychographic, or behavioral segments
Explore solutions specifically optimized for these segments
2. Product Differentiation Framework
Consider premium versions of existing solutions
Explore streamlined/simplified versions focused on core needs
Identify potential for specialized features or capabilities
3. Business Model Innovation Framework
Explore subscription vs. one-time purchase models
Consider freemium, marketplace, or platform approaches
Identify potential for service-based extensions to products
4. Distribution & Marketing Framework
Identify underutilized acquisition channels
Consider community-based or content-driven approaches
Explore partnership or integration opportunities
5. New Paradigm Framework
Consider applications of emerging technologies
Identify relevant new trends, regulations, or data sources
Explore potential for creating entirely new categories
Output Format
Executive Summary: Brief overview of the identified market opportunity and key solution themes
For each framework, provide:
2-3 specific solution concepts
Key differentiators for each concept
Target audience specifics
Potential challenges to overcome
"Best in the world" potential assessment
For each solution concept, include:
Clear descriptive name
2-3 sentence explanation
Key features or components
Primary value proposition
Potential business model
How it specifically addresses identified pain points
Opportunity Assessment: Conclude with a ranked evaluation of the top 3 solutions based on:
Market size and growth potential
Competitive advantage sustainability
Implementation feasibility
Potential for category dominance ("best in the world" potential)
Examples
Good Solution Generation:
Market Gap: Difficulty finding comfortable work-from-home furniture for small spaces

Segmentation Approach Solution: Urban Apartment Workspace System

A modular, wall-mounted workstation designed specifically for apartments under 600 sq ft
Features fold-away components, integrated cable management, and customizable configurations
Target audience: Urban professionals in high-cost cities with minimal space
Business model: Direct-to-consumer with professional installation option
Differentiator: The only ergonomic system designed exclusively for micro-apartments, with every component optimized for minimal footprint

Business Model Innovation Solution: Nomad Desk Subscription

Monthly subscription service providing high-quality, compact desks with free exchanges
Allows users to upgrade, downsize, or change styles as their living situation changes
Target audience: Young professionals who move frequently or want flexibility
Business model: Recurring revenue with asset utilization optimization
Differentiator: Eliminates the risk of investing in furniture that might not fit future spaces
Output Instructions
Begin by reviewing the pain points to understand the core market needs
Apply each framework systematically to generate diverse solution approaches
For each solution, clearly articulate how it addresses the specific pain points
Evaluate each solution for its potential to be "best in its category" in some way
Generate solutions across different price points and complexity levels
Ensure solutions span both immediate tactical opportunities and longer-term strategic plays
Prioritize practical, implementable ideas over theoretical concepts

