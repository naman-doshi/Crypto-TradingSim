# Crypto-TradingSim
Python Cryptocurrency Trading Simulator for all cryptocurrencies currently on Binance. A Binance API key is required.

Adjust the 'capital' variable to change your starting capital. After running the program, the commands available to use are:
- long BTCUSDT 
- short BTCUSDT
- check BTCUSDT (to check the PnL of a position)
- close BTCUSDT (to close said position)

where BTCUSDT is a placeholder for any trading pair currently on Binance (not Binance.US). After entering in a command, you may be asked some questions such as 'Leverage?' and 'Percentage of Capital?'. Reply to these with integers, such as 20 for 'leverage' and 100 for 'percentage of capital'.

There is a section that I commented out, but feel free to enable it if you need the liquidation feature.
