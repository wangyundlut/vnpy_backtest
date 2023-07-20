


from vnpy.trader.optimize import OptimizationSetting
from vnpy_ctastrategy.backtesting import BacktestingEngine
from vnpy_ctastrategy.strategies.atr_rsi_strategy import (
    AtrRsiStrategy,
)
from datetime import datetime

engine = BacktestingEngine()
engine.set_parameters(
    vt_symbol="1INCHUSDT.BINANCE",
    interval="d",
    start=datetime(2020, 12, 25),
    end=datetime(2023, 6, 20),
    rate=0.3/10000,
    slippage=0.2,
    size=300,
    pricetick=0.2,
    capital=1_000_000,
)
engine.add_strategy(AtrRsiStrategy, {})

engine.load_data()
engine.run_backtesting()
df = engine.calculate_result()
engine.calculate_statistics()
engine.show_chart()

setting = OptimizationSetting()
setting.set_target("sharpe_ratio")
setting.add_parameter("atr_length", 25, 27, 1)
setting.add_parameter("atr_ma_length", 10, 30, 10)

engine.run_ga_optimization(setting)


