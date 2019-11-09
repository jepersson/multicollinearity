# %% [markdown]
# Introduction
Feature selection is a very important step in modelling and while domain 
knowledge and common sense can be of tremendous help for narrowing down the 
number of features you feed your model sometimes the sheer amount of features
available makes this impossible as a first step. This happened me at work not
so long ago when one of the working data sets contains data spanning 10,000+
features. In order to deal with this we turned to Random Forests for their
suitability when tackling large amount of features and to the models feature 
importances in an attempt to weed out the unecessary features.

However, things doen't end there, otherwise this would be a short blog post, 
as some of you most likely have been screaming out while reading the above 
paragraph default feature importances in sklearn isn't very reliable and a lot
is given up to chance in the ranking. Rather than going through all of it here
I will just link to [this](https://explained.ai/rf-importance/) blog post. 

# %%
