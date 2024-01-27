# Bitcoin Price Index Script


## Description
The Bitcoin Price Index Script is a Python tool that fetches the current Bitcoin price in USD from the CoinDesk API and calculates the total value in USD based on a provided amount of Bitcoin.

### Key Features:

1. **Real-time Bitcoin Price:**
   - The script fetches real-time Bitcoin prices from the CoinDesk API, ensuring accuracy in calculations.

2. **Command-line Interface:**
   - Utilizes a simple command-line interface, allowing users to input the amount of Bitcoin for conversion.

3. **Error Handling:**
   - Incorporates error handling to gracefully manage issues during the API request, response parsing, and command-line argument processing.

## How to Use:

1. **Run the Script:**
   - Execute the script from the command line with the following command:
     ```bash
     python bitcoin_price_index.py <amount_of_bitcoin>
     ```
     Replace `<amount_of_bitcoin>` with the desired quantity of Bitcoin.

2. **View Results:**
   - The script will calculate and display the total value of the provided amount of Bitcoin in USD.

## Example

```bash
python bitcoin_price_index.py 0.5
```

This command will output the total value of 0.5 Bitcoin in USD based on the current exchange rate.

## Error Handling

The script includes error handling to ensure smooth execution. If an error occurs during the API request or response parsing, appropriate error messages will be displayed.

## Author

[Bassam Mejlaoui]
