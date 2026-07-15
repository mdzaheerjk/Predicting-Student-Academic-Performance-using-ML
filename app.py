from flask import Flask, request, render_template
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Safely handle data parsing from form submissions
            reading = request.form.get('reading_score')
            writing = request.form.get('writing_score')
            
            # Fallback to 0 if inputs are empty to prevent float conversion crash
            reading_score = float(reading) if reading else 0.0
            writing_score = float(writing) if writing else 0.0

            # Instantiate data object matching HTML form names
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                # Using 'test_preparation_course' to match the form field string
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=int(reading_score),
                writing_score=int(writing_score)
            )

            # Convert form inputs to a proper pandas DataFrame
            pred_df = data.get_data_as_data_frame()
            print("\n--- Input DataFrame ---")
            print(pred_df)
            print("-----------------------\n")

            print("Before Prediction")
            predict_pipeline = PredictPipeline()
            
            print("Mid Prediction")
            results = predict_pipeline.predict(pred_df)
            
            print("After Prediction")
            # Round result to 2 decimal places for a cleaner UI presentation
            final_result = round(results[0], 2)
            
            return render_template('home.html', results=final_result)

        except Exception as e:
            print(f"Error occurred during web execution: {str(e)}")
            return render_template('home.html', results=f"Error: {str(e)}")

if __name__ == '__main__':
    # Enabled debug=True for instant reloads during development
    app.run(host="0.0.0.0", debug=True, port=5000)
