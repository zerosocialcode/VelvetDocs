# 🎨 VelvetDocs

**Developer:** zerosocialcode

A beautiful, production-ready Flask web application that transforms plain text into stunning, professionally designed PDFs. Choose from 6 distinct themes and watch your content come to life!

![VelvetDocs](https://img.shields.io/badge/Flask-3.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

- **6 Professional Themes**: Academic Clean, Research Pro, Modern Colorblock, Elegant Dark, Corporate Blue, and Minimal Softpastel
- **Markdown Support**: Use familiar markdown syntax for formatting
- **Beautiful UI**: Modern, responsive interface built with Bootstrap 5
- **Instant Preview**: View your PDF before downloading
- **Smart Parser**: Automatically detects headings, lists, quotes, and emphasis
- **Production Ready**: Clean code structure, error handling, and scalability

---

## 🎨 Available Themes

### 1. **Academic Clean**
- Traditional serif typography (Times)
- Professional academic paper style
- Perfect for research papers and formal documents

### 2. **Research Pro**
- Modern sans-serif fonts (Helvetica)
- Structured layout with colored accents
- Ideal for professional research documents

### 3. **Modern Colorblock**
- Vibrant pink, purple, and orange colors
- Bold contemporary design
- Great for creative presentations

### 4. **Elegant Dark**
- Dark background with gold accents
- Sophisticated and luxurious
- Perfect for premium documents

### 5. **Corporate Blue**
- Professional navy and blue tones
- Business-focused layout
- Ideal for corporate reports

### 6. **Minimal Softpastel**
- Soft purple, green, and orange pastels
- Clean, airy spacing
- Perfect for modern, gentle aesthetics

---

## 📋 Supported Formatting

VelvetDocs supports markdown-like syntax:

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*

- List item 1
- List item 2

> Blockquote for important notes
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project**
   ```bash
   cd VelvetDocs
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   ```
   Navigate to: http://localhost:5000
   ```

---

## 📁 Project Structure

```
VelvetDocs/
│
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
│
├── templates/               # HTML templates
│   ├── base.html           # Base template with navbar
│   ├── index.html          # Main page with form
│   └── result.html         # PDF preview page
│
├── themes/                  # PDF theme definitions
│   ├── academic.py         # Academic Clean theme
│   ├── research_pro.py     # Research Pro theme
│   ├── modern_colorblock.py # Modern Colorblock theme
│   ├── elegant_dark.py     # Elegant Dark theme
│   ├── corporate_blue.py   # Corporate Blue theme
│   └── softpastel.py       # Minimal Softpastel theme
│
├── utils/                   # Utility modules
│   ├── parser.py           # Text parsing logic
│   └── pdf_generator.py    # PDF generation engine
│
├── static/                  # Static assets (CSS, JS)
│   ├── css/
│   └── js/
│
└── generated_pdfs/          # Temporary PDF storage
```

---

## 🛠️ How It Works

1. **User Input**: User pastes text and selects a theme
2. **Parsing**: `parser.py` detects markdown-like structures (headings, lists, etc.)
3. **Theme Application**: Selected theme applies colors, fonts, and layout
4. **PDF Generation**: ReportLab creates the PDF with all formatting
5. **Preview & Download**: User can preview and download the final PDF

---

## 🎯 Usage Examples

### Example 1: Academic Paper

```markdown
# The Impact of Climate Change on Marine Ecosystems

## Abstract
This paper examines the **significant effects** of climate change on marine biodiversity.

## Introduction
Climate change represents one of the most *pressing challenges* of our time.

## Key Findings
- Ocean temperatures rising by 0.13°C per decade
- 30% decline in coral reef coverage
- Migration patterns shifting poleward

> "The ocean is changing faster than at any point in recorded history."

## Conclusion
Immediate action is required to mitigate these impacts.
```

### Example 2: Business Report

```markdown
# Q4 2024 Sales Report

## Executive Summary
Record-breaking quarter with **25% growth** in revenue.

## Highlights
- Total revenue: $5.2M
- New customers: 1,200
- Customer satisfaction: 94%

> Key insight: Mobile sales increased by 40%

## Next Quarter Goals
- Expand to 3 new markets
- Launch product line extension
- Increase marketing budget
```

---

## 🔧 Customization

### Adding a New Theme

1. Create a new file in `themes/` (e.g., `my_theme.py`)
2. Define a class with color palette and styles:

```python
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch

class MyTheme:
    def __init__(self):
        self.name = "My Custom Theme"
        self.colors = {
            'primary': HexColor('#FF6B6B'),
            'secondary': HexColor('#4ECDC4'),
            # ... more colors
        }
        self.margins = {
            'top': 1.0 * inch,
            'bottom': 1.0 * inch,
            'left': 1.0 * inch,
            'right': 1.0 * inch
        }
    
    def get_styles(self):
        # Define paragraph styles
        pass
    
    def add_page_decorations(self, canvas, doc, page_num):
        # Add headers, footers, decorations
        pass
```

3. Register in `utils/pdf_generator.py`:

```python
from themes.my_theme import MyTheme

THEME_CLASSES = {
    # ... existing themes
    'my_theme': MyTheme
}
```

4. Add to app.py:

```python
THEMES = {
    # ... existing themes
    'my_theme': 'My Custom Theme'
}
```

---

## 🔒 Security Features

- Maximum file size limit (16MB)
- Input validation
- Automatic cleanup of old PDFs
- No code execution in user input
- CSRF protection ready

---

## 📦 Dependencies

- **Flask 3.0.0**: Web framework
- **ReportLab 4.0.7**: PDF generation
- **Pillow 10.1.0**: Image processing support
- **Werkzeug 3.0.1**: WSGI utilities

---

## 🚢 Deployment

### Production Considerations

1. **Use a production WSGI server** (Gunicorn, uWSGI)
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

2. **Set up proper secret key**
   ```python
   app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
   ```

3. **Use proper file storage** (AWS S3, cloud storage)

4. **Add rate limiting** for API endpoints

5. **Set up monitoring and logging**

### Deploy to Heroku

```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

---

## 🐛 Troubleshooting

### Issue: PDFs not generating

- Check ReportLab installation: `pip install --upgrade reportlab`
- Verify write permissions for `generated_pdfs/` folder
- Check application logs for errors

### Issue: Unicode characters not displaying

- Ensure UTF-8 encoding in parser
- ReportLab supports most Unicode characters by default

### Issue: Theme not applying

- Verify theme name in THEME_CLASSES dictionary
- Check for syntax errors in theme file
- Restart Flask server after theme changes

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute.

---

## 👨‍💻 Developer

**zerosocialcode**

Questions? Suggestions? Feel free to reach out or open an issue!

---

## 🎉 Acknowledgments

- Bootstrap for beautiful UI components
- ReportLab team for excellent PDF generation library
- Flask community for the amazing framework

---

## 🔮 Future Enhancements

- [ ] Add more themes (Newspaper, Magazine, etc.)
- [ ] Support for images in documents
- [ ] Table formatting support
- [ ] Custom theme builder UI
- [ ] Export to other formats (DOCX, HTML)
- [ ] User accounts and saved documents
- [ ] Collaborative editing
- [ ] Template library

---

**Made with ❤️ by zerosocialcode**