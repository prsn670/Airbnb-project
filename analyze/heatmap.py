import seaborn as sns

# not used, the map was too messy. Needs cleanup before it can be useful.
def heatmap(df):
    drop_col = ['host_neighbourhood', 'host_has_profile_pic', 'property_type', 'requires_license',
                           'instant_bookable']
    df.drop(columns=drop_col)
    sns.set(font_scale=0.5)
    # Often a useful plot is a correlation matrix - this can tell you which variables are related to one another.
    sns.heatmap(df.corr(), annot=True, fmt=".2f")
    return df.corr()