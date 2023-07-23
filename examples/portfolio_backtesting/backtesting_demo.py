from datetime import datetime
from importlib import reload

import vnpy_portfoliostrategy
reload(vnpy_portfoliostrategy)

from vnpy_portfoliostrategy import BacktestingEngine
from vnpy.trader.constant import Interval
from vnpy.trader.optimize import OptimizationSetting

# import vnpy_portfoliostrategy.strategies.pair_trading_strategy as stg
# reload(stg)
# from vnpy_portfoliostrategy.strategies.pair_trading_strategy import PairTradingStrategy

import vnpy_portfoliostrategy.strategies.portfolio_boll_channel_strategy as stg
reload(stg)
from vnpy_portfoliostrategy.strategies.portfolio_boll_channel_strategy import PortfolioBollChannelStrategy

engine = BacktestingEngine()
engine.set_parameters(
    vt_symbols=["1INCHUSDT.BINANCE", "AAVEUSDT.BINANCE"],
    interval=Interval.MINUTE,
    start=datetime(2023, 1, 1),
    end=datetime(2023, 1, 30),
    rates={
        "1INCHUSDT.BINANCE": 0/10000,
        "AAVEUSDT.BINANCE": 0/10000
    },
    slippages={
        "1INCHUSDT.BINANCE": 0,
        "AAVEUSDT.BINANCE": 0
    },
    sizes={
        "1INCHUSDT.BINANCE": 10,
        "AAVEUSDT.BINANCE": 10
    },
    priceticks={
        "1INCHUSDT.BINANCE": 0.001,
        "AAVEUSDT.BINANCE": 0.001
    },
    capital=1_000_000,
)

setting = {
    "boll_window": 20,
    "boll_dev": 1,
}
engine.add_strategy(PortfolioBollChannelStrategy, setting)


engine.load_data()
engine.run_backtesting()
df = engine.calculate_result()
engine.calculate_statistics()
# engine.show_chart()
engine.save_echarts()


setting = OptimizationSetting()
setting.set_target("sharpe_ratio")
setting.add_parameter("boll_window", 10, 30, 1)
setting.add_parameter("boll_dev", 1, 3, 1)

engine.run_ga_optimization(setting)

print('done')

