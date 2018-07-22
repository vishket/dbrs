# DBRS Technical Assessment

## To Run

To access the Notebook, Navigate to

https://ec2-52-14-156-217.us-east-2.compute.amazonaws.com:8888/tree/dbrs

Enter password

Inside the dbrs folder, click on the 'assessment.ipynb' file to launch the
notebook

## Downloading just the 2017 dataset

*To filter only 2017 dataset*

The SR 2010 - present dataset on NYC opendata allows you to filter based on
conditions. I created my own NYC opendata (to be able to save my filters) and
filtered based on 'created_date' field.

*To select only required columns*

I found this option on NYC open data that allows you to "Edit". I had to manually
delete each column that I did not need

*Export*

Finally, exported the new dataset as csv

## Task 1

*Consider only the 10 most common overall complaint types. For each borough, how many of each of those 10 types were there in 2017?*

I was able to implement this successfully and have provided further explanation
in the Notebook

## Task 2

*Consider only the 10 most common overall complaint types.  For the 10 most populous zip codes, how many of each of those 10 types were there in 2017?*

**The Population dataset**

I was unable to get a dataset that had the NYC population along with zip codes.
The Open NYC data site had a 2010 census data but was only available to be
viewed on a map. The closest I found on the internet was this:
https://blog.splitwise.com/2013/09/18/the-2010-us-census-population-by-zip-code-totally-free/

But instead of having zip codes, it has ZTCA which is different in quite a lot
of cases

As a result, for this technical assessment I chose the above dataset to partially
implement Task 2. I have still explained the steps I would do if I had the
correct dataset. Detailed explanation in Notebook

## Task 3

*Considering all complaint types. Which boroughs are the biggest "complainers" relative to the size of the population in 2017? Meaning, calculate a complaint-index that adjusts for population of the borough.*

Had the same issue here with not having the correct dataset. But I have still
outlined my steps to get the most "complainers" relative to population. Detailed
explanation in Notebook

## Deploying the Notebook

I logged in using the credentials provided and added myself to the Userdemo group.
That allowed me to create instances. I chose the ...

amzn-ami-hvm-2018.03.0.20180622-x86_64-gp2 (ami-40142d25)

... AMI as it had python, AWS command line tool pre installed. I added new security
group to allow inbound traffic on port 8888, on which Jupyter notebook will be serving
requests. Also created a new ssh key pair and saved the pem file locally

Once created, I download and installed Anaconda for Linux

I added some basic configuration such as passwords, certificates for HTTPS and
a Notebook folder

Finally, launched Jupyter Notebook in an attached screen
