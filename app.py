import joblib
import numpy as np
import pandas as pd
import gradio as gr

MODEL_PATH = "data/best_housing_model.joblib"
model = joblib.load(MODEL_PATH)

SUBURBS = ["PARRAMATTA", "BLACKTOWN", "MOSMAN"]


def predict_price(suburb, bedrooms, bathrooms, parking, land_area, sale_year):
    try:
        land_area = float(land_area) if land_area not in (None, "") else np.nan
        bedrooms = int(bedrooms)
        bathrooms = int(bathrooms)
        parking = int(parking)
        sale_year = int(sale_year)
        log_land_area = np.log1p(land_area) if pd.notna(land_area) and land_area >= 0 else np.nan
        bed_bath_ratio = bedrooms / bathrooms if bathrooms > 0 else np.nan
        X = pd.DataFrame([{
            "locality": str(suburb).upper(),
            "num_bed": bedrooms,
            "num_bath": bathrooms,
            "num_parking": parking,
            "log_land_area": log_land_area,
            "bed_bath_ratio": bed_bath_ratio,
            "sale_year": sale_year,
        }])
        pred = float(model.predict(X)[0])
        return f"Estimated sale price: ${pred:,.0f}"
    except Exception as exc:
        return f"Input error: {exc}"


with gr.Blocks(title="Sydney Housing Price Prediction") as demo:
    gr.Markdown("# Sydney Housing Price Prediction\nDecision-support prototype using the trained Gradient Boosting model.")
    gr.Markdown("Enter the basic property characteristics below. The estimate is a model prediction, not an official valuation.")
    with gr.Row():
        suburb = gr.Dropdown(SUBURBS, value="PARRAMATTA", label="Suburb")
        bedrooms = gr.Number(value=3, precision=0, label="Bedrooms")
        bathrooms = gr.Number(value=2, precision=0, label="Bathrooms")
    with gr.Row():
        parking = gr.Number(value=1, precision=0, label="Parking spaces")
        land_area = gr.Number(value=500, label="Land area (m²)")
        sale_year = gr.Number(value=2026, precision=0, label="Reference sale year")
    predict = gr.Button("Predict sale price")
    output = gr.Textbox(label="Prediction")
    predict.click(predict_price, [suburb, bedrooms, bathrooms, parking, land_area, sale_year], output)
    gr.Markdown("**Limitations:** The model uses a small sample and basic structured features. Premium characteristics such as views, renovation quality and exact street position are not directly represented.")

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, show_error=True)
