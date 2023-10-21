# FoodExpert: Portable Intelligent Device for Rapid Screening of Pulse Quality and Adulteration

## Short Abstract
Pulses, rich in protein, are susceptible to impurities. FoodExpert, an image-based system, accurately predicts pulse quality and adulteration, achieving 96% accuracy for quality and 94% for adulteration. It can be deployed on a Raspberry Pi and mobile app.

## Folder Structure

- **1. Adulteration Dataset**
- Note : This repo only contains the sample of the data not complete
    - **1.1 Adulteration Grade 1 Dataset:** Contains images representing pulse samples with Grade 1 adulteration.
    - **1.2 Adulteration Grade 2 Dataset:** Contains images representing pulse samples with Grade 2 adulteration.
    - **1.3 Adulteration Grade 3 Dataset:** Contains images representing pulse samples with Grade 3 adulteration.

- **2. Adulteration Dataset Code**
    - **2.1 caller.py:** Runs a sample method call over the class.
    - **2.2 csv_maker.py:** Concatenates various levels of image datasets into a single CSV.
    - **2.3 G1Clr.py, G2Clr.py, G3Clr.py:** Core class modules for handling various adulteration levels.
    - **2.4 model_trainer.py:** Trains the machine learning model and saves a Joblib model.
    - **2.5 userperdaal.py:** Tests a single pulse image using the saved Joblib model.
    - **2.6 Visualize.ipynb:** Jupyter Notebook for visualizing the dataset.

- **3. Grade Quality Dataset**
- - Note : This repo only contains the sample of the data not complete
    - **3.1 Grade 1 Dataset:** Contains images representing high-quality pulse samples (Grade 1).
    - **3.2 Grade 2 Dataset:** Contains images representing pulse samples with Grade 2 quality.
    - **3.3 Grade 3 Dataset:** Contains images representing pulse samples with Grade 3 quality.

- **4. Grade Quality Dataset Code**
    - **4.1 csv_maker.py:** Concatenates various grades of image datasets into a single CSV.
    - **4.2 G1run.py, G2run.py, G3run.py, G4run.py:** Core class modules for handling various grades.
    - **4.3 model.py:** Trains the machine learning model for pulse quality and saves a Joblib model.
    - **4.4 rpi.py:** Runner script for the Raspberry Pi edge module, for real-time quality assessment.
    - **4.5 userperdaal.py:** Tests a single pulse image using the saved Joblib model.

- **5. Flutter Application Build**
    - Contains the complete source code of the Flutter application compatible with embedded version V2, enabling the user to interact with the FoodExpert device.

## Usage

1. Start by exploring the dataset folders (1 and 3) to understand the images of different adulteration and quality grades.
2. Use the code in folders (2) and (4) for data preprocessing, model training, and testing.
3. If you have a Raspberry Pi setup, utilize the `rpi.py` script to enable real-time quality assessment on the edge.
4. For a user-friendly interface, examine and modify the Flutter application in folder (5).

