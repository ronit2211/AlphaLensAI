
from screeners.screener import (
    analyze_stock,
    evaluate_stock
)

result = analyze_stock("AAPL")

signal = evaluate_stock(result)

for key, value in result.items():
    print(key, ":", value)

print("\nSignal:", signal)