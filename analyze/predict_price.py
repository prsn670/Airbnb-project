from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

from plot.delta_bar_chart import plot_bar_chart

# after including all features, these features seemed to significantly impact the regression model negatively.
# float_price was included in the list only because this is what we model will be predicting
drop_col = ['host_has_profile_pic', 'property_type', 'requires_license', 'instant_bookable',
            'float_price']


def predict(df):
    return linear_regression(df)


def linear_regression(df):
    boston_listings_df = df

    X_boston = boston_listings_df.drop(columns=drop_col)
    y_boston = boston_listings_df['float_price']
    # print(X_boston.columns)

    X_train_boston, X_test_boston, y_train_boston, y_test_boston = train_test_split(X_boston, y_boston, test_size=.30,
                                                                                    random_state=42)

    lm_model_boston = LinearRegression(normalize=True)

    lm_model_boston.fit(X_train_boston, y_train_boston)

    boston_price_prediction = lm_model_boston.predict(X_test_boston)

    boston_score = r2_score(y_test_boston, boston_price_prediction)

    return boston_score


# See how much each variable changes our original r2 score
def calc_change(df, orig_score):
    variables = ['float_extra_people', 'float_cleaning_fee', 'float_security_deposit',
                 'float_host_acceptance_rate', 'float_host_response_rate',
                 'number_of_amenities', 'number_of_host_verifications', 'host_days',
                 'host_listings_count', 'host_total_listings_count', 'accommodates',
                 'bathrooms', 'bedrooms', 'beds', 'guests_included', 'minimum_nights',
                 'maximum_nights', 'availability_30', 'availability_60',
                 'availability_90', 'availability_365', 'number_of_reviews',
                 'review_scores_rating', 'review_scores_accuracy',
                 'review_scores_cleanliness', 'review_scores_checkin',
                 'review_scores_communication', 'review_scores_location',
                 'review_scores_value', 'calculated_host_listings_count',
                 'reviews_per_month', 'room_type_Private room', 'room_type_Shared room',
                 'host_is_superhost_t', 'host_response_time_within a day',
                 'host_response_time_within a few hours',
                 'host_response_time_within an hour', 'host_identity_verified_t',
                 'bed_type_Couch', 'bed_type_Futon', 'bed_type_Pull-out Sofa',
                 'bed_type_Real Bed', 'cancellation_policy_moderate',
                 'cancellation_policy_strict', 'cancellation_policy_super_strict_30',
                 'require_guest_phone_verification_t', 'require_guest_profile_picture_t',
                 'zipcode_02108 02111', 'zipcode_02109', 'zipcode_02110',
                 'zipcode_02111', 'zipcode_02113', 'zipcode_02114', 'zipcode_02115',
                 'zipcode_02116', 'zipcode_02118', 'zipcode_02119', 'zipcode_02120',
                 'zipcode_02121', 'zipcode_02122', 'zipcode_02124', 'zipcode_02125',
                 'zipcode_02126', 'zipcode_02127', 'zipcode_02128', 'zipcode_02129',
                 'zipcode_02130', 'zipcode_02131', 'zipcode_02132', 'zipcode_02134',
                 'zipcode_02134-1704', 'zipcode_02135', 'zipcode_02136', 'zipcode_02139',
                 'zipcode_02141', 'zipcode_02142', 'zipcode_02143', 'zipcode_02145',
                 'zipcode_02163', 'zipcode_02210', 'zipcode_02215', 'zipcode_02445',
                 'zipcode_02446', 'zipcode_02467']

    delta_list = []
    for var in variables:
        drop_col.append(var)
        new_score = linear_regression(df)
        delta = new_score - orig_score
        delta_list.append(delta)
        drop_col.remove(var)

    plot_bar_chart(variables, delta_list)
