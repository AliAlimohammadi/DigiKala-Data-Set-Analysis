#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import operator
import numpy as np


# In[18]:


df2 = pd.read_excel('C:\\Users\\Ali\\Desktop\\project\\part1\\codes\\data\\2-p9vcb5bb.xlsx')
df3 = pd.read_csv('C:\\Users\\Ali\\Desktop\\project\\part1\\codes\\data\\3-p5s3708k.csv')
df5 = pd.read_excel('C:\\Users\\Ali\\Desktop\\project\\part1\\codes\\data\\5-awte8wbd.xlsx')


# In[19]:


df3['product_id'] = df3['ID_Item']
df5['product_id'] = df5['id']


# In[20]:


df2_df3 = pd.merge(df2, df3, how='inner', left_on='product_id', right_on='ID_Item')
df2_df5 = pd.merge(df2, df5, on='product_id')
df3_df5 = pd.merge(df3, df5, on='product_id')
df2_df5.fillna(0)
df3_df5.fillna(0)


# In[21]:


categories = df2_df5['category_title_fa'].unique()

dict = {}
for i in range(len(categories)):
    dict[categories[i]] = len(df2_df5[df2_df5['category_title_fa'] == categories[i]])

sorted_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)


# In[22]:


comments = []

for i in range(len(df2_df5['product_id'])):
    if df2_df5['category_title_fa'][i] == sorted_dict[0][0]:
        comments.append(df2_df5['comment'][i])

all_words = []
for i in range(len(comments)):
    words = comments[i].split(' ')
    for j in range(len(words)):
        all_words.append(words[j])


# In[23]:


import collections


counter = collections.Counter(all_words)
sorted_counter = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)

top_words = []
for i in range(len(sorted_counter)):
    if sorted_counter[i][1] > 20 and sorted_counter[i][1] < 50:
        top_words.append(sorted_counter[i])

figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
plt.bar([row[0] for row in top_words], [row[1] for row in top_words])
plt.show()


# In[24]:


products = df2_df3['product_id_x'].unique()
numbers_sold = []
for pid in products:
    numbers_sold.append(len(df2_df3[df2_df3['product_id_x'] == pid]))

top_sellers = sorted(zip(numbers_sold, products), reverse=True)


# In[25]:


products = df2_df5['product_id'].unique()
dict = {}
for i in range(len(products)):
    dict[products[i]] = len(df2_df5[df2_df5['product_id'] == products[i]])

most_comments = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

product_id  = []
popularity = []
for i in range(len(top_sellers)):
    for j in range(len(most_comments)):
        if top_sellers[i][1] == most_comments[j][0]:
            product_id.append(top_sellers[i][1])
            popularity.append((top_sellers[i][0] + most_comments[j][1]) / 2)
            
most_popular = sorted(zip(popularity, product_id), reverse=True)[:10]

figure(num=None, figsize=(12, 6), dpi=100, facecolor='w', edgecolor='k')
plt.bar([str(row[1]) for row in most_popular], [row[0] for row in most_popular], color='#ce275f')
plt.xlabel('Product ID')
plt.ylabel('Popularity Factor')
plt.show()


# In[26]:


yalda2015_total_sale = 0
yalda2015_numbers_sold = 0
yalda2016_total_sale = 0
yalda2016_numbers_sold = 0
yalda2017_total_sale = 0
yalda2017_numbers_sold = 0

year2015_numbers_sold = 0
year2015_total_sale = 0
year2016_numbers_sold = 0
year2016_total_sale = 0
year2017_numbers_sold = 0
year2017_total_sale = 0

order_date = df3['DateTime_CartFinalize']

for i in range(len(order_date)):
    if order_date[i].__contains__('2015-12-21') or order_date[i].__contains__('2015-12-20') or order_date[i].__contains__('2015-12-19'):
        yalda2015_total_sale += int(df3['Amount_Gross_Order'][i])
        yalda2015_numbers_sold += 1
    elif order_date[i].__contains__('2016-12-21') or order_date[i].__contains__('2016-12-20') or order_date[i].__contains__('2016-12-19'):
        yalda2016_total_sale += int(df3['Amount_Gross_Order'][i])
        yalda2016_numbers_sold += 1
    elif order_date[i].__contains__('2017-12-21') or order_date[i].__contains__('2017-12-20') or order_date[i].__contains__('2017-12-19'):
        yalda2017_total_sale += int(df3['Amount_Gross_Order'][i])
        yalda2017_numbers_sold += 1
    if order_date[i].__contains__('2015'):
        year2015_total_sale += int(df3['Amount_Gross_Order'][i])
        year2015_numbers_sold += 1
    elif order_date[i].__contains__('2016'):
        year2016_total_sale += int(df3['Amount_Gross_Order'][i])
        year2016_numbers_sold += 1
    elif order_date[i].__contains__('2017'):
        year2017_total_sale += int(df3['Amount_Gross_Order'][i])
        year2017_numbers_sold += 1

amount_rel = [(yalda2015_total_sale / year2015_total_sale) * 100, (yalda2016_total_sale / year2016_total_sale) * 100, (yalda2017_total_sale / year2017_total_sale) * 100]
number_rel = [(yalda2015_numbers_sold / year2015_numbers_sold) * 100, (yalda2016_numbers_sold / year2016_numbers_sold) * 100, (yalda2017_numbers_sold / year2017_numbers_sold) * 100]
years = ['2015', '2016', '2017']


figure(num=None, figsize=(10, 6), dpi=100, facecolor='w', edgecolor='k')
plt.plot(years, amount_rel, label='Amount of sales in Yalda per amount of sales in year (Pecentage)', color='#2b18ba')
plt.plot(years, number_rel, label='Number of sales in Yalda per number of sales in year (Pecentage)', color='#fc260a')
plt.legend()
plt.show()


# In[27]:


other_brands_category = []
other_brands_price = []

for i in range(len(df3_df5['product_id'].unique())):
    if df3_df5['brand_name_fa'][i] == 'متفرقه':
        other_brands_category.append(df3_df5['category_title_fa'][i])


other_brands_category = np.unique(other_brands_category)
numbers_bought = []
for i in range(len(other_brands_category)):
    numbers_bought.append(0)
    other_brands_price.append(0)
    for j in range(len(df3_df5['product_id'].unique())):
        if df3_df5['category_title_fa'][j] == other_brands_category[i]:
            numbers_bought[i] += 1
            other_brands_price[i] += df3_df5['Amount_Gross_Order'][j]

most_bought_other_brands = sorted(zip(numbers_bought, other_brands_category, other_brands_price), reverse=True)[:10]

figure(num=None, figsize=(12, 6), dpi=100, facecolor='w', edgecolor='k')
plt.bar([row[1] for row in most_bought_other_brands], [row[0] for row in most_bought_other_brands], color='#10a574')
plt.xlabel('Category')
plt.ylabel('Numbers Bought')
plt.show()


# In[28]:


average_price_per_category_other = []

for i in range(len(most_bought_other_brands)):
    average_price_per_category_other.append(most_bought_other_brands[i][2] / most_bought_other_brands[i][0])
    
figure(num=None, figsize=(12, 6), dpi=100, facecolor='w', edgecolor='k')
plt.bar([row[1] for row in most_bought_other_brands], average_price_per_category_other, color='#d0db32')
plt.xlabel('Category')
plt.ylabel('Average Price')
plt.show()


# In[29]:


numbers_bought = [0] * len(most_bought_other_brands)
not_other_brands_price = [0] * len(most_bought_other_brands)

for i in range(len(df3_df5['product_id'].unique())):
    if df3_df5['brand_name_fa'][i] != 'متفرقه':
        for j in range(len(most_bought_other_brands)):
            if df3_df5['category_title_fa'][i] == most_bought_other_brands[j][1]:
                numbers_bought[j] += 1
                not_other_brands_price[j] += df3_df5['Amount_Gross_Order'][i]
            
average_price_per_category_not_other = []

for i in range(len(most_bought_other_brands)):
    average_price_per_category_not_other.append(not_other_brands_price[i] / numbers_bought[i])

average_price_rel = []
for i in range(len(most_bought_other_brands)):
    average_price_rel.append(average_price_per_category_other[i] / average_price_per_category_not_other[i])
    

figure(num=None, figsize=(12, 6), dpi=100, facecolor='w', edgecolor='k')
plt.bar([row[1] for row in most_bought_other_brands], average_price_rel, color='#db32d8')
plt.xlabel('Category')
plt.ylabel('Average price of other brands per average price of known brands')
plt.show()


# In[30]:


brands = df3_df5['brand_name_fa'].unique()
total_price = [0] * len(brands)
numbers_sold = [0] * len(brands)
for i in range(len(brands)):
    for j in range(len(df3_df5['product_id'])):
        if df3_df5['brand_name_fa'][j] == brands[i]:
            total_price[i] += df3_df5['Amount_Gross_Order'][j]
            numbers_sold[i] += 1

brands_average_price = [0] * len(brands)
for i in range(len(brands)):
    brands_average_price[i] = total_price[i] / numbers_sold[i]

popular_brands = sorted(zip(numbers_sold, brands, brands_average_price), reverse=True)[:10]

figure(num=None, figsize=(12, 6), dpi=100, facecolor='w', edgecolor='k')
plt.bar([row[1] for row in popular_brands], [row[0] for row in popular_brands], color='#3242db')
plt.xlabel('Brand')
plt.ylabel('Numbers Sold')
plt.show()


# In[31]:


figure(num=None, figsize=(12, 6), dpi=100, facecolor='w', edgecolor='k')
plt.bar([row[1] for row in popular_brands], [row[2] for row in popular_brands], color='#ce2b0a')
plt.xlabel('Brand')
plt.ylabel('Average Price')
plt.show()

