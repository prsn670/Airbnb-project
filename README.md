# Airbnb-project
Uses Airbnb data from Kaggle to predict pricing in Boston.

## Installation
There shouldn't be any installation needed. Code was written using Python 3.8 and Anaconda. Code can also be run using Jupyter Notebook 

## Project Motivation
Using the Airbnb data for Boston to try and create a model that will predict the price of a listing. The project also attempted to identify the main features used in predicting price.

## File Descriptions
  1. main.py and main.ipynb - Runs the program
  2. BostonData and SeattleData files - contain the csv files with data
  3. read_data files contans methods that retrieve data from Boston and SeattleData. Since only Boston is currently being used, corresponding Seattle methods may not be there.
  4. clean and update files - contains methods that drop, change, or otherwise change our dataframes before fitting our model
  5. plot - contains file that creates a bar chart based on differences of R2 values from different models.
  6. analyze files - predicts price, and collects R2 data to sent to plot. Also charts total number of reviews based on bedroom and bathroom number

## Interacting With Project
There shouldn't be anything particularly complicated. If using pycharm, you can simply run the project from main. Using notbook, just run the cells in order

## Licensing, Authors, Acknowledgements
[GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html)
Data provided by Airbnb and Kaggle - [Boston](https://www.kaggle.com/airbnb/boston), [Seattle](https://www.kaggle.com/airbnb/seattle)
Medium article based on my findings [here](https://parshad-anil.medium.com/airbnb-what-sells-ac328d7c2801)
