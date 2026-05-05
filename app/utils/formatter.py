def classify_score(score):
    if score >= 80:
        return "🔥 HIGH ALPHA"
    elif score >= 50:
        return "⚡ MEDIUM"
    else:
        return "🧊 LOW"


def print_token_report(name, address, price, score, category, insight, security):
    print(f"\n🔥 ALPHA REPORT")
    print(f"Token   : {name}")
    print(f"Address : {address}")
    print(f"Price   : ${price:.6f}")
    print(f"Score   : {score} ({category})")
    print(f"Insight : {insight}")

    if security:
        is_mintable = "Yes" if security.get('is_mintable') else "No"
        owner = security.get('owner', 'Unknown')
        print(f"Mintable: {is_mintable}")
        print(f"Owner   : {owner[:10]}...")