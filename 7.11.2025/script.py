user = float(input("Enter an amount in Euros:"))
eurorate = 1
euro_to_usd = 2.05

print(f"you entered: €{user:.2f}")
print(f"Exchange rate (Euro to USD): {euro_to_usd}")

usd = user * euro_to_usd
print(f"Converted amount in USD: ${usd:.2f}")


euro_to_jpy = 140.25
jpy = user * euro_to_jpy
print(f"Converted amount in JPY: ¥{jpy:.2f}")
print("euro rate :" f"{eurorate}")


