# Dish.ly CLI Scripts

This directory contains standalone command-line scripts for recipe generation.

## Scripts

### `index.py` - Recipe Generator
Generate recipes for any dish with ingredients and cooking steps.

**Usage:**
```bash
python scripts/index.py
```

**Requirements:**
- GROQ_API_KEY environment variable must be set
- Internet connection for Unsplash image API

### `reverse-recipe.py` - Reverse Recipe Search
Find recipes based on ingredients you have on hand.

**Usage:**
```bash
python scripts/reverse-recipe.py
```

**Requirements:**
- GROQ_API_KEY environment variable must be set
- Internet connection for Unsplash image API

## Setup

Make sure you have installed all dependencies:
```bash
pip install -r ../requirements.txt
```

Set your Groq API key:
```bash
export GROQ_API_KEY="your_api_key_here"
```
