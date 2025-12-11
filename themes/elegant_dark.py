"""
Elegant Dark Theme
Sophisticated dark background with gold accents
"""

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch

class ElegantDarkTheme:
    """Elegant dark theme with gold accents"""
    
    def __init__(self):
        self.name = "Elegant Dark"
        
        # Color palette - Dark and luxurious
        self.colors = {
            'primary': HexColor('#D4AF37'),      # Gold
            'secondary': HexColor('#C9A961'),    # Light gold
            'accent': HexColor('#F5DEB3'),       # Wheat/tan
            'background': HexColor('#1A1A1A'),   # Almost black
            'text': HexColor('#E8E8E8'),         # Light grey
            'blockquote': HexColor('#2A2A2A')    # Dark grey
        }
        
        # Margins
        self.margins = {
            'top': 1.1 * inch,
            'bottom': 1.0 * inch,
            'left': 1.1 * inch,
            'right': 1.1 * inch
        }
    
    def get_styles(self):
        """Return dictionary of paragraph styles"""
        styles = {}
        
        # Heading 1 - Elegant gold
        styles['Heading1'] = ParagraphStyle(
            'CustomHeading1',
            fontName='Times-Bold',
            fontSize=24,
            textColor=self.colors['primary'],
            spaceAfter=14,
            spaceBefore=10,
            alignment=TA_CENTER
        )
        
        # Heading 2 - Light gold
        styles['Heading2'] = ParagraphStyle(
            'CustomHeading2',
            fontName='Times-Bold',
            fontSize=18,
            textColor=self.colors['secondary'],
            spaceAfter=12,
            spaceBefore=12,
            alignment=TA_LEFT
        )
        
        # Heading 3 - Wheat color
        styles['Heading3'] = ParagraphStyle(
            'CustomHeading3',
            fontName='Times-Bold',
            fontSize=14,
            textColor=self.colors['accent'],
            spaceAfter=10,
            spaceBefore=10,
            alignment=TA_LEFT
        )
        
        # Body text - Light on dark
        styles['BodyText'] = ParagraphStyle(
            'CustomBodyText',
            fontName='Times-Roman',
            fontSize=12,
            textColor=self.colors['text'],
            alignment=TA_JUSTIFY,
            leading=17,
            spaceAfter=8
        )
        
        # Blockquote - Darker box with gold border
        styles['Blockquote'] = ParagraphStyle(
            'CustomBlockquote',
            fontName='Times-Italic',
            fontSize=11,
            textColor=self.colors['accent'],
            alignment=TA_LEFT,
            leftIndent=30,
            rightIndent=30,
            spaceAfter=12,
            spaceBefore=12,
            borderColor=self.colors['primary'],
            borderWidth=1,
            borderPadding=10,
            backColor=self.colors['blockquote']
        )
        
        # List items
        styles['List'] = ParagraphStyle(
            'CustomList',
            fontName='Times-Roman',
            fontSize=12,
            textColor=self.colors['text'],
            alignment=TA_LEFT,
            leftIndent=25,
            spaceAfter=5
        )
        
        return styles
    
    def add_page_decorations(self, canvas, doc, page_num):
        """Add elegant dark decorations with gold accents"""
        canvas.saveState()
        
        # Fill entire page with dark background
        canvas.setFillColor(self.colors['background'])
        canvas.rect(
            0, 0,
            doc.pagesize[0], doc.pagesize[1],
            fill=True,
            stroke=False
        )
        
        # Gold decorative corners (top)
        canvas.setStrokeColor(self.colors['primary'])
        canvas.setLineWidth(2)
        
        # Top left corner
        canvas.line(doc.leftMargin - 0.2 * inch, doc.height + doc.bottomMargin + 0.3 * inch,
                   doc.leftMargin + 0.5 * inch, doc.height + doc.bottomMargin + 0.3 * inch)
        canvas.line(doc.leftMargin - 0.2 * inch, doc.height + doc.bottomMargin + 0.3 * inch,
                   doc.leftMargin - 0.2 * inch, doc.height + doc.bottomMargin - 0.4 * inch)
        
        # Top right corner
        canvas.line(doc.width + doc.leftMargin + 0.2 * inch, doc.height + doc.bottomMargin + 0.3 * inch,
                   doc.width + doc.leftMargin - 0.5 * inch, doc.height + doc.bottomMargin + 0.3 * inch)
        canvas.line(doc.width + doc.leftMargin + 0.2 * inch, doc.height + doc.bottomMargin + 0.3 * inch,
                   doc.width + doc.leftMargin + 0.2 * inch, doc.height + doc.bottomMargin - 0.4 * inch)
        
        # Footer with elegant page number
        canvas.setFont('Times-Roman', 10)
        canvas.setFillColor(self.colors['primary'])
        canvas.drawCentredString(
            doc.width / 2 + doc.leftMargin,
            0.5 * inch,
            f"~ {page_num} ~"
        )
        
        canvas.restoreState()
