import pandas as pd


start_date = '2023-01-01'
end_date = '2023-02-01'



def process_data(file_path):
    df = pd.read_csv(file_path)

    df = df.loc[(df['timestamp'] >= start_date) & (df['timestamp'] <= end_date), :]
    df['timestamp'] = df.apply(lambda x: str(x['timestamp'])[0:-5], axis=1)
    # df['timestamp'] = df.apply(lambda x: x['timestamp'].replace(' +0800', ' '), axis=1)
    df = df.reset_index(drop=True)

    df.to_csv(file_path, index=False)

for file_path in [
    # '/Repositories/vnpy_backtest/data/1m/1INCHUSDT.csv', 
    '/Repositories/vnpy_backtest/data/1m/AAVEUSDT.csv']:
    process_data(file_path)
    print(f"processed {file_path}")

def process_data2(file_path):
    df = pd.read_csv(file_path)
    df['timestamp'] = df.apply(lambda x: str(x['timestamp'])[0:-1], axis=1)
    # df['timestamp'] = df.apply(lambda x: x['timestamp'].replace('.000000 +0800', ' '), axis=1)
    df = df.reset_index(drop=True)

    df.to_csv(file_path, index=False)

for file_path in [
    '/Repositories/vnpy_backtest/data/d/1INCHUSDT.csv', 
    '/Repositories/vnpy_backtest/data/d/AAVEUSDT.csv']:
    process_data2(file_path)
    print(f"processed {file_path}")




