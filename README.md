**🍃 Mango Leaf Disease Detection**
This system automatically detects diseases on mango leaves using a Convolutional Neural Network (CNN) and provides treatment solutions based on the prediction results. The web-based application features a simple and responsive interface, allowing users to upload mango leaf images and receive instant diagnosis and solutions.

**📖 Background**
Mango is a high-value agricultural commodity, especially in tropical countries like Indonesia. However, mango production is often disrupted by leaf diseases such as bacterial canker, gall midge, and sooty mould, which can significantly reduce both yield quality and quantity.
Traditional disease identification relies heavily on expert observation, which is time-consuming, subjective, and not always accessible in rural areas. To address this issue, a deep learning-based solution using Computer Vision and CNN models was developed to provide efficient and accurate detection of mango leaf diseases. The model is trained using the MangoLeafBD dataset available on Kaggle.

**📸 Application Features**

📤 Upload mango leaf images directly from the browser

🧠 Automatically predicts the type of disease using CNN

💡 Provides recommended treatment based on prediction

🖥️ Clean, responsive, and user-friendly interface

**🧠 Detected Diseases**
🦠 Bacterial Canker
🐛 Gall Midge
🍄 Sooty Mould
🌿 Healthy (No Disease)

**🛠️ Technologies Used**
Python : Main programming language
TensorFlow / Keras : Building and training the CNN model
Flask	: Backend framework for the web application
HTML + CSS : User interface styling
Jinja2 : HTML templating engine
Google Colab : Cloud-based training environment

**🧪 Processing Workflow**
**1. Dataset Collection**
Dataset used: MangoLeafBD
Contains 4 classes: Healthy, Gall Midge, Sooty Mould, Bacterial Canker

**2.Image Preprocessing**
All images are resized to 150x150 px. Image augmentation (rotation, flipping) is applied to enhance generalization.

**3.Building the CNN Model**
The model uses three Conv2D + MaxPooling2D layers to extract features, followed by Flatten and Dense layers. A dropout layer is used to prevent overfitting. The final Softmax layer outputs the prediction.

**4.Training and Validation**
Model is trained for 10 epochs using an 80/20 train-validation split.

**5.Model Saving**
After training, the model is saved in .h5 format.

**6.Prediction and Recommendation**
Users can upload a leaf image via the web app, and the model will classify the disease and suggest an appropriate treatment.

**🔗 Useful Links**
📦 Dataset: MangoLeafBD on Kaggle
📓 Google Colab Notebook: Open Notebook

📚 About the Project
**Name: Putri Amanda Sari
Class: 4 TI A
Course: Computer Vision
Lecturer: Ananda, S.Kom., M.T., Ph.D.
Teaching Assistant: Mhd. Anwar, S.Tr. Kom.
Institution: Politeknik Caltex Riau
Year: 2025**

