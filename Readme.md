# Blur Airdrop 2 Helper (Selenium + Python)

## Prerequisites

- install [python](https://www.python.org/downloads/)
- install [selenium python lib](https://selenium-python.readthedocs.io/)
- install [chromedriver](https://chromedriver.chromium.org/downloads)
- export metamask extension from you browser ([how to](https://www.alphr.com/export-chrome-extensions/)), rename to `metamask.crx` and put in the current folder

## Steps

0. Generate new wallet using metamask (it will print the seed in the terrminal and store a screenshot in the current folder for you to backup):

```
python metamask-new-wallet.py
```

1. Top up your new wallet with some ETH (E.g. using FTX/Blockfolio without fees)

2. Edit configuration in `metamask.py`:

```
seed = "ENTER YOUR SEED HERE"
collection = "https://blur.io/collection/async-blueprints"
listPrice = "0.01"
```

3. Run the Script to buy and list the cheapest item in the selected collection:

```
python metamask.py
```
