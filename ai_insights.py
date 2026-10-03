import pandas as pd


def generate_insights():

    df = pd.read_csv("data/business_data.csv")

    # Total revenue
    total_revenue = df["Revenue"].sum()

    # Best-performing product
    product_revenue = df.groupby("Product")["Revenue"].sum()
    best_product = product_revenue.idxmax()

    # Best-performing region
    region_revenue = df.groupby("Region")["Revenue"].sum()
    best_region = region_revenue.idxmax()

    # Average rating
    average_rating = df["Customer Rating"].mean()

    print("\n===== AI BUSINESS INSIGHTS =====")

    print(f"Total business revenue is ₹{total_revenue:,.0f}.")
    print(f"The highest-revenue product is {best_product}.")
    print(f"The strongest-performing region is {best_region}.")
    print(f"Average customer rating is {average_rating:.2f}/5.")

    print("\nBusiness Recommendation:")
    print(
        f"Focus marketing and inventory planning on {best_product} "
        f"and investigate opportunities to expand sales in {best_region}."
    )


if __name__ == "__main__":
    generate_insights()
