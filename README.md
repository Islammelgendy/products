##  products classification 
In this task I scrapped a text data from ([https://2b.com.eg/)](https://2b.com.eg)  about 5 different categories : 
- Computer 
- Mobile and Tablet 
- Gaming 
- Home Appliances.
- Accessories

###  the data scraped from the site is 
- URL
- Title 
- Main Category 

###  Main Technologies or Frameworks.

- python version = 3.8.5
-  scrapy
- scikit-learn 
-  Fast API 
- Docker

## Approach 

- Crawled the data set and saved into CSV file and SQLite database .
-  Explored the dataset to better understand the data and found the the dataset was unbalanced 
-  Handled the unbalance  with different methods 
    - Equal random sample from each Category 
    - Oversampling
    - Cost-Sensitive Learning for Multi-Class Classification  
 - metric : Accuracy 
 - deployed the using docker on google cloud services 
 > ## Instructions for running project on local Host 
- create new virtual environment for your project 
-  install the requirements by running this command 'pip3 install -r requirements.txt'
###  to run the API on [http://localhost.com](http://localhost.com)  
- change you directory to api directory and run this command 'uvicorn main:app --reolad' , don't use ('-- reload ') in production 
  - now you must be able to show page like this 
  
![image](https://user-images.githubusercontent.com/50594417/140556418-7eeb46f7-5f01-47a0-b3cb-29820045e68f.png)

- you can try out the [deployed api on GCP](https://task-axrrkgh2nq-rj.a.run.app/docs#/default/category_get_category_get)

## to run the scraping script 
- change your directory to product and run this commnad "scrapy crawl -O <filename>" 

## products.db file 
![image](https://user-images.githubusercontent.com/50594417/140556765-48c7c4f5-58f1-4813-a0c5-4910781e93eb.png)

