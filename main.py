# Local imports
import multiprocessing as mp

# Project modules
import gridtrader


def main():
    """Top level main execution function."""
    stock_trader = gridtrader.GridTrader(
        symbol = 'AAPL',
        trading_range = (242, 262),
        grids_amount = 10,
        quantity = 26
    )

    # btc_trader = gridtrader.GridTrader(
    #     symbol = 'BTCUSD',
    #     trading_range = (22930, 23000),
    #     grids_amount = 51,
    #     account_allocation = 0.1
    # )

    # easy_deploy = gridtrader.GridTrader.from_defaults(
    #     symbol = 'BTCUSD',
    #     grid_height = 15,
    #     grids_amount = 16,
    #     allocation = 0.5
    # )

    # Start the manual GridTraders simultaneously
    mp.Process(target=stock_trader.deploy).start()
    # mp.Process(target=btc_trader.deploy).start()
    # mp.Process(target=easy_deploy.deploy).start()


if __name__ == "__main__":
    main()
