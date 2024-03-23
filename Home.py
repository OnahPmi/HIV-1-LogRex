import streamlit as st
import numpy as np
import pandas as pd


st.set_page_config(page_title="Home", 
                   page_icon="project_data/favicon.jpg", 
                   layout="wide", 
                   initial_sidebar_state="expanded",
                   menu_items={'About': "HIV1-LogRex: Predicting Octapeptide Sequence Cleavage Site"})


st.write("## :rainbow[Welcome to HIV1-LogRex Webserver: Accelerate HIV-1 Protease Inhibitor Discovery]")
st.divider()
cola1, cola2 = st.columns([0.4, 0.6], gap="large")
cola2.image("project_data/homepageimage.png", width=None, use_column_width="auto")
cola2.subheader(":rainbow[Predicting Octapeptide Sequence Cleavage Site]")

# cola11, cola22 = st.columns([0.8, 0.2], gap="large")
# cola11.title(":rainbow[Welcome to HIV1-LogRex Webserver]")
# cola11.divider()
# cola1, cola2 = st.columns([0.4, 0.6], gap="large")
# cola2.image("project_data/homepageimage.png", width=None, use_column_width="auto")
# cola2.subheader(":rainbow[Predicting Octapeptide Sequence Cleavage Site]")

with st.container():
    st.markdown("***")
    st.markdown("""
    **This server implements varied algorithms for octapeptide descriptors calculations and the logistic regression model 
    (`HIV1-LogRex`) for HIV-1 protease cleavage site prediction for various machine/deep learning applications in 
    bioinformatics.**
    """)
    
    st.markdown("""
    **The calculated features such as the _amino acid binary profile_, which is a `one-hot-encoding` of peptides and some 
    physicochemical properties are needed for building robust models for the task of predicting the cleavage status of an 
    octapeptide. The sidebar shows the implementation of the various tools this webserver has to offer.**
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
    
    st.markdown("""
    **This work has been published at _BMC Bioinformatics_ [https://doi.org/10.1186/s12859-022-05017-x](https://doi.org/10.1186/s12859-022-05017-x)**""")

with st.expander("See Details Related to the Model's Training Procedure", expanded=True):
    st.markdown("""
     In most parts of the world, especially in underdeveloped countries, _Acquired Immunodeficiency Syndrome (AIDS)_ 
     still remains a major cause of death, disability and unfavorable economic outcomes. This has necessitated 
     intensive research to develop effective therapeutic agents for the treatment of _Human Immunodeficiency Virus 
     (HIV)_ infection, which is responsible for AIDS.  Peptide cleavage by `HIV-1 protease` is an essential step in 
     the replication of HIV-1. Thus, correct and timely prediction of the cleavage site of HIV-1 protease can 
     significantly speed up and optimize the drug discovery process of novel HIV-1 protease inhibitors.
     ***
     In this work, we present a `Logistic Regression Model` for predicting the substrate specificity and cleavage 
     site of HIV-1 protease. First, we built and compared the performance of selected machine learning models for 
     the prediction of HIV-1 protease cleavage site utilizing a hybrid of octapeptide sequence information comprising 
     `bond composition`, `amino acid binary profile (AABP)`, and `physicochemical properties` as numerical descriptors 
     serving as input variables for some selected machine learning algorithms. Our work differs from antecedent 
     studies exploring the same subject in the combination of octapeptide descriptors and method used. Instead of 
     using various subsets of the dataset for training and testing the models, we combined the dataset, applied a 
     3-way data split, and then used a "stratified" 10-fold cross-validation technique alongside the testing set
     to evaluate the models.
     ***
     This procedure showed that the `logistic regression model` and the `multi-layer perceptron classifier` achieved
     superior performance comparable to that of the state-of-the-art model, `linear support vector machine`. Our feature 
     selection algorithm implemented via the `decision tree algorithm` showed that the underlisted descriptors were the top 
     features selected during the models' training. 
     * `AABP → Amino Acid Binary Profile`
     * `PCP_BS → Composition of basic residues` 
     * `PCP_HL → Composition of hydrophilic residues` 
     ***
     This supports previous findings that water accessibility served as a discriminative factor to predict cleavage sites 
     [Warut et. al, 2022]( https://doi.org/10.1155/2022/8513719).
     ***
     Some of the performance metrics employed during model training and their values are shown below:""")
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Balanced Accuracy", "90.9 %")
    col2.metric("AUC", "0.97")
    col3.metric("F-Index", "0.91")
    col4.metric("Jaccard Index", "0.83")
    col5.metric("Specificity", "0.90")
    col6.metric("Sensitivity", "0.57")
    
with st.expander("Charts Related to the Model's Training Procedure", expanded=False):    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["ROC Curves", 
                                            "Model Training Algorithm", 
                                            "Feature Importance Plot by GBC", 
                                            "Sequence Logos of Cleaved and Uncleaved Octapeptides", 
                                            "10-Fold CV Metrics Distribution"])

    with tab1:
        st.markdown("""
        **ROC Curves of the Models on the Testing Set**""")
        st.image("project_data/ROC_Curves_of_the_Models_on_the_Testing_Set.png")

    with tab2:
        st.markdown("""
        **Model Training Algorithm**""")
        st.image("project_data/Model_Training_Flow_Chart.jpg")

    with tab3:
        st.markdown("""
        **Gini importance chart of the best 20 features selected by the Gradient Boosting Classifier**""")
        st.image("project_data/Plot_of_feature_importance_for_GB_classifier.png")

    with tab4:
        st.markdown("""
        **The sequence logos of A) cleaved octapeptide; B) un-cleaved octapeptide sequences generated
        with the online Seq2Logo webserver using Heuristic clustering algorithm, pseudo count with a
        weight of 200 and logotype as Kullback–Leibler. Enriched amino acids are shown on the positive
        y-axis and depleted amino acids on the negative y-axis**""")
        st.image("project_data/seq_logo_of_cleaved_&_uncleaved_octapeptides.png")

    with tab5:
        st.markdown("""
        **Distribution of the performance metrics scores of the models in the 10-fold CV experiment for
        each of the 6 standard tests conducted. a) Balanced Accuracy Scores; b) Sensitivity Scores; c)
        Specificity Scores; d) F-score; e) AUC; and f) Jaccard Index Scores**""")
        st.image("project_data/Distribution_of_the_Performance_Metrics_Across_the_Models.png")
    
with st.container():
    st.markdown("""
    ### Further information

    #### References    
     * Warut P, Kwanluck TA, Kasidit S, Parthana P, Jirachai B. "Hyperparameter Tuning of Machine Learning Algorithms
       Using Response Surface Methodology: A Case Study of ANN, SVM, and DBN", Mathematical Problems in Engineering. 2022,
       vol. 2022, Article ID 8513719, 17 pages [https://doi.org/10.1155/2022/8513719](https://doi.org/10.1155/2022/8513719).
       
    #### Inspiration  
      > A lot of inspirations was drawn from the works of the Raghava group, headed by Professor Raghava, the Head of the 
        Department of Computational Biology, Indraprastha Institute of Information Technology (IIIT-Delhi), India. Particularly, 
        their work on the [pfeature software](https://github.com/raghavagps/Pfeature) gave us insight on developing the various 
        algorithms for generating the Amino Acid Binary Profile, Composition of Basic and Hydrophilic Residues present in 
        Octapeptides. Worthy of note also is the work of [Singh & Su](https://doi.org/10.1186/s12859-016-1337-6). 
                
    #### Links to Other Tools by the same author 
    * ###### [:blue[ChemFetchTool: Automate Molecular Properties Retrieval from PubChem]](https://chemfetchtool.streamlit.app/).  
      > ChemFetchTool is a web-based tool employing the PubChem PUG REST API endpoint for automated retrieval of molecular properties 
        given only the compound name(s)
    
    #### Authors' Publications              
      > The authors have published a number of works in the _in silico_ drug design/bioinformatics domain spanning across
        various disease conditions like `Cancer`, `Infectious Diseases`, and `Neurodegenerative Disorders`. Notable examples
        include:  
      * Ibezim A, Onah E, Osigwe SC, Okoroafor PU, Ukoha OP, De Siqueira-Neto JL, Ntie-Kang F and Ramanathan, K. Potential 
        Dual Inhibitors of Hexokinases and Mitochondrial Complex I Discovered Through Machine Learning Approach. Available at SSRN:  
        [https://dx.doi.org/10.2139/ssrn.4635544](https://dx.doi.org/10.2139/ssrn.4635544)
      * Onah E, Uzor PF, Ugwoke IC, Eze JU, Ugwuanyi ST, Chukwudi IR, Ibezim A. Prediction of HIV-1 protease cleavage site 
        from octapeptide sequence information using selected classifiers and hybrid descriptors. BMC Bioinformatics. 2022 Nov 
        8;23(1):466. PMID: 36344934. PMCID: 9641908.  
        [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9641908/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9641908/). 
      * Ibezim A, Onah E, Dim EN, Ntie-Kang F. A computational multi-targeting approach for drug repositioning for psoriasis 
        treatment. BMC Complement Med Ther. 2021 Jul 5;21(1):193. PMID: 34225727. PMCID: 8258956.  
        [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8258956/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8258956/).
      * Onah, E., Ugwoke, I., Eze, U., Eze, H., Musa, S., Ndiana-Abasi, S., Okoli, O., Ekeh, I., & Edet, A. (2021). 
        Search for Structural Scaffolds Against SARS-COV-2 Mpro: An In Silico Study. Journal of Fundamental and Applied 
        Sciences, 13(2), 740-769.   
        [https://jfas.info/index.php/JFAS/article/view/987](https://jfas.info/index.php/JFAS/article/view/987).
        """)
    st.markdown("""#### If you utilize :rainbow[HIV1-LogRex] in your research, please cite it as follows:  
    Onah E. (2024). HIV1-LogRex: Accelerate HIV-1 Protease Inhibitor Discovery (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.10851067.""")

