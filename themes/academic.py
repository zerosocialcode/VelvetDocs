"""
Academic Clean Theme
Professional, traditional academic paper style with serif fonts
"""

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch

class AcademicTheme:
    """Clean academic theme with traditional serif typography"""
    
    def __init__(self):
        self.name = "Academic Clean"
        
        # Color palette
        self.colors = {
            'primary': HexColor('#2C3E50'),      # Dark blue-grey
            'secondary': HexColor('#34495E'),    # Medium grey
            'accent': HexColor('#7F8C8D'),       # Light grey
            'background': HexColor('#FFFFFF'),   # White
            'text': HexColor('#2C3E50'),         # Dark blue-grey
            'blockquote': HexColor('#ECF0F1')    # Very light grey
        }
        
        # Margins (in inches)
        self.margins = {
            'top': 1.0 * inch,
            'bottom': 1.0 * inch,
            'left': 1.0 * inch,
            'right': 1.0 * inch
        }
    
    def get_styles(self):
        """Return dictionary of paragraph styles for this theme"""
        styles = {}
        
        # Heading 1 - Large, bold, serif
        styles['Heading1'] = ParagraphStyle(
            'CustomHeading1',
            fontName='Times-Bold',
            fontSize=24,
            textColor=self.colors['primary'],
            spaceAfter=12,
            spaceBefore=12,
            alignment=TA_CENTER
        )
        
        # Heading 2 - Medium, bold
        styles['Heading2'] = ParagraphStyle(
            'CustomHeading2',
            fontName='Times-Bold',
            fontSize=18,
            textColor=self.colors['primary'],
            spaceAfter=10,
            spaceBefore=10,
            alignment=TA_LEFT
        )
        
        # Heading 3 - Smaller, bold
        styles['Heading3'] = ParagraphStyle(
            'CustomHeading3',
            fontName='Times-Bold',
            fontSize=14,
            textColor=self.colors['secondary'],
            spaceAfter=8,
            spaceBefore=8,
            alignment=TA_LEFT
        )
        
        # Body text - Justified, serif
        styles['BodyText'] = ParagraphStyle(
            'CustomBodyText',
            fontName='Times-Roman',
            fontSize=12,
            textColor=self.colors['text'],
            alignment=TA_JUSTIFY,
            leading=16,
            spaceAfter=6
        )
        
        # Blockquote - Italic, indented
        styles['Blockquote'] = ParagraphStyle(
            'CustomBlockquote',
            fontName='Times-Italic',
            fontSize=11,
            textColor=self.colors['secondary'],
            alignment=TA_LEFT,
            leftIndent=30,
            rightIndent=30,
            spaceAfter=8,
            spaceBefore=8,
            borderColor=self.colors['accent'],
            borderWidth=0,
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
            leftIndent=20,
            spaceAfter=4
        )
        
        return styles
    
    def add_page_decorations(self, canvas, doc, page_num):
        """Add header, footer, and page decorations"""
        canvas.saveState()
        
        # Footer with page number
        footer_text = f"Page {page_num}"
        canvas.setFont('Times-Roman', 10)
        canvas.setFillColor(self.colors['accent'])
        canvas.drawCentredString(
            doc.width / 2 + doc.leftMargin,
            0.5 * inch,
            footer_text
        )
        
        # Top border line
        canvas.setStrokeColor(self.colors['accent'])
        canvas.setLineWidth(0.5)
        canvas.line(
            doc.leftMargin,
            doc.height + doc.bottomMargin + 0.5 * inch,
            doc.width + doc.leftMargin,
            doc.height + doc.bottomMargin + 0.5 * inch
        )
        
        canvas.restoreState()
