# 🍽️ Dish.ly

**AI-Powered Recipe Generator** built for UOttaHack 7

Dish.ly is an intelligent recipe discovery platform that uses Groq's Llama 3.3 AI model to generate custom recipes based on your preferences. Whether you're searching for a specific dish or trying to figure out what to cook with ingredients you have on hand, Dish.ly has you covered!

## ✨ Features

- **🔍 Recipe Search**: Enter any dish name and get detailed ingredients and step-by-step cooking instructions
- **🔄 Reverse Recipe Search**: Input ingredients you have, and discover what dishes you can make
- **🖼️ Beautiful Food Images**: Automatic food photography from Unsplash API
- **⚡ Fast AI Generation**: Powered by Groq's lightning-fast Llama 3.3-70B model
- **🎨 Clean, Modern UI**: Responsive design with intuitive user experience

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Groq API key ([Get one here](https://console.groq.com))
- Unsplash API key ([Get one here](https://unsplash.com/developers))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Dish.ly.git
   cd Dish.ly
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   export GROQ_API_KEY="your_groq_api_key_here"
   ```
   
   Or create a `.env` file (see `.env.example`)

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser**
   Navigate to `http://localhost:8000`

## 🛠️ Technology Stack

- **Backend**: Django 5.1.5
- **AI Model**: Groq API with Llama 3.3-70B-Versatile
- **Image API**: Unsplash API
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite (development)

## 📁 Project Structure

```
Dish.ly/
├── Groq/                   # Main Django app
│   ├── templates/          # HTML templates
│   ├── static/             # CSS and static files
│   ├── views.py            # View logic and API integration
│   └── urls.py             # URL routing
├── hackathon/              # Django project settings
│   ├── settings.py         # Project configuration
│   └── urls.py             # Main URL configuration
├── scripts/                # Standalone utility scripts
│   ├── index.py            # CLI recipe generator
│   └── reverse-recipe.py   # CLI reverse recipe search
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## 🎯 Usage

### Web Interface

1. **Search for a Recipe**
   - Enter a dish name (e.g., "pizza", "spaghetti carbonara")
   - Click "Search"
   - View ingredients and cooking steps with a beautiful food image

2. **Reverse Recipe Search** (Coming Soon)
   - Enter ingredients you have
   - Get suggestions for dishes you can make

### Command Line Scripts

Run standalone scripts from the `scripts/` directory:

```bash
# Recipe generator
python scripts/index.py

# Reverse recipe search
python scripts/reverse-recipe.py
```

## 🔑 API Keys Configuration

The application requires two API keys:

1. **Groq API Key**: Set as environment variable `GROQ_API_KEY`
2. **Unsplash API Key**: Currently hardcoded in `views.py` (line 104)

⚠️ **Security Note**: For production, move all API keys to environment variables or a secure secrets manager.

## 🤝 Contributing

This project was created for UOttaHack 7. Contributions, issues, and feature requests are welcome!

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👥 Team

Created with ❤️ at UOttaHack 7

## 🙏 Acknowledgments

- [Groq](https://groq.com) for providing fast AI inference
- [Unsplash](https://unsplash.com) for beautiful food photography
- [Meta](https://ai.meta.com) for the Llama 3.3 model
- UOttaHack 7 organizers and mentors

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Happy Cooking! 🍳**
