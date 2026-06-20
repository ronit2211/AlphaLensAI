from ai.gemini_client import get_gemini_response


def generate_portfolio_report(
    portfolio_return,
    portfolio_volatility,
    sharpe_ratio
):

    prompt = f"""
You are a professional portfolio manager.

Analyze the following portfolio metrics.

Portfolio Return:
{portfolio_return:.4f}

Portfolio Volatility:
{portfolio_volatility:.4f}

Sharpe Ratio:
{sharpe_ratio:.4f}

Provide:

1. Performance Analysis
2. Risk Analysis
3. Risk-Adjusted Return Analysis
4. Portfolio Outlook

Keep the explanation concise and professional.
"""

    return get_gemini_response(prompt)