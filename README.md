# SOLGPT

**Autoconnect script to [https://solgpt.ai/](https://solgpt.ai/)**

---

## About The Project

SOLGPT is a Python automation script using Pyppeteer that automatically connects to the SolGPT web app. It simulates browser actions to open the site and trigger wallet connection, simplifying the login process for users interacting with SolGPT.

This project is useful for developers or users who want to automate wallet connection on SolGPT without manual interaction.

---

## Features

- Automatically opens https://solgpt.ai/
- Clicks the "Connect Wallet" button
- Handles basic wallet connection flow (customization may be needed for specific wallets)
- Headless browser support for automation environments

---

## Getting Started

### Prerequisites

- Python 3.6 or higher
- [Pyppeteer](https://github.com/pyppeteer/pyppeteer) library

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/Luizfelippe00966/SOLGPT.git
   cd SOLGPT
   ```

2. Install dependencies:

   ```
   pip install pyppeteer
   ```

---

## Usage

Run the autoconnect script:

```
python autoconnect.py
```

This will launch a Chromium browser instance, navigate to SolGPT, and attempt to connect the wallet automatically.

---

## Customization

- Modify the CSS selectors in `autoconnect.py` to match the current SolGPT UI elements if they change.
- For wallet popups (e.g., Phantom wallet), additional handling may be required depending on your setup.
- Set `headless=False` in the script to watch the browser actions for debugging.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for bug fixes, improvements, or new features.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
