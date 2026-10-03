import pandas as pd


def analyze_business_data():

    # Load business data
    df = pd.read_csv("data/business_data.csv")

    # Basic analysis
    total_revenue = df["Revenue"].sum()
    total_units = df["Units Sold"].sum()
    average_rating = df["Customer Rating"].mean()

    # Product performance
    product_revenue = (
        df.groupby("Product")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    # Regional performance
    region_revenue = (
        df.groupby("Region")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n===== AI-POWERED BUSINESS INTELLIGENCE =====")

    print(f"\nTotal Revenue: ₹{total_revenue:,.0f}")
    print(f"Total Units Sold: {total_units:,}")
    print(f"Average Customer Rating: {average_rating:.2f}")

    print("\nRevenue by Product:")
    print(product_revenue)

    print("\nRevenue by Region:")
    print(region_revenue)


if __name__ == "__main__":
    analyze_business_data()
