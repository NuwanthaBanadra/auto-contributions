#!/usr/bin/env python3
"""
Auto Contribution Script
Generates programming quotes and tech facts for automated contributions.
"""

import json
import random
from datetime import datetime
from pathlib import Path


# Collection of programming quotes from famous programmers
PROGRAMMING_QUOTES = [
    {
        "quote": "Programs must be written for people to read, and only incidentally for machines to execute.",
        "author": "Harold Abelson"
    },
    {
        "quote": "The best way to predict the future is to invent it.",
        "author": "Alan Kay"
    },
    {
        "quote": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
        "author": "Martin Fowler"
    },
    {
        "quote": "First, solve the problem. Then, write the code.",
        "author": "John Johnson"
    },
    {
        "quote": "Code is like humor. When you have to explain it, it's bad.",
        "author": "Cory House"
    },
    {
        "quote": "Simplicity is the soul of efficiency.",
        "author": "Austin Freeman"
    },
    {
        "quote": "Before software can be reusable it first has to be usable.",
        "author": "Ralph Johnson"
    },
    {
        "quote": "Make it work, make it right, make it fast.",
        "author": "Kent Beck"
    },
    {
        "quote": "Premature optimization is the root of all evil.",
        "author": "Donald Knuth"
    },
    {
        "quote": "Software is a great combination between artistry and engineering.",
        "author": "Bill Gates"
    },
    {
        "quote": "Talk is cheap. Show me the code.",
        "author": "Linus Torvalds"
    },
    {
        "quote": "The only way to learn a new programming language is by writing programs in it.",
        "author": "Dennis Ritchie"
    },
    {
        "quote": "Debugging is twice as hard as writing the code in the first place.",
        "author": "Brian Kernighan"
    },
    {
        "quote": "Perfection is achieved not when there is nothing more to add, but rather when there is nothing more to take away.",
        "author": "Antoine de Saint-Exupery"
    },
    {
        "quote": "Programming is not about typing, it's about thinking.",
        "author": "Rich Hickey"
    },
    {
        "quote": "Testing leads to failure, and failure leads to understanding.",
        "author": "Burt Rutan"
    },
    {
        "quote": "It's not a bug – it's an undocumented feature.",
        "author": "Anonymous"
    },
    {
        "quote": "The best error message is the one that never shows up.",
        "author": "Thomas Fuchs"
    },
    {
        "quote": "Simplicity is prerequisite for reliability.",
        "author": "Edsger W. Dijkstra"
    },
    {
        "quote": "One of my most productive days was throwing away 1000 lines of code.",
        "author": "Ken Thompson"
    },
    {
        "quote": "The most disastrous thing that you can ever learn is your first programming language.",
        "author": "Alan Kay"
    },
    {
        "quote": "Good code is its own best documentation.",
        "author": "Steve McConnell"
    },
    {
        "quote": "Walking on water and developing software from a specification are easy if both are frozen.",
        "author": "Edward V. Berard"
    },
    {
        "quote": "In programming, the hard part isn't solving problems, but deciding what problems to solve.",
        "author": "Paul Graham"
    },
    {
        "quote": "Controlling complexity is the essence of computer programming.",
        "author": "Brian Kernighan"
    }
]

# Collection of interesting tech facts
TECH_FACTS = [
    {
        "fact": "The first computer bug was an actual bug - a moth found in the Harvard Mark II computer in 1947.",
        "category": "History"
    },
    {
        "fact": "Python was named after Monty Python's Flying Circus, not the snake.",
        "category": "Programming Languages"
    },
    {
        "fact": "The first version of Git was created by Linus Torvalds in just 10 days.",
        "category": "Tools"
    },
    {
        "fact": "JavaScript was created in just 10 days by Brendan Eich in 1995.",
        "category": "Programming Languages"
    },
    {
        "fact": "The term 'debugging' predates computers and was used in aeronautics before WWII.",
        "category": "History"
    },
    {
        "fact": "The first computer programmer was Ada Lovelace, who wrote an algorithm for Charles Babbage's Analytical Engine in 1843.",
        "category": "History"
    },
    {
        "fact": "The first domain name ever registered was Symbolics.com on March 15, 1985.",
        "category": "Internet"
    },
    {
        "fact": "There are over 700 programming languages in existence today.",
        "category": "Programming Languages"
    },
    {
        "fact": "The original name for Java was Oak, named after an oak tree outside James Gosling's office.",
        "category": "Programming Languages"
    },
    {
        "fact": "C++ was originally called 'C with Classes'.",
        "category": "Programming Languages"
    },
    {
        "fact": "The term 'cloud computing' was inspired by the cloud symbol used to represent the internet in flowcharts.",
        "category": "Cloud Computing"
    },
    {
        "fact": "Linux runs on over 90% of the world's supercomputers.",
        "category": "Operating Systems"
    },
    {
        "fact": "The average programmer makes 100-150 errors per 1,000 lines of code.",
        "category": "Development"
    },
    {
        "fact": "NASA still uses software written in the 1970s for some of its spacecraft operations.",
        "category": "Space Technology"
    },
    {
        "fact": "The first version of Windows, Windows 1.0, was released in 1985.",
        "category": "Operating Systems"
    },
    {
        "fact": "GitHub was launched in 2008 and now hosts over 200 million repositories.",
        "category": "Tools"
    },
    {
        "fact": "The term 'algorithm' comes from the name of a 9th-century Persian mathematician, Al-Khwarizmi.",
        "category": "Computer Science"
    },
    {
        "fact": "The first email was sent by Ray Tomlinson to himself in 1971. He doesn't remember what it said.",
        "category": "Internet"
    },
    {
        "fact": "Binary code is the foundation of all computer programming, using only 1s and 0s.",
        "category": "Computer Science"
    },
    {
        "fact": "The world's first website is still online: http://info.cern.ch/",
        "category": "Internet"
    },
    {
        "fact": "Python uses indentation to define code blocks, making it unique among major programming languages.",
        "category": "Programming Languages"
    },
    {
        "fact": "The fastest supercomputer can perform over 1 quintillion calculations per second.",
        "category": "Hardware"
    },
    {
        "fact": "FORTRAN is the oldest programming language still in use today, created in 1957.",
        "category": "Programming Languages"
    },
    {
        "fact": "The term 'cookie' in web browsing was derived from 'magic cookie', an old computing term.",
        "category": "Internet"
    },
    {
        "fact": "Stack Overflow receives over 50 million visitors each month.",
        "category": "Development"
    }
]


def generate_contribution():
    """Generate a contribution entry with either a quote or a fact."""
    # Randomly choose between a quote and a fact
    content_type = random.choice(['quote', 'fact'])
    
    if content_type == 'quote':
        selected = random.choice(PROGRAMMING_QUOTES)
        content = {
            "type": "quote",
            "text": selected["quote"],
            "author": selected["author"]
        }
    else:
        selected = random.choice(TECH_FACTS)
        content = {
            "type": "fact",
            "text": selected["fact"],
            "category": selected["category"]
        }
    
    # Add timestamp
    timestamp = datetime.now().isoformat()
    
    return {
        "timestamp": timestamp,
        "content": content
    }


def save_contribution(contribution):
    """Save the contribution to a JSON file."""
    # Create contributions directory if it doesn't exist
    contrib_dir = Path(__file__).parent.parent / "contributions"
    contrib_dir.mkdir(exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"contribution_{timestamp}.json"
    filepath = contrib_dir / filename
    
    # Save to file
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(contribution, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Contribution saved to {filename}")
    return filepath


def display_contribution(contribution):
    """Display the contribution in a nice format."""
    content = contribution["content"]
    timestamp = contribution["timestamp"]
    
    print("\n" + "="*60)
    print(f"📅 Timestamp: {timestamp}")
    print("="*60)
    
    if content["type"] == "quote":
        print(f"\n💭 Programming Quote:\n")
        print(f'"{content["text"]}"')
        print(f"\n    — {content['author']}")
    else:
        print(f"\n🔍 Tech Fact ({content['category']}):\n")
        print(f"{content['text']}")
    
    print("\n" + "="*60 + "\n")


def main():
    """Main function to generate and save a contribution."""
    print("🤖 Auto Contribution Generator")
    print("-" * 60)
    
    # Generate contribution
    contribution = generate_contribution()
    
    # Display it
    display_contribution(contribution)
    
    # Save it
    filepath = save_contribution(contribution)
    
    print(f"📝 Contribution successfully created!")


if __name__ == "__main__":
    main()
