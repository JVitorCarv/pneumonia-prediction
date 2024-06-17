# Pneumonia Prediction

Describe the project here

## Getting Started

The necessary data files is already be included in the repository. However, if you want to execute everything from step zero, please follow the optional steps below.

## Optional: Obtain Raw Data from Kaggle

If you want to start from scratch and get the raw data directly from Kaggle, you need to:

1. **Download the Kaggle API Token:**

   - You need to have a Kaggle account.
   - Go to your Kaggle account settings and create a new API token.
   - This will download a `kaggle.json` file containing your credentials.

2. **Subscribe to the Competition:**
   - Go to the [RSNA Pneumonia Detection Challenge](https://www.kaggle.com/competitions/rsna-pneumonia-detection-challenge) page.
   - Click "Join Competition" and accept the competition rules.

### Steps to Download and Prepare Data

1. **Place the Kaggle API Token:**

   - Create a `.kaggle` directory in your home directory if it doesn't exist.
     ```sh
     mkdir -p ~/.kaggle
     ```
   - Move the downloaded `kaggle.json` file to the `.kaggle` directory.
     ```sh
     mv /path/to/kaggle.json ~/.kaggle/
     ```
   - Ensure the permissions of the `kaggle.json` file are set correctly.
     ```sh
     chmod 600 ~/.kaggle/kaggle.json
     ```

2. **Download the Data:**

   - Run the `download_kaggle_data.py` script to download and extract the datasets.
     ```sh
     python download_kaggle_data.py
     ```

3. **Prepare the Raw Data:**
   - After downloading the datasets, run the `get_raw_data.py` script to prepare the raw data.
     ```sh
     python get_raw_data.py
     ```
