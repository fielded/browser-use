def estimate_cost_from_tokens(total_tokens: int, cost_per_1k_tokens: float = 0.03) -> float:
    """
    Estimate the cost based on token usage.

    Args:
        total_tokens (int): Number of tokens used.
        cost_per_1k_tokens (float): Cost per 1000 tokens (default $0.03).

    Returns:
        float: Estimated cost in USD.
    """
    return round((total_tokens / 1000) * cost_per_1k_tokens, 4)


