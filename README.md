# Income Tax Calculation Project

This project is a simple API developed with **Django** and **Django REST Framework** that calculates the income tax due based on the annual income and deductions provided by the user. The API exposes endpoints that allow the calculation of tax according to the income tax brackets in Brazil.

## Technologies Used

- **Python 3.x**
- **Django 3.x or higher**
- **Django REST Framework**

## Installation and Setup

### Prerequisites

- Python 3.6 or higher installed
- Pip (Python package manager)
- Virtualenv (recommended)

## API Endpoints

| Endpoint                                      | Method | Description                                                                                     |
|-----------------------------------------------|--------|-------------------------------------------------------------------------------------------------|
| `/`                                           | GET    | Returns a status 200 OK.                                                                       |
| `/calculate/<str:value>/`                    | GET    | Calculates the income tax based on the provided income without deductions.                     |
| `/calculate/<str:value>/<str:deductions>/`   | GET    | Calculates the income tax based on the provided income and deductions. Returns either "Isento" if exempt or the calculated tax amount. |
