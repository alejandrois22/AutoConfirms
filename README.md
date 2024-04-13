# AutoConfirms

AutoConfirms is a Python-based application designed to automate the email confirmation process for trading transactions. It leverages Selenium for web automation and Tkinter for the graphical user interface, making it easy to manage and run trade confirmations automatically.

## Features

- **Web Automation**: Automates confirmation emails for trading transactions using Selenium.
- **GUI**: Provides an easy-to-use graphical interface to manage companies that should be excluded from receiving confirmations.
- **Customization**: Supports adding and removing keywords to exclude companies dynamically.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

```bash
python -m pip install -r requirements.txt
Installation
Follow these steps to get your development environment up and running:

Clone the repository:
bash
Copy code
git clone https://yourrepositorylink.com/AutoConfirms.git
Navigate to the project directory:
bash
Copy code
cd AutoConfirms
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the application:
bash
Copy code
python src/autoConfirms.py
Usage
To use AutoConfirms, simply follow these steps:

Run the command python src/autoConfirms.py from your terminal.
The GUI will launch, allowing you to add or remove keywords for excluding companies.
Click the "Execute Script" button to initiate the automation process which will manage email confirmations based on your settings.
