import requests
import itertools
import smtplib
from email.mime.text import MIMEText

# Your API Key and Email Credentials (Directly in Code)
OXR_API_KEY = "31ea34e7552c463682ae8478613d167b"
EMAIL_USER = "frodofellowship1@gmail.com"
EMAIL_PASS = "dbxd stlq evka potr"

# Currencies to Track
currencies = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "INR"]

# Function to Fetch Exchange Rates
def get_exchange_rates():
    url = f"https://open.er-api.com/v6/latest/USD?apikey={OXR_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data["rates"] if "rates" in data else {}

# Function to Detect Arbitrage Opportunities
def find_arbitrage_opportunities(rates):
    arbitrage_opportunities = []
    
    for trio in itertools.permutations(currencies, 3):
        base, mid, quote = trio
        
        if base in rates and mid in rates and quote in rates:
            rate1 = rates[mid] / rates[base]
            rate2 = rates[quote] / rates[mid]
            rate3 = rates[base] / rates[quote]
            
            profit = (rate1 * rate2 * rate3) - 1
            if profit > 0.001:  # Threshold to avoid tiny inefficiencies
                arbitrage_opportunities.append((trio, profit))
    
    return arbitrage_opportunities

# Function to Send Email Alert
def send_email(opportunities):
    if not opportunities:
        return
    
    message = "".join([f"{trio}: {profit:.4%}\n" for trio, profit in opportunities])
    msg = MIMEText(f"Arbitrage Opportunities Detected:\n{message}")
    msg["Subject"] = "Triangular Arbitrage Alert"
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_USER
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, EMAIL_USER, msg.as_string())

# Main Execution
def main():
    rates = get_exchange_rates()
    if not rates:
        print("Error fetching exchange rates!")
        return
    
    opportunities = find_arbitrage_opportunities(rates)
    if opportunities:
        send_email(opportunities)
        print("✅ Arbitrage alert sent!")
    else:
        print("No arbitrage opportunities found.")

if __name__ == "__main__":
    main()
