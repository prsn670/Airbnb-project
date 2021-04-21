def impute_data(df):
    values = {'host_is_superhost': 'f',  'host_has_profile_pic': 'f', 'host_verifications': '[]',
              'host_identity_verified': 'f', 'amenities': {}, 'security_deposit': '$0.00', 'cleaning_fee': '$0.00',
              'guests_included': 0, 'extra_people': '$0.00', 'requires_license': 'f',
              'require_guest_profile_picture': 'f', 'require_guest_phone_verification': 'f'
              }

    # fill in null values
    df.fillna(value=values, inplace=True)