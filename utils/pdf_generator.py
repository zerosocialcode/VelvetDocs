"""
PDF Generator Module
Creates PDFs using ReportLab with theme support
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.pdfgen import canvas
from datetime import datetime

# Import all themes
from themes.academic import AcademicTheme
from themes.research_pro import ResearchProTheme
from themes.modern_colorblock import ModernColorblockTheme
from themes.elegant_dark import ElegantDarkTheme
from themes.corporate_blue import CorporateBlueTheme
from themes.softpastel import SoftPastelTheme
from utils.parser import parse_inline_formatting

# Theme registry
THEME_CLASSES = {
    'academic': AcademicTheme,
    'research_pro': ResearchProTheme,
    'modern_colorblock': ModernColorblockTheme,
    'elegant_dark': ElegantDarkTheme,
    'corporate_blue': CorporateBlueTheme,
    'softpastel': SoftPastelTheme
}

def generate_pdf(parsed_content, theme_name, output_path):
    """
    Generate PDF from parsed content using specified theme
    
    Args:
        parsed_content: List of parsed text elements
        theme_name: Name of theme to apply
        output_path: Path where PDF will be saved
    """
    # Get theme class
    theme_class = THEME_CLASSES.get(theme_name, AcademicTheme)
    theme = theme_class()
    
    # Create PDF document
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=theme.margins['right'],
        leftMargin=theme.margins['left'],
        topMargin=theme.margins['top'],
        bottomMargin=theme.margins['bottom']
    )
    
    # Container for PDF elements
    story = []
    
    # Get styles from theme
    styles = theme.get_styles()
    
    # Process each parsed element
    for element in parsed_content:
        elem_type = element['type']
        
        if elem_type == 'h1':
            para = Paragraph(element['content'], styles['Heading1'])
            story.append(para)
            story.append(Spacer(1, 0.3 * inch))
        
        elif elem_type == 'h2':
            para = Paragraph(element['content'], styles['Heading2'])
            story.append(para)
            story.append(Spacer(1, 0.2 * inch))
        
        elif elem_type == 'h3':
            para = Paragraph(element['content'], styles['Heading3'])
            story.append(para)
            story.append(Spacer(1, 0.15 * inch))
        
        elif elem_type == 'paragraph':
            # Process inline formatting
            formatted_text = process_inline_formatting(element['content'], styles)
            para = Paragraph(formatted_text, styles['BodyText'])
            story.append(para)
            story.append(Spacer(1, 0.15 * inch))
        
        elif elem_type == 'blockquote':
            para = Paragraph(element['content'], styles['Blockquote'])
            story.append(para)
            story.append(Spacer(1, 0.15 * inch))
        
        elif elem_type == 'list':
            for item in element['items']:
                formatted_text = f"• {item}"
                para = Paragraph(formatted_text, styles['List'])
                story.append(para)
            story.append(Spacer(1, 0.15 * inch))
        
        elif elem_type == 'space':
            story.append(Spacer(1, 0.1 * inch))
    
    # Build PDF with header and footer
    doc.build(story, onFirstPage=lambda c, d: theme.add_page_decorations(c, d, 1),
              onLaterPages=lambda c, d: theme.add_page_decorations(c, d, doc.page))

def process_inline_formatting(text, styles):
    """
    Convert markdown-style inline formatting to ReportLab XML
    **bold** -> <b>bold</b>
    *italic* -> <i>italic</i>
    """
    import re
    
    # Replace **bold**
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    
    # Replace *italic* (but not if it's part of **)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', text)
    
    return text
