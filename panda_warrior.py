import numpy as np
import pandas as pd

cars = {'Brand': ['Honda', 'Toyota', 'Ford'],
        'Price': [22000, 25000, 27000]}

cars_df = pd.DataFrame(cars, columns=['Brand', 'Price'], index=[
                       'Car 1', 'Car 2', 'Car 3'])

# ADDING NEW COLOUMN TO DF ALWAYS SHOW IN THE END
year = [2010, 2011, 2008]
cars_df['Year'] = year

# ADD COLOUMN USING INSERT COLOUMN
cars_df.insert(1, 'Model', ['Civic', 'Prius', 'Focus'], True)

# ADD DATA NEW ROW
#new_car_1 = {'Brand': 'Hyundai', 'Model': 'Avante',
             #'Price': 20000, 'Year': 2010}

#cars_df = cars_df.append(new_car_1, ignore_index=True)

# ADD DATA NEW ROW USING LOC
cars_df.loc['Car 4'] = ['Hyundai', 'Avante', 20000, 2010]

# UPDATE DATA ROW EXISTS
cars_df.loc['Car 3'] = ['Suzuki', 'Swift', 26000, 2013]

# ADD DISCOUNT 10%
cars_df['Discount'] = 0.1*cars_df['Price']

# PRICE AFTER DISCOUNT
cars_df['Discount Price'] = cars_df['Price']-cars_df['Discount']

# ADD PRICE AFTER USING INSERT COLOUMN
#cars_df.insert(3, 'Discount Price', cars_df['Price']-cars_df['Discount'], True)


print(cars_df)
