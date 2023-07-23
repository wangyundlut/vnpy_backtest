


from vnpy.trader.optimize import OptimizationSetting
from vnpy_ctastrategy.backtesting import BacktestingEngine
from vnpy_ctastrategy.strategies.double_ma_strategy import (
    DoubleMaStrategy,
)
from datetime import datetime

engine = BacktestingEngine()
engine.set_parameters(
    vt_symbol="1INCHUSDT.BINANCE",
    interval="1m",
    start=datetime(2023, 1, 1),
    end=datetime(2023, 1, 5),
    rate=0.3/10000,
    slippage=0.2,
    size=300,
    pricetick=0.2,
    capital=1_000_000,
)
engine.add_strategy(DoubleMaStrategy, {})

engine.load_data()
engine.run_backtesting()
df = engine.calculate_result()
engine.calculate_statistics()
# engine.show_chart()
engine.save_echarts()

setting = OptimizationSetting()
setting.set_target("sharpe_ratio")
setting.add_parameter("atr_length", 25, 27, 1)
setting.add_parameter("atr_ma_length", 10, 30, 10)

engine.run_ga_optimization(setting)


