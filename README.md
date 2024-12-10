# Formula 1 Sentiment Analysis Project

## 📖 Overview

This project analyzes Formula 1-related comments from YouTube to assess audience sentiment regarding racers, teams, and races. Using Natural Language Processing (NLP) techniques, the project extracts insights on fan perceptions, emotional trends, and team popularity across the 2024 season. The analysis includes advanced sentiment classification, emotional engagement analysis, and comparative sentiment visualization for top racers and teams.

---

## 🎯 Objectives

- To analyze fan sentiments about Formula 1 racers, teams, and races using social media data (primarily YouTube comments).
- To identify trends in audience perception, emotional engagement, and racer/team popularity.
- To provide actionable insights for sports analysts, teams, and marketers for improving engagement and strategies.

---

## 🗂️ Project Workflow

1. **Data Collection**  
   - Scraped YouTube comments from 20 race-related videos, accumulating 100,000 comments, focusing on sentiment around drivers, teams, and race events.
   
2. **Data Preprocessing**  
   - Cleaned the data by removing irrelevant comments, stopwords, and special characters using **NLTK**.
   - Filtered comments mentioning specific racers and teams using a predefined list of keywords, ensuring relevance.
   
3. **Sentiment Analysis**  
   - Used **NRC Lexicon** for emotion classification into categories like joy, sadness, anger, fear, and surprise.
   - Implemented **Hugging Face** for multilabel sentiment analysis, identifying different sentiments for the same comment where multiple racers were mentioned (e.g., joy for one driver and anger for another).

4. **Visualization**  
   - Created detailed plots to depict racer and team sentiment trends, emotional engagement, and comparative analysis using **Matplotlib** and **Seaborn**.
   - Developed interactive dashboards using **PySpark** to visualize insights and support decision-making for teams and sponsors.

---

## 🔧 Technologies Used

- **Python**:  
  - Libraries: Pandas, NLTK, NRCLex, Matplotlib, Seaborn, Hugging Face (transformers)
- **Visualization**:  
  - **PySpark** for visualization and interactive dashboard.
- **Jupyter Notebook**:  
  - Used for iterative development and testing of the sentiment analysis pipeline.

---

## 📊 Key Features

- **Emotion Analysis**: Sentiments categorized into joy, sadness, surprise, anger, and fear using NRC Lexicon.
- **Racer Sentiment Trends**: Visualized emotional trends over the season for top racers.
- **Team Insights**: Compared audience perceptions across teams like Red Bull, McLaren, Ferrari, and Mercedes.
- **Audience Engagement**: Ranked top comments by likes to highlight the most resonant fan reactions.

---

## 🖼️ Sample Visualizations

- **Emotional Trends for Top 5 Racers**: A comparison of emotional engagement over the course of the season.
- **Comparative Sentiment Distribution for Leading Teams**: Insights into fan engagement with teams such as Red Bull, Ferrari, McLaren, and Mercedes.
- **Emotion Breakdown for Specific Races**: Detailed sentiment analysis on key races and controversial events.
- **Top 10 Comments by Likes for Each Race**: Highlighting fan engagement and popular content.
- **Heatmap of Constructors vs Sentiments**: Shows the relation between drivers in a team and the sentiment score.
- **Stacked Barplot**: Sentiment Distribution for the top 5 racers 

---

## 🚀 Future Enhancements

- **Social Media Expansion**:  
  - Expand analysis to include data from Twitter, Reddit, and Instagram for broader fan sentiment insights.
- **Real-time Analysis**:  
  - Automate sentiment analysis pipeline to capture real-time sentiment shifts during ongoing races and immediately after events.
- **Predictive Modeling**:  
  - Integrate machine learning models to forecast audience sentiment trends based on historical data and current events.
- **MultiLingual Support**:
  - Support sentiment analysis of multiple languages to help strategize and brand based on local fanbases by sentiments from different regions 

---

## 🤝 Contributions

We welcome feedback and contributions to improve this project. Feel free to open an issue or submit a pull request. Contributions can include expanding the dataset, adding new sentiment analysis techniques, or enhancing visualizations.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 💬 Contact

For queries, reach out to:  
- [Sanjiv Motilal Choudhari](mailto:motilalchoudhari.s@northeastern.edu)  
- LinkedIn: [Sanjiv Motilal Choudhari](https://www.linkedin.com/in/sanjivmotilalchoudhari/)
