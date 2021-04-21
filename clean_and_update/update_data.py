import datetime
import pandas as pd
import read_data.read_data as rd


# calculates the number of days the the person has been a host and replaces data under host_since with host_days
def update_host_since(df):
    column = 'host_since'
    # data_collection_data based on metadata info from source of download.
    data_collection_date = datetime.date(2016, 11, 16)
    for index in df.index:
        date_time_str = df.at[index, column]
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')
        date_difference = data_collection_date - date_time_obj.date()
        days = int(date_difference.days)
        df.at[index, column] = days
    df.rename(columns={column: 'host_days'}, inplace=True)

# updates data in list format to instead show the total number. Replaces with new column names
def update_array_to_number(df):
    values = ['host_verifications', 'amenities']
    prefix = 'number_of_'
    for value in values:
        length_list = []
        for index in df.index:
            to_list = df.at[index, value].strip("[]{}").replace("'", "").replace("\"", "").split(",")
            length_list.append(len(to_list))
        df.drop(value, axis=1, inplace=True)
        df.insert(0, prefix+value, length_list, True)

# convert str to float
def convert_string_to_float(df):
    cols = ['host_response_rate', 'host_acceptance_rate', 'price', 'security_deposit', 'cleaning_fee', 'extra_people']
    prefix = 'float_'
    for col in cols:
        float_list = []
        for index in df.index:
            new_string = df.at[index, col].strip("$%").replace(',', '')
            float_list.append(float(new_string))
        df.drop(col, axis=1, inplace=True)
        df.insert(0, prefix+col, float_list, True)



# Create dummies for categorical data
def create_dummy(df):
    # note that using dummy variable for zip code is quick an easy, but predicting based on new zip won't be possible
    cat_cols = ['room_type', 'host_is_superhost', 'host_response_time', 'host_identity_verified', 'bed_type',
                'cancellation_policy', 'require_guest_phone_verification', 'require_guest_profile_picture', 'zipcode']
    for col in cat_cols:
        try:
            # for each categorical variable add dummy var, drop original column
            df = pd.concat([df.drop(col, axis=1),
                            pd.get_dummies(df[col], prefix=col, prefix_sep='_', drop_first=True)],
                           axis=1)
        except:
            continue
    return df

def update(df):
    update_host_since(df)
    update_array_to_number(df)
    convert_string_to_float(df)
    return create_dummy(df)
