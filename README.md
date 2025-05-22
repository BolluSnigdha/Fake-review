## 🕵️‍♀️ Fake Review Detector

A smart web application that detects whether a product/service review is **Fake** or **Real** using a trained Machine Learning model. It includes features like **confidence score**, **dark/light mode**, **speech-to-text input**, and a fun **Lottie animation** for enhanced user experience.

## 🚀 Demo

🔗 https://github.com/BolluSnigdha/Fake-review/blob/main/working.mp4

## 📌 Table of Contents

- [📝 About](#-about)
- [✨ Features](#-features)
- [🧠 Tech Stack](#-tech-stack)
- [📂 Project Structure](#-project-structure)
- [🛠️ Installation](#️-installation)
- [💡 Usage](#-usage)
- [🖼️ Screenshots](#️-screenshots)
- [📈 Model Info](#-model-info)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 📝 About

Fake reviews on e-commerce and service platforms are a growing concern. This project is an attempt to **classify reviews as Real or Fake** using NLP and ML techniques. The frontend is developed with **HTML, Bootstrap, and JS**, and the backend is built with **Flask** and a trained **TF-IDF + Logistic Regression model**.


## ✨ Features

- 🎯 Predicts whether a review is **fake** or **real**
- 📊 Displays **confidence percentage** with progress bar
- 🎤 Accepts **voice input** (Speech-to-Text using Web Speech API)
- 🌙 Toggle between **Dark and Light Mode**
- 🤖 Engaging **Lottie robot animation**
- 🚀 Clean, responsive UI using **Bootstrap 5**

## 🧠 Tech Stack

### Frontend:
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Lottie Web

### Backend:
- Python 3
- Flask
- Scikit-learn
- NLTK
- Pickle

### Machine Learning:
- TF-IDF Vectorization

## 📂 Project Structure

Fake-Review-Detector/
│                   
├── templates/
│   └── index.html              # Main frontend page
│
├── fake\_review\_model.pkl       # Trained ML model
├── tfidf\_vectorizer.pkl        # Trained TF-IDF vectorizer
├── app.py                      # Flask app (backend logic)
├── README.md                   # Project README
├── requirements.txt            # Python dependencies

## 🛠️ Installation

1. **Clone this repository**:
   git clone https://github.com/BolluSnigdha/Fake-review.git
   cd fake-review

2. **Create and activate a virtual environment** (optional but recommended):

   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows


3. **Install required packages**:

   pip install -r requirements.txt
  

4. **Run the Flask app**:
   python app.py
  

5. **Open in browser**:
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 💡 Usage

1. Open the app.
2. Enter a product review in the text area or use the 🎤 mic button to speak.
3. Click **"Analyze Review"**.
4. View the result with a confidence score and color-coded bar:

   * ✅ **Real Review**
   * ❌ **Fake Review**


## 🖼️ Screenshots

### 💻 Light Mode
![image](https://github.com/user-attachments/assets/48127993-73ed-4df3-9fb0-dc298ab49466)



### 🌙 Dark Mode
![image](https://github.com/user-attachments/assets/7f3f2869-4413-4501-8434-f2b1ced73f43)


## 📈 Model Info

* **Vectorizer**: TF-IDF (`TfidfVectorizer`)
* **Training Dataset**: A labeled dataset of fake vs. genuine reviews
* **Text Preprocessing**:

  * Lowercasing
  * Punctuation Removal
  * Stopword Removal
  * Stemming (PorterStemmer)

## 🧪 Testing

* Try entering obvious fake reviews like:

  > “This is the best product in the entire galaxy!!! Must buy!!”
* Or real ones like:

  > “The product was okay, but delivery was delayed. Not satisfied.”


## 📦 Dependencies

List of packages in `requirements.txt`:

```txt
Flask
nltk
scikit-learn
```

Install via:

```bash
pip install -r requirements.txt
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!


## 📬 Contact

**Author**: Snigdha
📧 Email:snigdhachowdary2410@gmail.com
🔗 GitHub: https://github.com/BolluSnigdha

## ⭐ Star the Repository

If you like this project, consider giving it a ⭐ on [GitHub](https://github.com/BolluSnigdha/Fake-review)!


