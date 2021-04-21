from random import random

import numpy as np
import matplotlib.pyplot as plt


def bed_bath_chart(df):
    df_bed_bath = df[['bedrooms', 'bathrooms', 'number_of_reviews']]

    # maps number of bathrooms to an index
    bathroom_dict = {0: 0, 0.5: 1, 1: 2, 1.5: 3, 2: 4, 2.5: 5, 3: 6, 3.5: 7, 4: 8, 4.5: 9, 5: 10, 5.5: 11, 6: 12}
    # contains total number of reviews for bed/bath combo
    bed_bath_matrix = np.zeros((6, 13))

    # sum total number of reviews for the different bed/bath combos
    for index in df_bed_bath.index:
        num_bed = int(df.at[index, 'bedrooms'])
        num_bath = df.at[index, 'bathrooms']
        reviews = df.at[index, 'number_of_reviews']
        bed_bath_matrix[num_bed][bathroom_dict[num_bath]] += reviews


    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot()
    ax.set_xlabel('Bathrooms')
    ax.set_ylabel('Bedrooms')
    ax.set_xticklabels([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])
    ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    ax.set_title('Total Reviews for Bed/Bath combinations')
    for i in range(len(bed_bath_matrix[0])):
        for j in range(len(bed_bath_matrix)):
            val = bed_bath_matrix[j,i]
            ax.text(i, j, str(val), va='center', ha='center')
    plt.imshow(bed_bath_matrix)

    return bed_bath_matrix
