# PHY 132 – Activity 3.5 - Magnetic Induction Answer Checker

This repository contains a Streamlit application for PHY 132 Activity 3.5 on Magnetic Induction. The app is designed to help students check their final numerical answers to problems related to magnetic induction, electromagnetic induction, and associated topics. In addition, it provides comprehensive background information on key concepts such as magnetic field formulas, Faraday's Law, magnetic flux, Lenz's Law, centripetal force, Ohm's Law, power dissipation in resistors, and gravitational force and potential energy.

## Overview

The application is divided into two main pages:

- **Answer Checker:**  
  Select a question from a dropdown, input your numerical answer(s), and receive immediate feedback if your answer is within a 1% tolerance of the expected value.

- **Background Information:**  
  Detailed explanations and centered formulas for:
  - Magnetic field configurations (long straight wire, circular loop, and solenoid),
  - Electromagnetic induction (including Faraday’s Law, magnetic flux, and Lenz’s Law),
  - Centripetal force,
  - Ohm's Law and power dissipation in resistors,
  - Gravitational force and gravitational potential energy (using g ≈ 9.81 m/s²).

  The background information also includes diagrams and images that illustrate these concepts. For example, the magnetic flux diagram uses color-coded descriptions (green arrows, salmon-colored areas, red normals).

## Features

- **Interactive Answer Checker:**  
  Verify your numerical answers with a 1% tolerance limit.

- **Comprehensive Background Material:**  
  In-depth explanations and formulas to support your learning in magnetic induction and electromagnetism.

- **Easy Navigation:**  
  Use the sidebar to switch between the Answer Checker and Background Information pages.

## Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/yourusername/phy132-activity-3.5-induction.git
   cd phy132-activity-3.5-induction
   ```

2. **(Optional) Create a virtual environment:**

   ```
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```
   pip install streamlit numpy
   ```

## Usage

Run the application with the following command:

```
streamlit run app.py
```

The app will open in your default web browser. Use the sidebar to navigate between the **Answer Checker** and **Background Information** pages.

## File Structure

```
.
├── app.py               # Main Streamlit application file
├── data
│   ├── qs_3.5.json      # JSON file containing numerical questions and answers for Activity 3.5
│   └── figs             # Directory containing images and diagrams used in the background information
│       ├── B_field_wire.jpg
│       ├── B_field_loop.jpg
│       ├── B_field_solenoid.jpg
│       ├── faraday_anim.gif
│       └── magnetic-flux.png
└── README.md            # This file
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with any improvements or bug fixes. Ensure your changes adhere to the existing style and provide clear commit messages.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or suggestions, please contact **Professor Zakeri** at [m.zakeri@eku.edu](mailto:m.zakeri@eku.edu).

---

This tool was developed for PHY 132 - College Physics II at Eastern Kentucky University.
