import numpy as np
import pandas as pd
import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))  # This is your Project Root


def get_listing_data():
    boston_listings_df = pd.read_csv(os.path.abspath(ROOT_DIR + "/BostonData/listings.csv"))
    # seattle_listings_df = pd.read_csv(os.path.abspath(ROOT_DIR + "/SeattleData/listings.csv"))
    return boston_listings_df

def get_seattle_data():

    seattle_cal_df = pd.read_csv(os.path.abspath(ROOT_DIR + "/SeattleData/calendar.csv"))
    seattle_listings_df = pd.read_csv(os.path.abspath(ROOT_DIR + "/SeattleData/listings.csv"))
    seattle_reviews_df = pd.read_csv(os.path.abspath(ROOT_DIR + "/SeattleData/reviews.csv"))
    return seattle_cal_df, seattle_listings_df, seattle_reviews_df


def get_boston_data():
    boston_cal_df = pd.read_csv(os.path.abspath(ROOT_DIR + "/BostonData/calendar.csv"))
    boston_listings_df = pd.read_csv(os.path.abspath(ROOT_DIR + "/BostonData/listings.csv"))
    boston_reviews_df = pd.read_csv(os.path.abspath(ROOT_DIR + "/BostonData/reviews.csv"))
    return boston_cal_df, boston_listings_df, boston_reviews_df

def get_boston_review_data():
    boston_reviews_df = pd.read_csv(os.path.abspath(ROOT_DIR + "/BostonData/reviews.csv"))
    return boston_reviews_df


# Used for testing
if __name__ == "__main__":
    # print("root dir: " + ROOT_DIR)
    seattle_cal_df, seattle_listings_df, seattle_reviews_df = get_seattle_data()
    boston_cal_df, boston_listings_df, boston_reviews_df = get_boston_data()

    # review = list(seattle_reviews_df['listing_id'])
    # review_list = seattle_reviews_df.loc[seattle_reviews_df['listing_id'] == 241032.00000]
    # print(type(review_list))
    # print(review_list)
    # 241032.00000
    # print(241032.00000 in review)
    # note that in seattle_listings_df id column corresponds to the listing_id columns in the other two datasets
    # calendar_val_count = boston_cal_df["listing_id"].value_counts()
    # calendar_counts = boston_cal_df["listing_id"].count()
    # non_avail = boston_cal_df[boston_cal_df['available'] == 'f'].dropna(subset=['price'])
    # print(calendar_val_count)
    # column_list_cal = []
    # column_list_listings = []
    # column_list_reviews = []
    # column_list_cal.extend(boston_cal_df.columns.tolist())
    # column_list_listings.extend(boston_listings_df.columns.tolist())
    # column_list_reviews.extend(boston_reviews_df.columns.tolist())
    #
    # # 7735100.00000
    # listing_cal_avail = boston_cal_df[boston_cal_df['listing_id'] == 7735100.00000]