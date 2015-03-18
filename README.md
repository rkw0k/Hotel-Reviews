# Hotel-Reviews
Suggest-Inn, hotel recommender that finds the best value for your price.

www.suggest-inn.com

### Motivation
According to Michele Walters, Co-Founder of Origin World Labs, hotel data science seems to have a plethora of untapped, solvable problems.

[(article by Michele Walters)](http://hotelexecutive.com/business_review/3619/hotel-data-science-a-new-profession-for-the-new-era-of-advanced-hospitality)

"This shortage will hit the hospitality industry especially hard as it tends to be 
at the bottom of the totem pole for attracting analytical and technical talent. 
Unfortunately, hospitality is still perceived as an industry where soft skills are 
overwhelmingly more important than hard skills."

"Companies such as Marriott and Disney have realized that hospitality is a data-intensive 
business and that there is a wealth of creative strategies and tactics that can be found 
when the data is analyzed by professionals. Yet, even for these big brands the single biggest 
obstacle to making data-driven progress is their inability to find enough qualified talent to 
fill their analytics positions." 

### Data Sources:
Anonymized hotel_id data was obtained by [Professor Hongning Wang](http://www.cs.virginia.edu/people/faculty/hwang.html).

He and co-authors have accompanying machine learning papers discovering latent aspects in the rating.
Overview of data:
`2232 Hotels, 37181 Reviews, 34187 Reviewers, 96.5 Avg Len, [3.92-1.23, 3.929+1.23] Rating.`

[Data page](http://times.cs.uiuc.edu/~wang296/Data/)

"Latent Aspect Rating Analysis on Review Text Data: A Rating Regression Approach", [paper](http://sifaka.cs.uiuc.edu/~wang296/paper/rp166f-wang.pdf),
[slides](http://times.cs.uiuc.edu/~wang296/paper/hongning-KDD10-v2.pptx)

"Latent Aspect Rating Analysis without Aspect Keyword Supervision",
[paper](http://sifaka.cs.uiuc.edu/~wang296/paper/p618.pdf),
[slides](http://times.cs.uiuc.edu/~wang296/paper/latent-aspect-rating-analysis.pptx)

### Model
#### K-Means 
Clustering on four aspect ratings `Value, Room, Location, Cleanliness` (the features)

from the table `H_normed` in the database `app.db` available in the `web-app` folder. 

### Pipeline

Store data from [Data page] into SQL databases. Group ratings by
hotel_id and average the predictions for the aspect ratings.

### Future work

1. Scrape hotel data from Yelp using their API and have non-anonymized data.
2. Create LARA, a combination of regression and maximum likelihood estimation,
   code for python to get prediction for the four aspects listed above in Model.
3. Use word2vec on the keywords extracted from LARA to build an alternative
   model for unsupervised learning.
  


