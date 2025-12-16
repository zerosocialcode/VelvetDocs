# VelvetDocs

Hi — I'm zerosocialcode. VelvetDocs is a small Flask app I built to turn plain text (or simple Markdown) into nicely styled PDFs. It comes with several themes so you can pick a look that fits your document.

---

## What it does

- Lets you paste or type text, choose a theme, and get a PDF
- Supports headings, lists, bold/italic, and blockquotes
- Instant preview in the browser before you download
- Six built-in themes to cover academic, business, and creative styles

---

## Themes

Each theme changes fonts, colors and layout so the same content can look very different.

- Academic Clean — serif fonts, conservative spacing, paper-like layout  
- Research Pro — clean sans-serif, structured sections, subtle accents  
- Modern Colorblock — bright color blocks and bold headings  
- Elegant Dark — dark background with gold accents for a premium feel  
- Corporate Blue — navy/blue tones and a business-like layout  
- Minimal Softpastel — soft pastel palette and airy spacing

---

## Supported formatting

You can use simple markdown-like syntax. Examples:

```markdown
# Heading 1
## Heading 2

**Bold**
*Italic*

- List item
> Blockquote
```

---

## Quick start

Requirements
- Python 3.8+
- pip

Install and run

```bash
git clone https://github.com/zerosocialcode/VelvetDocs.git
cd VelvetDocs

python -m venv venv
# activate the venv:
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open http://localhost:5000 in your browser.

---

## Project layout

VelvetDocs (important files)

```
app.py                    # Main Flask app
requirements.txt          # Python dependencies

templates/                # HTML templates
  base.html
  index.html
  result.html

themes/                   # Theme definitions (one file per theme)
utils/                    # parser.py and pdf_generator.py
static/                   # css and js
generated_pdfs/           # temporary PDF storage
```

---

## How it works (brief)

1. You paste text and pick a theme.
2. parser.py parses headings, lists, etc.
3. A theme supplies styles and decorations.
4. pdf_generator.py builds the PDF (ReportLab).
5. You preview and download the PDF.

---

## Examples

Academic paper sample:

```markdown
# The Impact of Climate Change on Marine Ecosystems

## Abstract
This paper examines the **significant effects** of climate change on marine biodiversity.
```

Business report sample:

```markdown
# Q4 2024 Sales Report

## Executive Summary
Record-breaking quarter with **25% growth** in revenue.

- Total revenue: $5.2M
- New customers: 1,200
```

---

## Add a new theme

1. Create a file in `themes/`, e.g. `my_theme.py`.
2. Define a class with colors, margins, and a `get_styles()` method and an `add_page_decorations()` method.
3. Import and register the class in `utils/pdf_generator.py`.
4. Add the theme's display name in `app.py` so it appears in the UI.

Short example:

```python
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch

class MyTheme:
    def __init__(self):
        self.name = "My Custom Theme"
        self.colors = {'primary': HexColor('#FF6B6B')}
        self.margins = {'top': 1.0 * inch, 'bottom': 1.0 * inch,
                        'left': 1.0 * inch, 'right': 1.0 * inch}

    def get_styles(self):
        # return paragraph styles
        pass

    def add_page_decorations(self, canvas, doc, page_num):
        # draw headers/footers or decorations
        pass
```

---

## Security & limits

- Max upload size: 16MB
- Inputs are validated; no code execution from user input
- Old PDFs are cleaned up automatically
- CSRF protection is prepared but make sure to set a proper SECRET_KEY for production

---

## Dependencies

- Flask (3.0.0)
- ReportLab (4.0.7)
- Pillow (10.1.0)
- Werkzeug (3.0.1)

---

## Deployment tips

- Use a production WSGI server like Gunicorn:
  ```bash
  pip install gunicorn
  gunicorn -w 4 -b 0.0.0.0:8000 app:app
  ```
- Configure a secure SECRET_KEY from the environment:
  ```python
  app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
  ```
- Store PDFs in S3 or another persistent store in production
- Add rate limiting and logging for a public deployment

---

## Troubleshooting

- PDFs not generating: check that ReportLab is installed and `generated_pdfs/` is writable.
- Unicode problems: make sure parser and templates use UTF-8.
- Theme not applying: confirm the theme is registered in `pdf_generator.py` and the server was restarted.

---

## Contributing

If you'd like to help, please fork the repo and open a pull request. A simple workflow:

1. Fork
2. git checkout -b feature/my-feature
3. Make changes
4. Commit and push
5. Open a PR

---

## License

MIT — use it, change it, share it.

---

If you want, I can:
- Simplify any section further
- Convert this README into a shorter "quick" README
- Add screenshots or example PDFs to the repo

Made by zerosocialcode
