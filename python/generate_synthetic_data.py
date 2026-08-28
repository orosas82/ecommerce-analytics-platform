import csv
import random
from datetime import date, timedelta
from pathlib import Path

RANDOM_SEED = 42
DAYS = 180
OUTPUT_DIR = Path(__file__).resolve().parents[1] / 'data' / 'synthetic'
CHANNELS = {
    'google_paid_search': (900, 2200, 0.055),
    'meta_paid_social': (700, 1800, 0.035),
    'email': (120, 350, 0.025),
    'organic': (0, 0, 0.0),
}

def daily_dates(days):
    end = date.today() - timedelta(days=1)
    return [end - timedelta(days=offset) for offset in range(days - 1, -1, -1)]

def write_marketing_spend(dates):
    rows = []
    for day in dates:
        for channel, (low, high, _) in CHANNELS.items():
            weekday_factor = 0.78 if day.weekday() >= 5 else 1.0
            spend = round(random.uniform(low, high) * weekday_factor, 2)
            rows.append([day.isoformat(), channel, spend])
    with (OUTPUT_DIR / 'marketing_spend.csv').open('w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['date', 'channel', 'spend_usd'])
        writer.writerows(rows)

def write_web_sessions(dates):
    rows = []
    for day in dates:
        for channel, (_, _, base_rate) in CHANNELS.items():
            sessions = random.randint(900, 3800) if channel != 'organic' else random.randint(2500, 7000)
            conversion_rate = max(0.006, base_rate + random.uniform(-0.008, 0.012))
            transactions = max(1, round(sessions * conversion_rate))
            revenue = round(transactions * random.uniform(58, 112), 2)
            rows.append([day.isoformat(), channel, sessions, transactions, revenue])
    with (OUTPUT_DIR / 'web_sessions.csv').open('w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['date', 'channel', 'sessions', 'transactions', 'revenue_usd'])
        writer.writerows(rows)

def main():
    random.seed(RANDOM_SEED)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    dates = daily_dates(DAYS)
    write_marketing_spend(dates)
    write_web_sessions(dates)
    print(f'Wrote synthetic files to {OUTPUT_DIR}')

if __name__ == '__main__':
    main()
