# 🍃 Mango Leaf Disease Detection

An intelligent system that automatically detects diseases in mango leaves using a **Convolutional Neural Network (CNN)** and provides treatment suggestions based on prediction results. This web-based application features a clean and responsive interface that allows users to upload mango leaf images and get instant diagnostic feedback.

---

## 📖 Background

Mango is a high-value agricultural commodity, especially in tropical countries like Indonesia. Unfortunately, mango production is often hindered by various leaf diseases, such as *bacterial canker*, *gall midge*, and *sooty mould*, which can reduce both the quality and quantity of yields.

Conventional disease diagnosis relies on expert observation, which is time-consuming and not always available in remote areas. This project leverages **deep learning** and **computer vision** techniques using a **CNN model** trained on the **MangoLeafBD** dataset to accurately and efficiently classify leaf diseases.

---

## 📸 Features

- 📤 Upload mango leaf images directly via the browser  
- 🤖 Automatically predict the disease using a trained CNN model  
- 💊 Show suggested treatment based on prediction results  
- 🖥️ Clean and responsive web interface  

---

## 🧠 Detected Diseases

- 🦠 **Bacterial Canker**
- 🐛 **Gall Midge**
- 🍄 **Sooty Mould**
- 🌿 **Healthy (No Disease)**

---

## 🛠️ Technologies Used

| Technology         | Description                                     |
|--------------------|-------------------------------------------------|
| Python             | Core programming language                       |
| TensorFlow / Keras | Building and training the CNN model             |
| Flask              | Backend web framework                                                    |
| HTML + CSS         | Frontend web design                             |
| Jinja2             | HTML templating                                 |
| Google Colab       | Model development and training environment      |

---
---

## 🧪 Workflow Overview

1. **Dataset Collection**  
   Dataset: [MangoLeafBD (Kaggle)](https://www.kaggle.com/datasets/warcoder/mango-leaf-disease-dataset)

2. **Data Preprocessing**  
   - Resize all images to 150x150 pixels  
   - Apply data augmentation (rotation, flip, zoom)

3. **Model Building**  
   - CNN with Conv2D, MaxPooling, Flatten, Dense, Dropout, and Softmax

4. **Model Training**  
   - 10 training epochs  
   - 80% training, 20% validation split

5. **Model Saving & Prediction**  
   - Save trained model to `.h5`  
   - Load model for web-based predictions  
   - Display results and suggested treatments to users

---

## 💡 Disease Treatment Suggestions

| Disease           | Suggested Treatment                                  |
|-------------------|------------------------------------------------------|
| Bacterial Canker  | Prune infected parts and spray with bactericide      |
| Gall Midge        | Trim affected leaves and apply insecticide           |
| Sooty Mould       | Clean with soapy water and apply fungicide           |
| Healthy           | No treatment needed                                  |

---

## 🧪 Workflow Overview

1. **Dataset Collection**  
   Dataset: [MangoLeafBD (Kaggle)](https://www.kaggle.com/datasets/warcoder/mango-leaf-disease-dataset)

2. **Data Preprocessing**  
   - Resize all images to 150x150 pixels  
   - Apply data augmentation (rotation, flip, zoom)

3. **Model Building**  
   - CNN with Conv2D, MaxPooling, Flatten, Dense, Dropout, and Softmax

4. **Model Training**  
   - 10 training epochs  
   - 80% training, 20% validation split

5. **Model Saving & Prediction**  
   - Save trained model to `.h5`  
   - Load model for web-based predictions  
   - Display results and suggested treatments to users

---

## 💡 Disease Treatment Suggestions

| Disease           | Suggested Treatment                                  |
|-------------------|------------------------------------------------------|
| Bacterial Canker  | Prune infected parts and spray with bactericide      |
| Gall Midge        | Trim affected leaves and apply insecticide           |
| Sooty Mould       | Clean with soapy water and apply fungicide           |
| Healthy           | No treatment needed                                  |

---

🔗 Useful Links

-📦 Dataset: MangoLeafBD on Kaggle

-📓 Model Training Notebook: Google Colab

📚 Project Info

Name: Putri Amanda Sari

Class: 4 TI A

Course: Computer Vision

Lecturer: Ananda, S.Kom., M.T., Ph.D.

Lab Assistant: Mhd. Anwar, S.Tr. Kom.

Institution: Politeknik Caltex Riau

Year: 2025







