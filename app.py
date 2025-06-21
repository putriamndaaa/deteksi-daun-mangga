from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from PIL import Image

app = Flask(__name__)
model = load_model('model_mango_leaf_multiclass_cnn.h5')

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class_labels = ['Bacterial Canker', 'Gall Midge', 'Healthy', 'Sooty Mould']
solutions = {
    'Bacterial Canker': 'Potong bagian yang terinfeksi dan semprotkan bakterisida.',
    'Gall Midge': 'Pangkas daun yang terkena dan gunakan insektisida.',
    'Sooty Mould': 'Bersihkan jamur dengan air sabun ringan.',
    'Healthy': 'Daun sehat, tidak memerlukan tindakan.'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Preprocess image
            img = Image.open(filepath)
            img = img.resize((150, 150))
            img_array = image.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            prediction = model.predict(img_array)
            class_index = np.argmax(prediction)
            class_name = class_labels[class_index]
            solution = solutions[class_name]

            return render_template('index.html',
                                   filename=file.filename,
                                   result=class_name,
                                   solution=solution)
    return render_template('index.html')

@app.route('/display/<filename>')
def display_image(filename):
    return f'/static/uploads/{filename}'

if __name__ == '__main__':
    app.run(debug=True)
