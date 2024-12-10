from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Define your plots with descriptions and filenames
    plots = [
        {"id": "plot1", "image": "Racer_emotion.png", "description": "1. This bar plot shows the distribution of emotions (joy, surprise, neutral, sad, anger) expressed in comments for each racer. It helps to visualize which emotions are most prevalent for different racers and identify potential trends or patterns."},
        {"id": "plot2", "image": "Racer_emotion_2.png", "description": "2. This stacked bar plot illustrates the top emotions associated with each racer. It provides a clear comparison of the dominant emotions expressed towards different racers and helps to understand the overall sentiment associated with them"},
        {"id": "plot3", "image": "heatmap.png", "description": "3. This heatmap visualizes the average sentiment score for each racer within their respective constructors. It provides a comprehensive overview of sentiment towards racers and constructors, highlighting potential relationships between the two."}, 
        {"id": "plot4", "image": "Top_racer_positive.png", "description": "4. This bar plot highlights the top racers who received the most positive comments (associated with the emotion joy). It provides insights into which racers are generally perceived more positively by users."}, 
        {"id": "plot5", "image": "Top_racer_negative.png", "description": "5. This bar plot highlights the top racers who received the most negative comments (associated with the emotion anger). It helps to identify racers who might be facing criticism or negative sentiment from users."}, 
        {"id": "plot6", "image": "positive.png", "description": "6. This word cloud visualizes the most frequent words used in comments with positive sentiment. It provides a quick overview of the key themes and topics associated with positive comments."}, 
        {"id": "plot7", "image": "negative.png", "description": "7. This word cloud visualizes the most frequent words used in comments with negative sentiment. It provides a quick overview of the key themes and topics associated with negative comments."}
    ]
    return render_template('index.html', plots=plots)

if __name__ == '__main__':
    app.run(debug=True)
