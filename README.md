# Welcome to HIV1-LogRex Webserver [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://octapeptide-cleavage-site-prediction-stream.streamlitapp.com/)
##  This server impliments varied algorithms for octapeptide descriptors calculations and the logistic regression model (`HIV1-LogRex`) for HIV-1 protease cleavage site prediction for various machine/deep learning applications in bioinformatics.
##### This work has been published at _BMC Bioinformatics_ [https://doi.org/10.1186/s12859-022-05017-x](https://doi.org/10.1186/s12859-022-05017-x)
**In most parts of the world, especially in underdeveloped countries, _Acquired Immunodeficiency Syndrome (AIDS)_ still remains a major cause of death, disability and unfavorable economic outcomes. This has necessitated intensive research to develop effective therapeutic agents for the treatment of _Human Immunodeficiency Virus (HIV)_ infection, which is responsible for AIDS.  Peptide cleavage by `HIV-1 protease` is an essential step in the replication of HIV-1. Thus, correct and timely prediction ofthe cleavage site of HIV-1 protease can significantly speed up and optimize the drug discovery process of novel HIV-1 protease inhibitors.**
***
**In this work, we present a `Logistic Regression Model` for predicting the substrate specificity and cleavage site of HIV-1 protease. First, we built and compared the performance of selected machine learning models for the prediction of HIV-1 protease cleavage site utilizing a hybrid of octapeptide sequence information comprising 
`bond composition`, `amino acid binary profile (AABP)`, and `physicochemical properties` as numerical descriptors serving as input variables for some selected machine learning algorithms. Our work differs from antecedent studies exploring the same subject in the combination of octapeptide descriptors and method used. Instead of using various subsets of the dataset for training and testing the models, we combined the dataset, applied a 3-way data split, and then used a "stratified" 10-fold cross-validation technique alongside the testing set to evaluate the models.**
***
**This procedure showed that the `logistic regression model` and the `multi-layer perceptron classifier` achieve superior performance comparable to that of the state-of-the-art model, `linear support vector machine`. Our feature selection algorithm implemented via the `Decision tree model` showed that**: 

* `AABP → Amino Acid Binary Profile` **and two of the physicochemical properties, mamely**: 
* `PCP_BS → Composition of basic residues`, **and** 
* `PCP_HL → Composition of hydrophilic residues` 

**were top features selected by during model training. This supports previous findings that water accessibility served as a discriminative factor to predict cleavage sites [Warut et. al, 2022]( https://doi.org/10.1155/2022/8513719).**
