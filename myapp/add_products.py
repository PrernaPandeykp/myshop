import pandas as pd
from .models import Product

df = pd.read_csv("D:\django start\mysite\Fashion_Dataset.csv")


def add_product():
    count = 0
    for _, row in df.iterrows():
        new = Product(
            id=row["id"],
            gender=row["gender"],
            master_category=row["masterCategory"],
            sub_category=row["subCategory"],
            article_type=row["articleType"],
            base_colour=row["baseColour"],
            season=row["season"],
            year=row["year"],
            usage=row["usage"],
            product_name=row["productDisplayName"],
            image_url=row["image_url"],
            price=row["price"],
            discount_price=row["discountedPrice"],
            brand_name=row["brandName"],
            age_group=row["ageGroup"],
        )
        new.save()
        count += 1
        if count > 1000:
            break
