# FoodExpert: Portable Intelligent Device for Rapid Screening of Pulse Quality and Adulteration

## Abstract

Pulses are one of the most important food crops in the world due to their higher protein content, approximately 21- 25%. Therefore, it is crucial to analyze the crop’s quality and impurity levels. Stones, pebbles, marble chips, and synthetic dyes such as lead chromate, metanil yellow, artificial colors, etc., are some of the impurities added to pulse products, accidentally or on purpose. The existing analysis techniques are mostly laboratory- based, time-consuming, costly, and require human examination. To address this issue, this paper presents an intelligent system, FoodExpert, based on image processing that automatically uses an image of a pulse sample to identify the region of interest and essential attributes. Then, machine learning frameworks are used to predict pulse quality and adulteration levels based on the obtained parameters. On the test dataset, the suggested model had a 96% accuracy rate for pulse quality prediction and 94% accuracy for adulteration level prediction. The model was successfully deployed on a Raspberry Pi-based hardware prototype and mobile application

## Folder Structure

- **1. Adulteration Dataset**
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
    - **3.1 Grade 1 Dataset:** Contains images representing high-quality pulse samples (Grade 1).
    - **3.2 Grade 2 Dataset:** Contains images representing pulse samples with Grade 2 quality.
    - **3.3 Grade 3 Dataset:** Contains images representing pulse samples with Grade 3 quality.
    - **3.4 Grade 4 Dataset:** Contains images representing pulse samples with Grade 4 quality.

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

