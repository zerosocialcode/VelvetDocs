"""
Text Parser Module
Detects markdown-like structures and converts to structured format
"""

import re

def parse_text(text):
    """
    Parse input text and detect markdown-like patterns
    
    Supported patterns:
    - # Heading 1
    - ## Heading 2
    - ### Heading 3
    - **bold text**
    - *italic text*
    - - list item
    - > blockquote
    
    Returns: List of dictionaries with type and content
    """
    lines = text.split('\n')
    parsed = []
    in_list = False
    list_items = []
    
    for line in lines:
        line = line.rstrip()
        
        # Skip empty lines but preserve spacing
        if not line.strip():
            if in_list:
                parsed.append({'type': 'list', 'items': list_items})
                list_items = []
                in_list = False
            parsed.append({'type': 'space', 'content': ''})
            continue
        
        # Heading 1: # Text
        if line.startswith('# ') and not line.startswith('## '):
            if in_list:
                parsed.append({'type': 'list', 'items': list_items})
                list_items = []
                in_list = False
            parsed.append({'type': 'h1', 'content': line[2:].strip()})
        
        # Heading 2: ## Text
        elif line.startswith('## ') and not line.startswith('### '):
            if in_list:
                parsed.append({'type': 'list', 'items': list_items})
                list_items = []
                in_list = False
            parsed.append({'type': 'h2', 'content': line[3:].strip()})
        
        # Heading 3: ### Text
        elif line.startswith('### '):
            if in_list:
                parsed.append({'type': 'list', 'items': list_items})
                list_items = []
                in_list = False
            parsed.append({'type': 'h3', 'content': line[4:].strip()})
        
        # Blockquote: > Text
        elif line.startswith('> '):
            if in_list:
                parsed.append({'type': 'list', 'items': list_items})
                list_items = []
                in_list = False
            parsed.append({'type': 'blockquote', 'content': line[2:].strip()})
        
        # List item: - Text or * Text
        elif line.startswith('- ') or line.startswith('* '):
            content = line[2:].strip()
            list_items.append(content)
            in_list = True
        
        # Regular paragraph
        else:
            if in_list:
                parsed.append({'type': 'list', 'items': list_items})
                list_items = []
                in_list = False
            # Parse inline formatting (bold, italic)
            parsed.append({'type': 'paragraph', 'content': line})
    
    # Close any remaining list
    if in_list:
        parsed.append({'type': 'list', 'items': list_items})
    
    return parsed

def parse_inline_formatting(text):
    """
    Parse inline formatting like **bold** and *italic*
    Returns list of tuples: (text, format) where format is 'normal', 'bold', or 'italic'
    """
    result = []
    current_pos = 0
    
    # Find all bold patterns (**text**)
    bold_pattern = r'\*\*(.+?)\*\*'
    # Find all italic patterns (*text*)
    italic_pattern = r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)'
    
    # Combine patterns
    combined_pattern = r'(\*\*(.+?)\*\*)|(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)'
    
    matches = list(re.finditer(combined_pattern, text))
    
    for match in matches:
        # Add text before match
        if match.start() > current_pos:
            result.append((text[current_pos:match.start()], 'normal'))
        
        # Determine if bold or italic
        if match.group(1):  # Bold
            result.append((match.group(2), 'bold'))
        elif match.group(3):  # Italic
            result.append((match.group(3), 'italic'))
        
        current_pos = match.end()
    
    # Add remaining text
    if current_pos < len(text):
        result.append((text[current_pos:], 'normal'))
    
    # If no formatting found, return original text as normal
    if not result:
        result.append((text, 'normal'))
    
    return result
