# 🥛 Milk Quality Prediction

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A machine learning-powered web application that predicts milk quality based on various physical and chemical parameters. This project uses a Random Forest classifier to categorize milk into three quality grades: **High**, **Medium**, and **Low**.

## 🌟 Features

- **Interactive Web Interface**: User-friendly Streamlit application with a modern UI
- **Real-time Prediction**: Instant milk quality assessment based on input parameters
- **Multiple Quality Grades**: Classifies milk into High, Medium, and Low quality categories
- **Comprehensive Analysis**: Considers 7 key parameters for accurate prediction
- **Responsive Design**: Works seamlessly across different devices

## 📊 Parameters Analyzed

The application analyzes the following parameters to determine milk quality:

| Parameter       | Description            | Range       |
| --------------- | ---------------------- | ----------- |
| **pH**          | Acidity/basicity level | 3.0 - 9.5   |
| **Temperature** | Temperature in Celsius | 34°C - 90°C |
| **Taste**       | Taste quality score    | 0.0 - 1.0   |
| **Odor**        | Smell quality score    | 0.0 - 1.0   |
| **Fat**         | Fat content percentage | 0.0 - 1.0   |
| **Turbidity**   | Clarity measurement    | 0.0 - 1.0   |
| **Color**       | Color intensity scale  | 240 - 255   |

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/Milk-Quality_Prediction.git
   cd Milk-Quality_Prediction
   ```

2. **Install required dependencies**

   ```bash
   pip install streamlit pandas numpy scikit-learn
   ```

3. **Run the application**

   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501` to access the application

## 🎯 How to Use

1. **Enter Your Name**: Start by entering your name for a personalized experience
2. **Input pH and Temperature**:
   - pH: Enter the acidity/basicity value (typically 6.0-7.0 for good milk)
   - Temperature: Enter the temperature in Celsius
3. **Rate Quality Parameters** (0.0 to 1.0 scale):
   - **Taste**: How does the milk taste?
   - **Odor**: How does it smell?
   - **Fat**: Fat content percentage
   - **Turbidity**: Clarity of the milk
   - **Color**: Color intensity
4. **Get Prediction**: Click the "Predict!" button to see the quality grade

## 📈 Quality Grades

- **🟢 HIGH QUALITY**: Premium grade milk suitable for direct consumption
- **🟡 MEDIUM QUALITY**: Acceptable quality, may need processing
- **🔴 LOW QUALITY**: Poor quality, not recommended for consumption

## 🛠️ Technical Details

### Model Information

- **Algorithm**: Random Forest Classifier
- **Dataset**: 1,061 milk samples with labeled quality grades
- **Features**: 7 physical and chemical parameters
- **Accuracy**: Trained on comprehensive milk quality dataset

### Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Backend**: Python
- **Machine Learning**: Scikit-learn (Random Forest)
- **Data Processing**: Pandas, NumPy
- **Model Persistence**: Pickle

## 📁 Project Structure

```
Milk-Quality_Prediction/
├── app.py              # Main Streamlit application
├── milknew.csv         # Training dataset
├── rf_model.pkl        # Trained Random Forest model
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

## 🔬 Dataset Information

The model is trained on a comprehensive dataset containing:

- **1,061 samples** of milk with quality assessments
- **7 features** for quality prediction
- **3 quality classes**: High, Medium, Low
- **Real-world data** from dairy industry standards

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Dataset contributors for providing comprehensive milk quality data
- Streamlit team for the excellent web framework
- Scikit-learn community for the robust machine learning library

## 📞 Contact

- **Project Link**: [https://github.com/yourusername/Milk-Quality_Prediction](https://github.com/yourusername/Milk-Quality_Prediction)
- **Issues**: [GitHub Issues](https://github.com/yourusername/Milk-Quality_Prediction/issues)

---

⭐ **Star this repository if you found it helpful!**

---

_Made with ❤️ for the dairy industry and machine learning enthusiasts_
