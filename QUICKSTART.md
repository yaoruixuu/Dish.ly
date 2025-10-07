# 🚀 Quick Start Guide

Get Dish.ly up and running in 5 minutes!

## Prerequisites Check

```bash
# Check Python version (need 3.8+)
python3 --version

# Check pip
pip3 --version
```

## Installation Steps

### 1. Install Dependencies
```bash
pip3 install -r requirements.txt
```

### 2. Set Up API Keys

Get your free API keys:
- **Groq**: https://console.groq.com (sign up and create an API key)
- **Unsplash**: https://unsplash.com/developers (create an app to get access key)

Set the Groq API key as an environment variable:
```bash
export GROQ_API_KEY="your_actual_groq_api_key"
```

**Note**: The Unsplash API key is currently hardcoded in `Groq/views.py` line 104. You can replace it with your own key if needed.

### 3. Initialize Database
```bash
python3 manage.py migrate
```

### 4. Run the Server
```bash
python3 manage.py runserver
```

### 5. Open Your Browser
Navigate to: **http://localhost:8000**

## First Recipe

1. Type a dish name (e.g., "chocolate cake")
2. Click "Search"
3. Get instant ingredients and cooking steps with a beautiful image!

## Troubleshooting

### "ModuleNotFoundError: No module named 'django'"
- Run: `pip3 install -r requirements.txt`

### "GROQ_API_KEY not set"
- Make sure you exported the environment variable
- Check: `echo $GROQ_API_KEY`

### Server won't start
- Check if port 8000 is already in use
- Try: `python3 manage.py runserver 8080`

## Next Steps

- Try the CLI scripts in `scripts/` directory
- Read the full [README.md](README.md) for more features
- Check [CONTRIBUTING.md](CONTRIBUTING.md) to contribute

## Need Help?

Open an issue on GitHub or check the documentation!
