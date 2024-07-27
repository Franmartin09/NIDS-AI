### NIDS-AI

---

#### Description

NIDS-AI is a Python program designed for continuous and large-scale analysis of potential intrusions using tools such as Zeek, Filebeat, Elasticsearch, and Kibana, all integrated within a Docker environment. This system leverages a pre-trained machine learning model to enhance threat detection in networks.

---
#### Installation

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

---

#### Usage

1. **Example usage:**

   To run NIDS-AI, follow these steps:
   ```bash
   docker-compose up -d   # Start the required Docker containers
   python3 /app/main.py   # Start the intrusion analysis
   ```

2. **Flow description:**

   The application also features a graphical interface with two main buttons: Run and Stop.
   
   When the application is run using the corresponding button, NIDS-AI begins capturing data from the Zeek tool and sends it to the AI model for analysis. If the model detects a threat, the application displays a line indicating the nature of the threat detected in real-time within the same graphical interface.

---

![Main](app/main.png)

<p align="center">
  <img src="app/secondary.png" alt="Secondary">
</p>


#### Contribution

- If you wish to contribute to the development of NIDS-AI, please follow these steps:
  1. Fork the repository.
  2. Create a branch with your new feature (`git checkout -b feature/new-feature`).
  3. Make your changes and commit them (`git commit -am 'Added new feature'`).
  4. Push to the branch (`git push origin feature/new-feature`).
  5. Create a pull request on GitHub.

---

#### License

This project is licensed under the [MIT License](https://github.com/Franmartin09/NIDS-AI/blob/main/LICENSE).

---

#### Contact

For any questions, suggestions, or issues related to NIDS-AI, please contact via email: [Fran Martin](mailto:franmartinaguilar@gmail.com).

---




