from screeners.screener import (
    analyze_stock,
    evaluate_stock
)

from ai.prompts import (
    build_stock_analysis_prompt
)

from ai.gemini_client import (
    get_gemini_response
)


metrics = analyze_stock("AAPL")

metrics["recommendation"] = (
    evaluate_stock(metrics)
)

prompt = build_stock_analysis_prompt(
    metrics
)

response = get_gemini_response(
    prompt
)

print(response)