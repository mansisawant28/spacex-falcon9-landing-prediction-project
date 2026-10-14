# SpaceX Falcon 9 First-Stage Landing Prediction

IBM Data Science Professional Certificate – Applied Data Science Capstone.

SpaceX advertises Falcon 9 launches at about $62 million, against $165 million or more for other providers, mainly because it can reuse the first stage. This project predicts whether the first stage will land successfully, which lets a competitor estimate the cost of a SpaceX launch.

## Notebooks and files

| Step | File |
|---|---|
| 1. Data collection: SpaceX REST API | `jupyter-labs-spacex-data-collection-api.ipynb` |
| 2. Data collection: web scraping (Wikipedia) | `jupyter-labs-webscraping.ipynb` |
| 3. Data wrangling and landing labels | `labs-jupyter-spacex-Data_wrangling.ipynb` |
| 4. EDA with SQL | `jupyter-labs-eda-sql-coursera_sqllite.ipynb` |
| 5. EDA with data visualization | `edadataviz.ipynb` |
| 6. Interactive map with Folium | `lab_jupyter_launch_site_location.ipynb`, `spacex_folium_maps.html` |
| 7. Dashboard with Plotly Dash | `spacex_dash_app.py` |
| 8. Predictive analysis (classification) | `SpaceX_Machine_Learning_Prediction_Part_5.ipynb` |

## Key results

- 90 Falcon 9 launches analysed; overall landing success rate 66.7%.
- Landing success rose from 0% (2010–2013) to about 90% (2019).
- KSC LC-39A has the highest launch success ratio (76.9%) and the largest share of successful launches (41.7%).
- Logistic regression, SVM and KNN reach 83.3% test accuracy, with no missed landings.

## Notes

- The live SpaceX API (`api.spacexdata.com`) returned a Cloudflare 522 error, so the API notebook falls back to IBM's hosted copy of the same output (`dataset_part_1.csv`).
- `spacex_folium_maps.html` is a standalone version of the three Folium maps; open it in any browser.
- To run the dashboard: `pip install dash pandas plotly`, place `spacex_launch_dash.csv` in the same folder, then `python spacex_dash_app.py`.
