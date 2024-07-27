# NIDS-AI

This repository contains a machine learning project focused on detecting intrusion on a local network. The project employs machine learning techniques to identify intrusions . Below is an overview of the repository contents and instructions for use.

## Repository Contents

- **`Tkinter App`**: Machine learning model usage on visual app
- **`Docker service`**: Zeek | Elastic Stack
- **`notebook.ipynb`**: Jupyter Notebook with the project's code and analysis there are on "preproceso" directory.
- **`Documentation`**: Project documentation in Spanish.
- **`Paper`**: Project paper in Spanish.

## Project Description

NIDS-AI is a Python program designed for continuous and large-scale analysis of potential intrusions using tools such as Zeek, Filebeat, Elasticsearch, and Kibana, all integrated within a Docker environment. This system leverages a pre-trained machine learning model to enhance threat detection in networks.

## Notebook Contents

The Jupyter Notebook (`preproceso/notebook.ipynb`) includes:

1. **Introduction to the Project**: Overview of the project and its objectives.
2. **Description of the Data Source**: Information about the source of the data used.
3. **Description of Data Preprocessing**: Details on data cleaning and transformation techniques.
4. **Graphs**:
   - Fraudulent/Legitimate
   - Box and Whisker
   - Heatmap
5. **Criteria for Evaluating the Data Mining Model**: Methods for assessing model performance.
6. **Execution of Different Machine Learning Methods**:
   - Naive Bayes (NB)
   - K-Nearest Neighbors (KNN)
   - Decision Tree (DT)
   - Support Vector Machine (SVM)
   - AdaBoost (AB)
   - Majority Voting (MV)
   - Bagging (BG)
   - Random Forest (RF)
7. **Comparison and Conclusions**: Comparative analysis of methods and final conclusions.

## Instructions to Run the Notebook

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Franmartin09/IA-Credit-Card
   cd IA-Credit-Card
   ```

2. **Install Dependencies**:

   Ensure Python and Jupyter Notebook are installed. Then, install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Open the Notebook**:

   Launch Jupyter Notebook and open `notebook.ipynb`:

   ```bash
   jupyter notebook notebook.ipynb
   ```

4. **Run the Cells**:

   Execute the cells in the notebook to perform the analysis and visualize the results.


## Instruction to execute the app

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Franmartin09/NIDS-AI.git
   cd NIDS-AI
   ```

2. **Install dependencies:**
   To install the necessary dependencies, run one of the following commands:
   - Using `pip` directly:
     ```bash
     pip install -r requirements.txt
     ```
   - Running the Python script that handles the installation of requirements:
     ```bash
     python install_requirements.py
     ```

## Usage

1. **Example usage:**

   To run NIDS-AI, follow these steps:
   ```bash
   docker-compose up -d   # Start the required Docker containers
   python3 /app/main.py   # Start the intrusion analysis
   ```

2. **Flow description:**

   The application also features a graphical interface with two main buttons: Run and Stop.
   
   When the application is run using the corresponding button, NIDS-AI begins capturing data from the Zeek tool and sends it to the AI model for analysis. If the model detects a threat, the application displays a line indicating the nature of the threat detected in real-time within the same graphical interface.


![Main](app/main.png)

<p align="center">
  <img src="app/secondary.png" alt="Secondary">
</p>

## Documentation

- **[Paper in Spanish](https://github.com/Franmartin09/NIDS-AI/blob/main/Paper%20-%20NIDS%20AI.pdf)**
- **[Documentation in Spanish](https://github.com/Franmartin09/NIDS-AI/blob/main/Documentation%20-%20NIDS%20AI.pdf)**

The documentation provides extensive details about the project, the methods used, and the results obtained.
## Contribution

- If you wish to contribute to the development of NIDS-AI, please follow these steps:
  1. Fork the repository.
  2. Create a branch with your new feature (`git checkout -b feature/new-feature`).
  3. Make your changes and commit them (`git commit -am 'Added new feature'`).
  4. Push to the branch (`git push origin feature/new-feature`).
  5. Create a pull request on GitHub.


## License

This project is licensed under the [MIT License](https://github.com/Franmartin09/NIDS-AI/blob/main/LICENSE).



## Contact

For any questions, suggestions, or issues related to NIDS-AI, please contact via email: [Fran Martin](mailto:franmartinaguilar@gmail.com).

---




