def generate_insight(token):
    if token.get('price_change_1h', 0) > 20:
        return "🚀 Strong momentum detected"

    if token.get('liquidity', 0) < 20000:
        return "⚠️ Low liquidity - high risk"

    if token.get('trade_count', 0) > 150:
        return "🐋 High trading activity (possible whale movement)"

    return "Stable"