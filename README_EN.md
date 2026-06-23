# xiaoshuo-skill - Novel Writing Assistant Skill

A creative writing assistant skill designed for novel platform authors, helping authors prepare for their novel writing process.

## Features

### 1. Book Title Check
- Check if the book title complies with platform rules and content safety requirements
- Identify sensitive words, special characters, and other violating content
- Provide modification suggestions

### 2. Tag Matching
- Intelligently match novel tags based on the book title
- Support four dimensions: main category, theme, characters, and plot
- Provide matching confidence scores

### 3. Random Generation
- Generate random tag combinations for users without a specific goal
- Support generation by category and theme
- Ensure combinations are non-repetitive

### 4. Writing Guidance
- Provide opening suggestions based on tags
- Recommend similar popular works for reference
- Offer writing tips and anti-AI-style suggestions

## Installation and Usage

### 1. Installation

```bash
python install.py
```

### 2. Launch Interactive Interface

```bash
python start.py
```

### 3. Direct Usage

```python
from xiaoshuo_skill import XiaoShuoSkill

# Create skill instance
skill = XiaoShuoSkill()

# Check book title
result = skill.check_book_name("《Reborn: Urban Cultivation》")
print(result)

# Match tags
result = skill.match_tags("《The CEO's Substitute Bride》")
print(result)

# Random generation
result = skill.generate_random_tags(count=3)
print(result)

# Writing guidance
result = skill.get_writing_guidance(
    main_category="CEO Romance",
    themes=["Modern Romance", "Wealthy Family"],
    characters=["CEO", "Young Lady"],
    plots=["Contract Marriage", "Marriage Before Love"]
)
print(result)
```

### 4. Run Examples

```bash
python example.py
python demo.py
```

## File Structure

```
xiaoshuo-skill/
├── README.md              # Project documentation (Chinese)
├── README_EN.md           # Project documentation (English)
├── USAGE.md               # Usage guide
├── DEVELOPMENT.md         # Development summary
├── SUMMARY.md             # Project summary
├── example.py             # Usage examples
├── demo.py                # Feature demonstration
├── install.py             # Installation script
├── start.py               # Startup script
└── xiaoshuo_skill/        # Main code
    ├── __init__.py         # Main module
    ├── knowledge_base.py   # Knowledge base
    ├── book_checker.py     # Book title checker
    ├── tag_matcher.py      # Tag matcher
    ├── random_generator.py # Random generator
    └── writing_guide.py    # Writing guide
```

## Knowledge Base Content

### Platform Rules
- Basic requirements: Original content, title matching, golden first three chapters, smooth language, chapter structure
- Content red lines: Political sensitivity, pornography and violence, illegal content, values issues, minor protection
- Writing techniques: Golden three chapters, dense excitement points, compact rhythm, hook endings, distinctive character design, face-slapping tropes

### Content Safety Guidelines
- Prohibited content: 8 categories of prohibited content
- Rejection reasons: 10 common reasons for review rejection
- Penalty descriptions: Penalties for violating works

### Novel Tags
- Main categories: 21 categories (Female Suspense, Ancient Romance, Sci-Fi Apocalypse, etc.)
- Themes: 25 themes (Ancient Power Struggle, Suspense Romance, BL, etc.)
- Characters: 40 characters (CEO, Loyal Dog, All-Powerful, etc.)
- Plots: 92 plots (Substitute Marriage, Conquering the Villain, Feng Shui Secrets, etc.)

## Use Cases

### Case 1: New Author
```
User: I want to write a novel, but I don't know what to write about
Skill: Generating 3 random tag combinations for you...
```

### Case 2: Clear Idea
```
User: I want to write a novel called "Reborn: Urban Cultivation"
Skill: Checking book title... Title complies with standards
       Matching tags for you...
       Recommended tags: Modern Brain Hole + Fantasy Romance + Big Shot + Rebirth
```

### Case 3: Need Writing Guidance
```
User: I chose the CEO Romance category, how should I write the opening?
Skill: CEO Romance opening suggestions:
1. Chapter 1: Create strong conflict, such as contract marriage, substitute bride
2. Chapter 2: Show the male lead's powerful aura and female lead's unique charm
3. Chapter 3: Set up suspense, such as female lead's hidden identity, male lead's secret
```

## Important Notes

1. All creations must comply with "Content Safety Guidelines" and "Platform Rules"
2. Avoid AI-style writing, reference more popular works
3. Tag combinations should be reasonable, avoid contradictions
4. Openings should be attractive, follow the golden three chapters rule
5. Keep each chapter between 1500-3000 words, maintain compact rhythm

## Development Plan

### V0.0.1 (Current Version)
- [x] Basic framework setup
- [x] Knowledge base integration
- [x] Book title check feature
- [x] Tag matching feature
- [x] Random generation feature
- [x] Writing guidance feature

### V0.0.2 (Planned)
- [ ] Online search for popular works
- [ ] Smarter tag matching algorithm
- [ ] Personalized recommendation system
- [ ] Writing template generation

### V0.0.3 (Planned)
- [ ] User preference learning
- [ ] Writing progress tracking
- [ ] Community interaction features
- [ ] Data statistics and analysis

## Contributing

Welcome to submit Issues and Pull Requests to improve this skill.

## License

MIT License
