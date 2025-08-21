# Revenue v/s Risk Prediction

This project explores the trade-off between revenue generation and risk exposure in financial decision-making. 
By analyzing historical data from major banks such as JPMorgan Chase, Morgan Stanley, Goldman Sachs, Deutsche Bank, and Bank of America, the goal is to quantify how changes in risk levels influence revenue outcomes and to identify a balanced relationship between profitability and stability.

So far, a structured project environment has been setup with clear separation of code, notebooks, and data. All datasets are stored within the project’s `data/` folder, with a distinction between **raw** data collected from APIs or scraped sources, and **processed** data that has been cleaned or transformed for analysis. 
To make storage efficient and portable, every dataset is saved in both CSV and Parquet formats, and helper functions have been implemented to handle reading and writing in a consistent way. 

Initial experiments combined NumPy and pandas to compute vectorized metrics such as correlations, dot products, and revenue deltas. We also integrated a Value-at-Risk (VaR) based risk index to begin capturing actual financial risk alongside revenue. These foundations give us a reproducible workflow that ensures data integrity and prepares the ground for advanced modeling and analysis.

Most recently, a preprocessing layer was added to standardize and clean the data before modeling. This includes handling missing values, applying normalization, and ensuring consistent data types across sources. The cleaned datasets are stored in the processed folder, ensuring a reliable pipeline from data acquisition to analysis. This makes the project ready for the next phase of building and evaluating predictive models.
