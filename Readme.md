# Blur Airdrop 2 Helper (Selenium + Python)

## Prerequisites

- install [python](https://www.python.org/downloads/)
- install [selenium python lib](https://selenium-python.readthedocs.io/)
- install [chromedriver](https://chromedriver.chromium.org/downloads)
- export metamask extension from you browser ([how to](https://www.alphr.com/export-chrome-extensions/)), rename to `metamask.crx` and put in the current folder

## Steps

0. Generate new wallet using metamask (it will print the address, seed and mnemonic in the terminal, save json with those details and store a screenshot in the current folder for you to backup):

```
python metamask-new-wallet.py
```

1. Top up your new wallet with some ETH (E.g. using FTX/Blockfolio without fees)

2. Run the Script to buy and list the cheapest item in the selected collection using following format:

```
python metamask.py --url https://blur.io/collection/dotbit --price=0.01 --seed="ENTER 12 WORDS SEED PHRASE HERE PLEASE PLEASE PLEASE PLEASE PLEASE PLEASE"
```

3. If you do not want to used arguments, edit configuration in `metamask.py` and add them there:

```
seed = "ENTER YOUR SEED HERE"
collection = "https://blur.io/collection/async-blueprints"
listPrice = "0.01"
python metamask.py
```
