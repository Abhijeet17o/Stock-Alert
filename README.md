# Stock Insights Generator

This Python script retrieves stock data and news sentiment for a specified stock using the Alpha Vantage API. It fetches the latest stock data, including the percentage change in stock price, and retrieves the top news headlines related to the specified stock, along with a brief summary of each news article. The script then generates a text file containing this information.

## Getting Started

Before running the script, you'll need to obtain an API key from Alpha Vantage and replace `"YOUR API KEY FOR THE ENDPOINT"` with your actual API key.

### Usage

1. Modify the `STOCK` variable in the script to specify the stock symbol you want to analyze.
   - Note: The name of the stock should be in listed in Nasdaq Stock Exchange
   - For example: 'AAPL', 'MSFT', 'TSLA'
2. Replace `"YOUR API KEY FOR THE ENDPOINT"` with your actual Alpha Vantage API key.
3. Run the script:

   ```bash
   python stock_analyzer.py
   ```

5. After execution, a file named `final.txt` will be generated in the same directory, containing the stock information and news sentiment analysis.

## Features

- Retrieves the percentage change in stock price for the specified stock.
- Fetches the top news headlines related to the specified stock and provides a brief summary for each news article.
- Displays a positive or negative indicator (🔺 or 🔻) based on the percentage change in stock price.
- Writes the stock information and news sentiment analysis to a text file for easy reference.

## Project Structure

- `stock_analyzer.py`: Main Python script containing the implementation of the stock news and sentiment analyzer.
- `final.txt`: Text file containing the generated stock information and news sentiment analysis.
- `README.md`: Markdown file containing information about the script and how to use it.

## Contributing

Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, feel free to open an issue or create a pull request.

## Contact

For any inquiries or support, please contact [abhijeetsapar17@gmail.com].
