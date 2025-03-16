# Required Imports
from flask import Flask, request, jsonify
import io
from PIL import Image
import torch
from transformers import DonutProcessor, VisionEncoderDecoderModel


# Flask app
app = Flask(__name__)


# Initialize Model and Processor
Donut_processor = DonutProcessor.from_pretrained(r'C:\Users\amuqt\Work Drive\Learning\Flask_Apps\Parse_Equation\Model Weights')
Donut_model = VisionEncoderDecoderModel.from_pretrained(r'C:\Users\amuqt\Work Drive\Learning\Flask_Apps\Parse_Equation\Model Weights')


# Device setup to cude or cpu
device = "cuda" if torch.cuda.is_available() else "cpu"
Donut_model.to(device)

# set app route and methods
@app.route('/', methods = ['POST'])
def Parse_Equation():
    if 'file' not in request.files:
        return jsonify({'error':'no file provided'}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'no file selected'}), 400
    
    try:
        img = Image.open(io.BytesIO(file.read())).convert("RGB")
        inputs = Donut_processor(images=img, return_tensors="pt")
        generated_ids = Donut_model.generate(pixel_values=inputs["pixel_values"].to(device), max_length=512)
        generated_text = Donut_processor.batch_decode(generated_ids, skip_special_tokens=False)[0]

        # Convert to JSON
        formatted_text = Donut_processor.token2json(generated_text)
        return jsonify({"Extracted equation": formatted_text})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(debug=True)

