# SIT720 8.1D — Final student actions

The technical project has been completed and checked. Before submitting, complete only these final student-owned items:

1. **Human estimates:** Open `data/part5_ten_property_comparison_template.csv` and enter your own genuine independent estimates in the `Human Estimate` column. Do not copy the ML or LLM values. Then rerun the notebook/Part 5 metrics cell.
2. **Deployment screenshot:** Run `python app.py`, enter a sample property, click **Predict sale price**, and capture a genuine screenshot of the working Gradio interface. Replace the screenshot placeholder in `REPORT_FINAL.pdf` if required by the final submission format.
3. **GitHub link:** Upload this project to GitHub and insert the accessible repository link into the report and README.

## Dataset integrity changes already completed

- 113 rows retained: 33 Parramatta, 36 Blacktown, 44 Mosman.
- Every row has an individual `realestate.com.au` property URL.
- Three suburb-level source pages are retained in `source_page_url`.
- Artificial June-30 contract dates were removed.
- Sale year is retained instead of unsupported exact-date precision.
- `source_checked_date` records the final source-check date.
- Figure 2 and Figure 3 captions are correct.
- Five largest prediction errors are now actually ranked by absolute error before selection.
- The notebook executes without errors.
- `squared=False` is not used.
- The deployment code uses Gradio consistently.

## Important

Do not fabricate human estimates, screenshots or access links. They must be genuine evidence from the student's own work/environment.
