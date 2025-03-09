# Consumer Sentiment Analysis for Packaging

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg" alt="Framework">
  <img src="https://img.shields.io/badge/AI-OpenAI-412991.svg" alt="AI">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

### A powerful tool that analyzes consumer feedback about packaging designs from multiple sources to extract sentiment and actionable insights.

![IMAGE](https://github.com/user-attachments/assets/e629dd10-7136-43b9-976a-d235fb067080)


## 🔍 Overview

This Streamlit application helps packaging design teams understand consumer sentiment by analyzing:

- **Consumer Reviews** - Direct feedback from buyers about product packaging
- **Survey Responses** - Structured feedback from market research initiatives
- **Social Media Comments** - Real-time, unfiltered opinions from social platforms

Using OpenAI's powerful language models, the application extracts sentiment patterns, identifies key themes, and delivers actionable recommendations to improve packaging design decisions.

![Sentiment Analysis Demo](https://via.placeholder.com/800x400?text=Sentiment+Analysis+Demo)

## ✨ Features

### 📊 Multi-Source Analysis
- Simultaneously analyze feedback from different sources
- Compare sentiment across channels to identify consistency or discrepancies
- Understand which packaging aspects matter most in different contexts

### 🧠 Advanced Sentiment Detection
- Identify positive, negative, and neutral feedback
- Detect nuanced emotions beyond basic sentiment
- Surface key themes and recurring concerns

### 📝 Comprehensive Reports
- Generate source-specific analyses for detailed insights
- Create combined reports that synthesize findings across all channels
- Export reports for sharing with stakeholders

### 🔄 Flexible AI Options
- Choose between different OpenAI models based on your needs
- Optimize for speed or deeper analysis depending on your use case
- Load sample data to test the system's capabilities

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- OpenAI API key

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/lazer-eye-development/sentiment-analysis.git
cd sentiment-analysis
```

2. **Install required packages:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key to the `.env` file
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. **Run the application:**
```bash
streamlit run app.py
```

## 📊 Usage

1. **Enter text in one or more input fields:**
   - Paste consumer reviews in the first tab
   - Add survey responses in the second tab
   - Include social media comments in the third tab

2. **Select your preferred OpenAI model** from the dropdown

3. **Click "Analyze Sentiment"** to process the text

4. **View the results:**
   - Individual analysis for each source
   - Combined insights that synthesize all feedback
   - Download a complete report for sharing

5. **Optional: Load sample data** to see how the analysis works

## 💡 Use Cases

- **Product Development** - Refine packaging based on consumer preferences
- **Market Research** - Understand packaging impact on product perception
- **Sustainability Initiatives** - Identify consumer attitudes toward eco-friendly packaging
- **Competitive Analysis** - Compare feedback on your packaging vs. competitors

## 🔒 Security

The application uses OpenAI's API with secure communication. Your API key is stored locally in the `.env` file and is never shared.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<p align="center">
  <small>Turning consumer feedback into better packaging design</small>
</p>
