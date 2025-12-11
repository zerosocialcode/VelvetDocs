"""
Corporate Blue Theme
Professional business document style
"""

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch

class CorporateBlueTheme:
    """Professional corporate theme in blue tones"""
    
    def __init__(self):
        self.name = "Corporate Blue"
        
        # Color palette - Professional blues
        self.colors = {
            'primary': HexColor('#003366'),      # Navy blue
            'secondary': HexColor('#0055A5'),    # Corporate blue
            'accent': HexColor('#66B2FF'),       # Light blue
            'background': HexColor('#FFFFFF'),   # White
            'text': HexColor('#333333'),         # Dark grey
            'blockquote': HexColor('#E6F2FF')    # Very light blue
        }
        
        # Margins
        self.margins = {
            'top': 1.0 * inch,
            'bottom': 1.0 * inch,
            'left': 1.2 * inch,
            'right': 1.2 * inch
        }
    
    def get_styles(self):
        """Return dictionary of paragraph styles"""
        styles = {}
        
        # Heading 1 - Corporate navy
        styles['Heading1'] = ParagraphStyle(
            'CustomHeading1',
            fontName='Helvetica-Bold',
            fontSize=22,
            textColor=self.colors['primary'],
            spaceAfter=14,
            spaceBefore=10,
            alignment=TA_LEFT
        )
        
        # Heading 2 - Blue with underline
        styles['Heading2'] = ParagraphStyle(
            'CustomHeading2',
            fontName='Helvetica-Bold',
            fontSize=17,
            textColor=self.colors['secondary'],
            spaceAfter=11,
            spaceBefore=11,
            alignment=TA_LEFT,
            borderWidth=0,
            borderColor=self.colors['accent']
        )
        
        # Heading 3 - Medium blue
        styles['Heading3'] = ParagraphStyle(
            'CustomHeading3',
            fontName='Helvetica-Bold',
            fontSize=14,
            textColor=self.colors['secondary'],
            spaceAfter=9,
            spaceBefore=9,
            alignment=TA_LEFT
        )
        
        # Body text - Professional and clean
        styles['BodyText'] = ParagraphStyle(
            'CustomBodyText',
            fontName='Helvetica',
            fontSize=11,
            textColor=self.colors['text'],
            alignment=TA_JUSTIFY,
            leading=15,
            spaceAfter=7
        )
        
        # Blockquote - Blue tinted box
        styles['Blockquote'] = ParagraphStyle(
            'CustomBlockquote',
            fontName='Helvetica-Oblique',
            fontSize=10,
            textColor=self.colors['secondary'],
            alignment=TA_LEFT,
            leftIndent=28,
            rightIndent=28,
            spaceAfter=10,
            spaceBefore=10,
            borderColor=self.colors['secondary'],
            borderWidth=0,
            borderPadding=10,
            backColor=self.colors['blockquote']
        )
        
        # List items
        styles['List'] = ParagraphStyle(
            'CustomList',
            fontName='Helvetica',
            fontSize=11,
            textColor=self.colors['text'],
            alignment=TA_LEFT,
            leftIndent=24,
            spaceAfter=4
        )
        
        return styles
    
    def add_page_decorations(self, canvas, doc, page_num):
        """Add corporate header and footer"""
        canvas.saveState()
        
        # Corporate header bar
        canvas.setFillColor(self.colors['primary'])
        canvas.rect(
            0,
            doc.height + doc.bottomMargin + 0.5 * inch,
            doc.pagesize[0],
            0.3 * inch,
            fill=True,
            stroke=False
        )
        
        # Light blue accent bar
        canvas.setFillColor(self.colors['accent'])
        canvas.rect(
            0,
            doc.height + doc.bottomMargin + 0.48 * inch,
            doc.pagesize[0],
            0.05 * inch,
            fill=True,
            stroke=False
        )
        
        # Footer line
        canvas.setStrokeColor(self.colors['secondary'])
        canvas.setLineWidth(1.5)
        canvas.line(
            doc.leftMargin,
            0.7 * inch,
            doc.width + doc.leftMargin,
            0.7 * inch
        )
        
        # Page number
        canvas.setFont('Helvetica', 9)
        canvas.setFillColor(self.colors['secondary'])
        canvas.drawRightString(
            doc.width + doc.leftMargin,
            0.5 * inch,
            f"Page {page_num}"
        )
        
        # Company watermark (optional)
        canvas.setFont('Helvetica-Bold', 10)
        canvas.setFillColor(self.colors['accent'])
        canvas.drawString(
            doc.leftMargin,
            0.5 * inch,
            "VelvetDocs"
        )
        
        canvas.restoreState()
