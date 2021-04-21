import read_data.read_data as rd
from clean_and_update.impute_data import impute_data


# remove unneeded columns
def drop_data(df):
    # drop columns where all values are null/nan
    df.dropna(how='all')

    drop_null = ['price', 'host_response_time', 'host_response_rate', 'host_acceptance_rate', 'property_type',
                 'room_type', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'bed_type', 'reviews_per_month',
                 'review_scores_value', 'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness',
                 'review_scores_checkin', 'review_scores_communication', 'review_scores_location', 'zipcode',
                 'host_since', 'host_neighbourhood', 'host_listings_count',
                 'host_total_listings_count', 'calculated_host_listings_count', 'minimum_nights',
                 'maximum_nights', 'availability_30', 'availability_60', 'availability_90', 'availability_365',
                 'number_of_reviews', 'instant_bookable', 'cancellation_policy']

    # drop rows where data is null
    for subset in drop_null:
        try:
            df.dropna(subset=[subset], inplace=True)
        except Exception:
            pass

    unneeded_columns = ['id', 'host_id', 'listing_url', 'scrape_id', 'last_scraped', 'name', 'summary', 'space',
                        'description', 'experiences_offered', 'neighborhood_overview', 'notes', 'transit',
                        'access', 'interaction', 'house_rules', 'thumbnail_url', 'medium_url',
                        'picture_url', 'xl_picture_url', 'host_url', 'host_name', 'host_about',
                        'host_thumbnail_url', 'host_picture_url', 'street', 'neighbourhood',
                        'neighbourhood_cleansed', 'neighbourhood_group_cleansed', 'city', 'state',
                        'market', 'smart_location', 'country_code', 'country', 'latitude', 'longitude',
                        'is_location_exact', 'calendar_updated', 'calendar_last_scraped',
                        'first_review', 'last_review', 'jurisdiction_names', 'weekly_price',
                        'monthly_price', 'has_availability', 'license', 'square_feet', 'neighbourhood', 'host_location']
    # drop unneeded columns
    for column in unneeded_columns:
        try:
            df.drop(columns=[column], inplace=True)
        except Exception:
            pass