# SALES DATA ANALYSIS & VISUALIZATION

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ------------------------------------------
# 1. CREATE SAMPLE SALES DATA
# ------------------------------------------

data = {
    "Date": [
        "2026-01-05", "2026-01-12", "2026-01-20",
        "2026-02-05", "2026-02-15", "2026-02-25",
        "2026-03-05", "2026-03-15", "2026-03-25",
        "2026-04-05", "2026-04-15", "2026-04-25",
        "2026-05-05", "2026-05-15", "2026-05-25",
        "2026-06-05", "2026-06-15", "2026-06-25"
    ],

    "Category": [
        "Almonds", "Cashews", "Raisins",
        "Almonds", "Cashews", "Raisins",
        "Almonds", "Cashews", "Raisins",
        "Almonds", "Cashews", "Raisins",
        "Almonds", "Cashews", "Raisins",
        "Almonds", "Cashews", "Raisins"
    ],

    "Sales": [
        12000, 15000, 9000,
        14000, 17000, 10000,
        16000, 18000, 11000,
        15000, 19000, 12000,
        18000, 21000, 13000,
        20000, 23000, 15000
    ]
}


# Convert dictionary into DataFrame
df = pd.DataFrame(data)


# ------------------------------------------
# 2. CONVERT DATE COLUMN
# ------------------------------------------

df["Date"] = pd.to_datetime(df["Date"])


# Display data
print("\n========== SALES DATA ==========")
print(df)


# ------------------------------------------
# 3. BASIC INFORMATION
# ------------------------------------------

print("\n========== DATA INFORMATION ==========")
print(df.info())


print("\n========== TOTAL SALES ==========")

total_sales = df["Sales"].sum()

print("Total Sales:", total_sales)


# ------------------------------------------
# 4. CATEGORY-WISE SALES
# ------------------------------------------

category_sales = df.groupby("Category")["Sales"].sum()

print("\n========== CATEGORY-WISE SALES ==========")
print(category_sales)


# ------------------------------------------
# 5. MONTHLY SALES
# ------------------------------------------

df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)


# ------------------------------------------
# 6. LINE CHART
# Sales over Time
# ------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    df["Date"],
    df["Sales"],
    marker="o",
    linewidth=2
)

plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.grid(True)

plt.tight_layout()

# Save chart as PNG
plt.savefig("sales_over_time.png", dpi=300)

plt.show()


# ------------------------------------------
# 7. MONTHLY SALES LINE CHART
# ------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.grid(True)

plt.tight_layout()

plt.savefig("monthly_sales.png", dpi=300)

plt.show()


# ------------------------------------------
# 8. BAR CHART
# Category Comparison
# ------------------------------------------

plt.figure(figsize=(8, 6))

plt.bar(
    category_sales.index,
    category_sales.values
)

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("category_sales_bar.png", dpi=300)

plt.show()


# ------------------------------------------
# 9. PIE CHART
# Category Sales Share
# ------------------------------------------

plt.figure(figsize=(8, 8))

plt.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales Share by Category")

plt.tight_layout()

plt.savefig("category_sales_pie.png", dpi=300)

plt.show()


# ------------------------------------------
# 10. FIND BEST SELLING CATEGORY
# ------------------------------------------

best_category = category_sales.idxmax()
best_category_sales = category_sales.max()

print("\n========== BEST CATEGORY ==========")

print("Best Selling Category:", best_category)
print("Sales:", best_category_sales)


# ------------------------------------------
# 11. FIND BEST SALES MONTH
# ------------------------------------------

best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()

print("\n========== BEST MONTH ==========")

print("Best Sales Month:", best_month)
print("Sales:", best_month_sales)


# ------------------------------------------
# 12. CREATE SHORT SUMMARY
# ------------------------------------------

summary = f"""
SALES ANALYSIS SUMMARY
======================

Total Sales: ₹{total_sales:,}

Best Selling Category:
{best_category}

Category Sales:
{category_sales.to_string()}

Best Sales Month:
{best_month}

Best Month Sales:
₹{best_month_sales:,}

Charts Created:
1. Sales Over Time
2. Monthly Sales
3. Category-wise Sales Bar Chart
4. Category Sales Share Pie Chart
"""


# Print summary
print("\n========== SUMMARY ==========")
print(summary)


# ------------------------------------------
# 13. SAVE SUMMARY TO TEXT FILE
# ------------------------------------------

with open("sales_summary.txt", "w") as file:
    file.write(summary)


print("\nProject completed successfully!")
print("Charts saved as PNG files.")
print("Summary saved as sales_summary.txt")