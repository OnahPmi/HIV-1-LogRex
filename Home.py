#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import numpy as np
import pandas as pd


st.set_page_config(page_title="Home", page_icon="project_data/favicon.jpg", layout="wide", initial_sidebar_state="expanded")

with st.container():
    st.markdown("""
    # `Welcome to HIV1-LogRex Webserver`
    """)
    st.markdown("***")
    st.markdown("""
    **This server impliments varied algorithms for octapeptide descriptors calculations and the logistic regression model 
    (`HIV1-LogRex`) for HIV-1 protease cleavage site prediction for various machine/deep learning applications in 
    bioinformatics.**
    """)
    
    st.markdown("""
    **The calculated features such as the _amino acid binary profile_, which is a `one-hot-encoding` of peptides and some 
    physicochemical properties are needed for bulding rubost models for the task of predicting the cleavage status of an 
    octapeptide. The sidebar shows the implimentation of the various tools this webserver has to offer.**
    """)
    st.markdown("***")
    col1, col2 = st.columns(2)
    with col1: 
        st.markdown("""
        * The **`Make Prediction`** tool predicts the cleavage status of octapeptide sequence(s). The generated results 
          can be applied to making improved decision on various drug design/bioinformatics tasks.
        """)
    with col2:
        st.markdown("""
        * The **`Calculate Descriptor`** tool calculates and returns a CSV file of the calculated descriptors which can
          be downloaded for various machine/deep learning applications in the design of potent HIV drugs.
        """)
   
   
with st.expander("Charts Related to the Model's Training Procedure. Each Heading Contains a Related Chart", expanded=True):    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["ROC Curves", 
                                            "Model Training Algorithm", 
                                            "Feature Importance Plot by GBC", 
                                            "Sequence Logos of Cleaved and Uncleaved Octapeptides", 
                                            "10-Fold CV Metrics Distribution"])

    with tab1:
        # st.markdown("""
        # **ROC Curves of the Models on the Testing Set**""")
        st.image("project_data/ROC_Curves_of_the_Models_on_the_Testing_Set.png", caption="ROC Curves of the Models on the Testing Set")

    with tab2:
        # st.markdown("""
        # **Model Training Algorithm**""")
        st.image("project_data/Model_Training_Flow_Chart.jpg", caption="Model Training Algorithm")

    with tab3:
        # st.markdown("""
        # **Gini importance chart of the best 20 features selected by the Gradient Boosting Classifier**""")
        st.image("project_data/Plot_of_feature_importance_for_GB_classifier.png", caption="Gini importance chart of the best 20 features selected by the Gradient Boosting Classifier")

    with tab4:
        # st.markdown("""
        # **The sequence logos of A) cleaved octapeptide; B) un-cleaved octapeptide sequences generated
        # with the online Seq2Logo webserver using Heuristic clustering algorithm, pseudo count with a
        # weight of 200 and logotype as Kullback–Leibler. Enriched amino acids are shown on the positive
        # y-axis and depleted amino acids on the negative y-axis**""")
        st.image("project_data/seq_logo_of_cleaved_&_uncleaved_octapeptides.png", caption="The sequence logos of A) cleaved octapeptide; B) un-cleaved octapeptide sequences generated with the online Seq2Logo webserver using Heuristic clustering algorithm, pseudo count with a weight of 200 and logotype as Kullback–Leibler. Enriched amino acids are shown on the positive y-axis and depleted amino acids on the negative y-axis")

    with tab5:
        # st.markdown("""
        # **Distribution of the performance metrics scores of the models in the 10-fold CV experiment for
        # each of the 6 standard tests conducted. a) Balanced Accuracy Scores; b) Sensitivity Scores; c)
        # Specificity Scores; d) F-score; e) AUC; and f) Jaccard Index Scores**""")
        st.image("project_data/Distribution_of_the_Performance_Metrics_Across_the_Models.png", caption="Distribution of the performance metrics scores of the models in the 10-fold CV experiment for each of the 6 standard tests conducted. a) Balanced Accuracy Scores; b) Sensitivity Scores; c) Specificity Scores; d) F-score; e) AUC; and f) Jaccard Index Scores")
    
with st.container():
    st.markdown("""
    #### References:    
     * Warut P, Kwanluck TA, Kasidit S, Parthana P, Jirachai B. "Hyperparameter Tuning of Machine Learning Algorithms
       Using Response Surface Methodology: A Case Study of ANN, SVM, and DBN", Mathematical Problems in Engineering. 2022,
       vol. 2022, Article ID 8513719, 17 pages [https://doi.org/10.1155/2022/8513719](https://doi.org/10.1155/2022/8513719).
       
    #### Further information:  
     * A lot of inspirations was drawn from the works of the Raghava group, headed by Professor Raghava, the Head of the 
       Department of Computational Biology, Indraprastha Institute of Information Technology (IIIT-Delhi), India. Particularly, 
       their work on the [pfeature software](https://github.com/raghavagps/Pfeature) gave us insight on developing the various 
       algorithms for generating the Amino Acid Binary Profile, Composition of Basic and Hydrophilic Residues present in 
       Octapeptides. Worthy of note also is the work of [Singh & Su](https://doi.org/10.1186/s12859-016-1337-6). 
    
     * The authors have published a number of works in the _in silico_ drug design/bioinformatics domain spanning across
       various disease conditions like `Cancer`, `Infectious Diseases`, and `Neurodegenerative Disorders`. Notable examples
       include:  
        * Onah, E., Uzor, P.F., Ugwoke, I.C. et al. (2022) Prediction of HIV-1 protease cleavage site from octapeptide sequence  
          information using selected classifiers and hybrid descriptors. BMC Bioinformatics 23, 466.  
          [https://doi.org/10.1186/s12859-022-05017-x](https://doi.org/10.1186/s12859-022-05017-x). 
        * Ibezim A., Onah E., Dim E.N., and Ntie-Kang F. (2021). A Computational Multi-targeting Approach for Psoriasis 
          Treatment. BMC Complementary Medicine and Therapies, 21(1), 193.
          [https://doi.org/10.1186/s12906-021-03359-2](https://doi.org/10.1186/s12906-021-03359-2).
        * Onah, E., Ugwoke, I., Eze, U., Eze, H., Musa, S., Ndiana-Abasi, S., Okoli, O., Ekeh, I., & Edet, A. (2021). 
          Search for Structural Scaffolds Against SARS-COV-2 Mpro: An In Silico Study. Journal of Fundamental and Applied 
          Sciences, 13(2), 740-769. 
          [https://jfas.info/index.php/JFAS/article/view/987](https://jfas.info/index.php/JFAS/article/view/987).
    """)

