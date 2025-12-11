"""
Modern Colorblock Theme
Bold, vibrant colors with contemporary design
"""

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch

class ModernColorblockTheme:
    """Bold modern theme with vibrant color blocks"""
    
    def __init__(self):
        self.name = "Modern Colorblock"
        
        # Color palette - Vibrant and modern
        self.colors = {
            'primary': HexColor('#E91E63'),      # Pink/Magenta
            'secondary': HexColor('#9C27B0'),    # Purple
            'accent': HexColor('#FF5722'),       # Orange-red
            'background': HexColor('#FFFFFF'),   # White
            'text': HexColor('#212121'),         # Dark grey
            'blockquote': HexColor('#FCE4EC')    # Light pink
        }
        
        # Margins
        self.margins = {
            'top': 0.9 * inch,
            'bottom': 0.9 * inch,
            'left': 0.9 * inch,
            'right': 0.9 * inch
        }
    
    def get_styles(self):
        """Return dictionary of paragraph styles"""
        styles = {}
        
        # Heading 1 - Large, bold, colored
        styles['Heading1'] = ParagraphStyle(
            'CustomHeading1',
            fontName='Helvetica-Bold',
            fontSize=26,
            textColor=self.colors['primary'],
            spaceAfter=16,
            spaceBefore=0,
            alignment=TA_LEFT
        )
        
        # Heading 2 - Purple accent
        styles['Heading2'] = ParagraphStyle(
            'CustomHeading2',
            fontName='Helvetica-Bold',
            fontSize=19,
            textColor=self.colors['secondary'],
            spaceAfter=12,
            spaceBefore=12,
            alignment=TA_LEFT
        )
        
        # Heading 3 - Orange accent
        styles['Heading3'] = ParagraphStyle(
            'CustomHeading3',
            fontName='Helvetica-Bold',
            fontSize=15,
            textColor=self.colors['accent'],
            spaceAfter=10,
            spaceBefore=10,
            alignment=TA_LEFT
        )
        
        # Body text - Modern sans-serif
        styles['BodyText'] = ParagraphStyle(
            'CustomBodyText',
            fontName='Helvetica',
            fontSize=11,
            textColor=self.colors['text'],
            alignment=TA_LEFT,
            leading=16,
            spaceAfter=8
        )
        
        # Blockquote - Pink background box
        styles['Blockquote'] = ParagraphStyle(
            'CustomBlockquote',
            fontName='Helvetica-Oblique',
            fontSize=11,
            textColor=self.colors['primary'],
            alignment=TA_LEFT,
            leftIndent=20,
            rightIndent=20,
            spaceAfter=12,
            spaceBefore=12,
            borderColor=self.colors['primary'],
            borderWidth=0,
            borderPadding=12,
            backColor=self.colors['blockquote']
        )
        
        # List items - With color accent
        styles['List'] = ParagraphStyle(
            'CustomList',
            fontName='Helvetica',
            fontSize=11,
            textColor=self.colors['text'],
            alignment=TA_LEFT,
            leftIndent=22,
            spaceAfter=5
        )
        
        return styles
    
    def add_page_decorations(self, canvas, doc, page_num):
        """Add colorful modern decorations"""
        canvas.saveState()
        
        # Top color block (gradient effect with multiple bars)
        colors = [self.colors['primary'], self.colors['secondary'], self.colors['accent']]
        bar_height = 0.08 * inch
        
        for i, color in enumerate(colors):
            canvas.setFillColor(color)
            canvas.rect(
                doc.leftMargin + (i * doc.width / 3),
                doc.height + doc.bottomMargin + 0.4 * inch,
                doc.width / 3,
                bar_height,
                fill=True,
                stroke=False
            )
        
        # Side accent bar
        canvas.setFillColor(self.colors['primary'])
        canvas.rect(
            doc.leftMargin - 0.3 * inch,
            doc.bottomMargin,
            0.15 * inch,
            doc.height,
            fill=True,
            stroke=False
        )
        
        # Footer with colorful page number
        canvas.setFont('Helvetica-Bold', 10)
        canvas.setFillColor(self.colors['secondary'])
        canvas.drawCentredString(
            doc.width / 2 + doc.leftMargin,
            0.5 * inch,
            f"— {page_num} —"
        )
        
        canvas.restoreState()
