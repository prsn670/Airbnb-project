import read_data.read_data as rd
from clean_and_update.drop_data import drop_data
from clean_and_update.impute_data import impute_data
from clean_and_update.update_data import update
from analyze.predict_price import predict, calc_change
from analyze.bed_bath import bed_bath_chart

if __name__ == "__main__":
    # gather data
    df = rd.get_listing_data()
    old_df = df.copy(deep=True)

    # assess what data is available
    print(df)
    
    # clean and update data
    drop_data(df)
    impute_data(df)
    df = update(df)

    # show cleaned data
    print(df.head)
    
    # analyze correlation data when compared to price.
    corr_price = df.corr()['float_price'].sort_values()
    
    # display correlation of features to price
    # Assess which features are good candidates as a primary predictor in our model
    print(corr_price)

    # train/fit model to data and predict price of a place
    score = predict(df)
    
    # Calculate change in R2 based on feature and display
    # Assess which features contribute most to R2
    calc_change(df, score)
    # Show R2 score
    print("R2 score: " + str(score))

    # analyze number of beds, bathrooms, and total reviews
    # Visualize in Matrix format
    # assess which combination is most prominent
    new_df = bed_bath_chart(df)

    
