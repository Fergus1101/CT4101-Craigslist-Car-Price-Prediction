# CT4101-Craigslist-Car-Price-Prediction
Repository for work on my machine learning project for final year of college. For this we will train a model to accurately predict the resale value of a used car listed on Craigslist based on different attributes like mileage, age, condition and car brand

CT4101 Machine Learning Project - Milestone 1: Project Proposal
Project Title: Predicting Used Vehicle Resale Prices on Craigslist Using Classical Regression Models
Repository Link: 
1. Prediction Question & Task Classification
	Can we accurately predict the resale value of a used car listed on Craigslist based on different attributes like mileage, age, condition and car brand?
	Task Type: Supervised ML - Regression
2. Dataset Details:
	Craigslist Used Vehicle Dataset
	Source: Kaggle
	License: CC0: Public Domain
	Citation: Reese, A. (2021). Used Cars Dataset: Vehicles listings from Craigslist. Kaggle.
https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data
3. Target Variable & Main Input Features
	Target Variable (y): price — Continuous numerical target representing the listing price in USD. 
	Main Input Features (x):
	Numerical: odometer (mileage), year (used to derive vehicle_age). 
	Categorical (Nominal / Ordinal): manufacturer, model, condition, cylinders, fuel, transmission, etc.
	Excluded Columns: Non-predictive data such as listing id, url, image_url, description, and posting_date will be dropped to prevent leakage or unnecessary dimensionality.
4. Data Scale & Quality Issues
	Approximate Scale: The raw dataset contains far too many records (400k) and 26 features. To make a more efficient and manageable dataset, a random sample of 30,000 records will be drawn using a fixed random seed (random_state=42). This way it can be reproduced if ran off of a clean slate.
	Key Quality Issues:
	Extreme outliers: If you have ever scrolled on something like DoneDeal yourself, you know its common for sellers to list their vehicles for 0$, 123456$ or 999999$, so we will use an acceptable range ($500 to $100000)
	Missing Values: There is high missingness across important categorical variables (condition, cylinders, drive) requiring categorical imputation or explicit "missing" flags. 
5. Proposed Baseline, Candidate Models, & Evaluation Metrics
	Baseline Model: DummyRegressor will predict the mean or median target price of the training set to show its learning something useful.
	Candidate Models:
	Ridge / Linear Regression - It assumes a direct mathematical relationship (e.g., as mileage goes up, price goes down at a constant rate).
	RandomForestRegressor - It handles complex, non-linear relationships well (e.g. old cars going back up in value due to becoming vintage).
	KNeighborsRegressor - instance-based distance model (e.g. looking at the average price of the most similar cars in the dataset based on feature distance).
	Evaluation Metrics: Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and Coefficient of Determination (R^2). 
6. Responsible Machine Learning & Risk Considerations
	Privacy & Confidentiality: The dataset consists solely of public listing metadata and doesn’t have any personally identifiable information (PII) such as seller names, email addresses, or exact street locations.
	Fairness & Misuse: There is a possibility of algorithmic bias if the region affects the price, for example lower-income geographic areas could lead to disproportionately undervalued cars.

