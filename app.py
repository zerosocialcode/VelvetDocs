"""
VelvetDocs - Flask PDF Generation Application
Developer: zerosocialcode
A modern web app for generating beautifully themed PDFs from text input
"""

from flask import Flask, render_template, request, send_file, jsonify
from utils.parser import parse_text
from utils.pdf_generator import generate_pdf
import os
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'velvetdocs-secret-key-2024'
app.config['UPLOAD_FOLDER'] = 'generated_pdfs'
app.config['IMAGE_FOLDER'] = 'uploaded_images'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

# Ensure folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['IMAGE_FOLDER'], exist_ok=True)

# Available themes
THEMES = {
    'academic': 'Academic Clean',
    'research_pro': 'Research Pro',
    'modern_colorblock': 'Modern Colorblock',
    'elegant_dark': 'Elegant Dark',
    'corporate_blue': 'Corporate Blue',
    'softpastel': 'Minimal Softpastel'
}

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    """Main landing page with text input and theme selection"""
    return render_template('index.html', themes=THEMES)

@app.route('/generate', methods=['POST'])
def generate():
    """
    Process text input and generate PDF with selected theme
    Returns JSON with status and download URL
    """
    try:
        # Get form data
        text_content = request.form.get('content', '')
        theme = request.form.get('theme', 'academic')
        alignment = request.form.get('alignment', 'left')
        
        # Validate inputs
        if not text_content.strip():
            return jsonify({'error': 'Please provide some text content'}), 400
        
        if theme not in THEMES:
            return jsonify({'error': 'Invalid theme selected'}), 400
        
        # Handle image uploads
        uploaded_images = []
        files = request.files.getlist('images')
        
        for file in files:
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                unique_filename = f"{timestamp}_{filename}"
                filepath = os.path.join(app.config['IMAGE_FOLDER'], unique_filename)
                file.save(filepath)
                uploaded_images.append(filepath)
        
        # Parse the text content (detect markdown-like structure)
        parsed_content = parse_text(text_content, uploaded_images)
        
        # Generate unique filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'velvetdocs_{theme}_{timestamp}.pdf'
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Generate PDF with selected theme and alignment
        generate_pdf(parsed_content, theme, filepath, alignment)
        
        return jsonify({
            'success': True,
            'filename': filename,
            'message': 'PDF generated successfully!'
        })
        
    except Exception as e:
        return jsonify({'error': f'Error generating PDF: {str(e)}'}), 500

@app.route('/download/<filename>')
def download(filename):
    """Serve the generated PDF file"""
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(filepath):
            return send_file(filepath, as_attachment=True, download_name=filename)
        else:
            return "File not found", 404
    except Exception as e:
        return f"Error downloading file: {str(e)}", 500

@app.route('/preview/<filename>')
def preview(filename):
    """Display PDF preview page"""
    return render_template('result.html', filename=filename)

# Clean up old files
@app.before_request
def cleanup_old_files():
    """Remove PDF and image files older than 1 hour"""
    try:
        current_time = datetime.now().timestamp()
        
        # Clean PDFs
        for filename in os.listdir(app.config['UPLOAD_FOLDER']):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file_time = os.path.getmtime(filepath)
            if current_time - file_time > 3600:
                os.remove(filepath)
        
        # Clean images
        for filename in os.listdir(app.config['IMAGE_FOLDER']):
            filepath = os.path.join(app.config['IMAGE_FOLDER'], filename)
            file_time = os.path.getmtime(filepath)
            if current_time - file_time > 3600:
                os.remove(filepath)
    except:
        pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
