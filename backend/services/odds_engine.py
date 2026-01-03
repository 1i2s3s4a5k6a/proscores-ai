def validate_arbitrage(odds: list):
    if len(odds) < 3:
        return None
    margin = sum(1/o for o in odds)
    if margin >= 1:
        return None
    return round((1 - margin) * 100, 2)
