# DailyFuelPriceUpdate
Crawl Vietnam fuel price; predict, display and send notification if change exist via Notion app

# Tunning ARIMA model
`https://www.kaggle.com/code/ngkhtrf/predict-fuel-prices-in-vietnam-use-arima/notebook`

# Setup in linux
- Install python, pip, selenium and relevant:
  - `chmod +x install_requirements/*`
  - `sudo install_requirements\install_requirements.sh`
- Install python requirements: `pip install -r requirements.txt`

# Running
`nohup python3 main.py >> DailyFuelPriceUpdate.log 2>&1 &`
