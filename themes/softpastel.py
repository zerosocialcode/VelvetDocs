"""
Minimal Softpastel Theme
Clean, minimalist design with soft pastel colors
"""

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch

class SoftPastelTheme:
    """Minimal theme with soft pastel color palette"""
    
    def __init__(self):
        self.name = "Minimal Softpastel"
        
        # Color palette - Soft pastels
        self.colors = {
            'primary': HexColor('#B39DDB'),      # Soft purple
            'secondary': HexColor('#81C784'),    # Soft green
            'accent': HexColor('#FFB74D'),       # Soft orange
            'background': HexColor('#FAFAFA'),   # Off-white
            'text': HexColor('#424242'),         # Medium grey
            'blockquote': HexColor('#F3E5F5')    # Very light purple
        }
        
        # Margins - Generous spacing
        self.margins = {
            'top': 1.3 * inch,
            'bottom': 1.0 * inch,
            'left': 1.3 * inch,
            'right': 1.3 * inch
        }
    
    def get_styles(self):
        """Return dictionary of paragraph styles"""
        styles = {}
        
        # Heading 1 - Soft purple, minimal
        styles['Heading1'] = ParagraphStyle(
            'CustomHeading1',
            fontName='Helvetica-Bold',
            fontSize=24,
            textColor=self.colors['primary'],
            spaceAfter=16,
            spaceBefore=8,
            alignment=TA_LEFT
        )
        
        # Heading 2 - Soft green
        styles['Heading2'] = ParagraphStyle(
            'CustomHeading2',
            fontName='Helvetica-Bold',
            fontSize=18,
            textColor=self.colors['secondary'],
            spaceAfter=12,
            spaceBefore=14,
            alignment=TA_LEFT
        )
        
        # Heading 3 - Soft orange
        styles['Heading3'] = ParagraphStyle(
            'CustomHeading3',
            fontName='Helvetica',
            fontSize=14,
            textColor=self.colors['accent'],
            spaceAfter=10,
            spaceBefore=10,
            alignment=TA_LEFT
        )
        
        # Body text - Clean and airy
        styles['BodyText'] = ParagraphStyle(
            'CustomBodyText',
            fontName='Helvetica',
            fontSize=11,
            textColor=self.colors['text'],
            alignment=TA_LEFT,
            leading=17,
            spaceAfter=9
        )
        
        # Blockquote - Soft purple background
        styles['Blockquote'] = ParagraphStyle(
            'CustomBlockquote',
            fontName='Helvetica-Oblique',
            fontSize=10,
            textColor=self.colors['primary'],
            alignment=TA_LEFT,
            leftIndent=25,
            rightIndent=25,
            spaceAfter=12,
            spaceBefore=12,
            borderColor=self.colors['primary'],
            borderWidth=0,
            borderPadding=12,
            backColor=self.colors['blockquote']
        )
        
        # List items - Minimal
        styles['List'] = ParagraphStyle(
            'CustomList',
            fontName='Helvetica',
            fontSize=11,
            textColor=self.colors['text'],
            alignment=TA_LEFT,
            leftIndent=20,
            spaceAfter=6
        )
        
        return styles
    
    def add_page_decorations(self, canvas, doc, page_num):
        """Add minimal decorations with pastel accents"""
        canvas.saveState()
        
        # Subtle background tint
        canvas.setFillColor(self.colors['background'])
        canvas.rect(
            0, 0,
            doc.pagesize[0], doc.pagesize[1],
            fill=True,
            stroke=False
        )
        
        # Minimal top accent - small colored dots
        dot_colors = [self.colors['primary'], self.colors['secondary'], self.colors['accent']]
        dot_y = doc.height + doc.bottomMargin + 0.4 * inch
        
        for i, color in enumerate(dot_colors):
            canvas.setFillColor(color)
            canvas.circle(
                doc.leftMargin + (i * 0.3 * inch),
                dot_y,
                0.08 * inch,
                fill=True,
                stroke=False
            )
        
        # Minimal footer - just page number, no lines
        canvas.setFont('Helvetica', 9)
        canvas.setFillColor(self.colors['primary'])
        canvas.drawCentredString(
            doc.width / 2 + doc.leftMargin,
            0.5 * inch,
            str(page_num)
        )
        
        canvas.restoreState()
