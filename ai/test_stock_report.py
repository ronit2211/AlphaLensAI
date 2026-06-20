from screeners.screener import analyze_stock
from screeners.screener import evaluate_stock

from ai.stock_report import generate_stock_report

metrics = analyze_stock("AAPL")

metrics["recommendation"] = evaluate_stock(metrics)

report = generate_stock_report(metrics)

print(report)