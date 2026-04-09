import pandas as pd

df = pd.DataFrame({
    "city": ["Kathmandu", "Kathmandu", "Pokhara", "Pokhara"],
    "product": ["A", "B", "A", "B"],
    "sales": [100, 200, 150, 300]
})


print(df)

print(df.pivot(index="city", columns="product", values="sales"))

