import read_data.read_data as rd
from clean_and_update.drop_data import drop_data
from clean_and_update.impute_data import impute_data
from clean_and_update.update_data import update
from analyze.predict_price import predict, calc_change
from analyze.bed_bath import bed_bath_chart

if __name__ == "__main__":
    # get data
    df = rd.get_listing_data()

    # clean and update data
    drop_data(df)
    impute_data(df)
    df = update(df)

    # train, analyze, display data
    corr_price = df.corr()['float_price'].sort_values()
    # show correlation of features to price
    print(corr_price)

    # train and predict price of a place
    score = predict(df)
    calc_change(df, score)

    # analyze number of beds, bathrooms, and total reviews
    new_df = bed_bath_chart(df)

    print("R2 score: " + str(score))
