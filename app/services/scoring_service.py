def calculate_score(token):
    score = 0

    # 🔥 mapping field API (tidak ubah logika)
    volume_1h = token.get('volume1h', 0)
    volume_24h = token.get('volume24h', 1)  # hindari division by zero
    price_change = token.get('priceChange1h', 0)
    liquidity = token.get('liquidityUsd', 0)
    trade_count = token.get('txns', 0)

    # volume growth
    if volume_1h > volume_24h * 0.3:
        score += 30
        
    # price momentum
    if price_change > 10:
        score += 25
        
    # liquidity
    if liquidity > 50000:
        score += 20
        
    # whale activity (dummy logic)
    if trade_count > 100:
        score += 25
        
    return score