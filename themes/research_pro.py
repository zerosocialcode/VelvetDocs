"""
Research Pro Theme
Professional research paper style with modern accents
"""

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch

class ResearchProTheme:
    """Professional research theme with structured layout"""
    
    def __init__(self):
        self.name = "Research Pro"
        
        # Color palette - Professional blues and greys
        self.colors = {
            'primary': HexColor('#1A237E'),      # Deep blue
            'secondary': HexColor('#283593'),    # Medium blue
            'accent': HexColor('#3F51B5'),       # Lighter blue
            'background': HexColor('#FFFFFF'),   # White
            'text': HexColor('#212121'),         # Almost black
            'blockquote': HexColor('#E8EAF6')    # Light blue tint
        }
        
        # Margins
        self.margins = {
            'top': 1.2 * inch,
            'bottom': 1.0 * inch,
            'left': 1.0 * inch,
            'right': 1.0 * inch
        }
    
    def get_styles(self):
        """Return dictionary of paragraph styles"""
        styles = {}
        
        # Heading 1 - All caps, bold
        styles['Heading1'] = ParagraphStyle(
            'CustomHeading1',
            fontName='Helvetica-Bold',
            fontSize=22,
            textColor=self.colors['primary'],
            spaceAfter=14,
            spaceBefore=14,
            alignment=TA_LEFT,
            textTransform='uppercase'
        )
        
        # Heading 2 - Bold, underlined effect
        styles['Heading2'] = ParagraphStyle(
            'CustomHeading2',
            fontName='Helvetica-Bold',
            fontSize=16,
            textColor=self.colors['secondary'],
            spaceAfter=10,
            spaceBefore=12,
            alignment=TA_LEFT,
            borderWidth=0,
            borderColor=self.colors['accent'],
            borderPadding=2
        )
        
        # Heading 3
        styles['Heading3'] = ParagraphStyle(
            'CustomHeading3',
            fontName='Helvetica-Bold',
            fontSize=13,
            textColor=self.colors['secondary'],
            spaceAfter=8,
            spaceBefore=8,
            alignment=TA_LEFT
        )
        
        # Body text - Clean, readable
        styles['BodyText'] = ParagraphStyle(
            'CustomBodyText',
            fontName='Helvetica',
            fontSize=11,
            textColor=self.colors['text'],
            alignment=TA_JUSTIFY,
            leading=15,
            spaceAfter=6
        )
        
        # Blockquote - Highlighted box
        styles['Blockquote'] = ParagraphStyle(
            'CustomBlockquote',
            fontName='Helvetica-Oblique',
            fontSize=10,
            textColor=self.colors['secondary'],
            alignment=TA_LEFT,
            leftIndent=25,
            rightIndent=25,
            spaceAfter=10,
            spaceBefore=10,
            borderColor=self.colors['accent'],
            borderWidth=2,
            borderPadding=8,
            backColor=self.colors['blockquote']
        )
        
        # List items
        styles['List'] = ParagraphStyle(
            'CustomList',
            fontName='Helvetica',
            fontSize=11,
            textColor=self.colors['text'],
            alignment=TA_LEFT,
            leftIndent=25,
            spaceAfter=4
        )
        
        return styles
    
    def add_page_decorations(self, canvas, doc, page_num):
        """Add professional header and footer"""
        canvas.saveState()
        
        # Header bar
        canvas.setFillColor(self.colors['primary'])
        canvas.rect(
            doc.leftMargin,
            doc.height + doc.bottomMargin + 0.3 * inch,
            doc.width,
            0.1 * inch,
            fill=True,
            stroke=False
        )
        
        # Footer with page number and separator
        canvas.setStrokeColor(self.colors['accent'])
        canvas.setLineWidth(1)
        canvas.line(
            doc.leftMargin,
            0.7 * inch,
            doc.width + doc.leftMargin,
            0.7 * inch
        )
        
        canvas.setFont('Helvetica', 9)
        canvas.setFillColor(self.colors['secondary'])
        canvas.drawRightString(
            doc.width + doc.leftMargin,
            0.5 * inch,
            f"Page {page_num}"
        )
        
        canvas.restoreState()
