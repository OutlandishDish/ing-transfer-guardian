# ING Guardian

A lightweight Python automation tool that reminds you of upcoming ING transfers and prevents missed payments.

## Features
- Automated reminders for scheduled transfers
- Customisable reminder timing
- Simple Python setup
- Local logging
- Lightweight and dependency-minimal



## Project Structure
ING-Guardian/
├── src/
│   ├── main.py
│   ├── scheduler.py
│   └── utils.py
├── Docs/
│   └── design-brief.md
├── tests/
├── README.md
└── requirements.txt


## Installation

Clone the repository:

git clone https://github.com/<yourname>/ING-Guardian.git
cd ING-Guardian

Create a virtual environment:

python -m venv .venv
.venv\Scripts\activate   # Windows

Install dependencies:

pip install -r requirements.txt


## Usage

Run the main script:

python src/main.py


## Configuration

Edit the configuration values in `config.ini`:

[settings]
transfer_day = 28
reminder_days_before = 3


## Roadmap
- Add email notifications
- Add CLI arguments
- Add unit tests
- Add GitHub Actions CI

## License
MIT License

