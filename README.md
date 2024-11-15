# Auxiliary Network: Scalable and Agile Online Learning for Dynamic System with Inconsistently Available Inputs [Link](https://link.springer.com/chapter/10.1007/978-3-031-30105-6_46)

## Citation

Please consider citing the below paper, if you are using the code provided in this repository.
```
@inproceedings{agarwal2022auxiliary,
  title={Auxiliary Network: Scalable and agile online learning for dynamic system with inconsistently available inputs},
  author={Agarwal, Rohit and Agarwal, Krishna and Horsch, Alexander and Prasad, Dilip K},
  booktitle={International Conference on Neural Information Processing},
  pages={549--561},
  year={2022},
  organization={Springer}
}
```

## Overview
This repository contains datasets and implementation codes of different models for the paper, titled "Auxiliary Network: Scalable and Agile Online Learning for Dynamic System with Inconsistently Available Inputs".


## Datasets
The link of all the datasets can be found below. The italy power demand (ipd) datasets in its corresponding respective folder inside `data/` directory. To run them, please download the datsets files form the given link below and place them inside their respective directories (see instructions for each dataset below...).  

<p align="center">
Small Datsets
</p>  
<hr>

- ### WPBC
    Data link: https://archive.ics.uci.edu/dataset/16/breast+cancer+wisconsin+prognostic  
    Directory: `data/wbc/`  
    (provided in repository/not provided in repository)  

- ### ionosphere
    Data link: https://archive.ics.uci.edu/dataset/52/ionosphere  
    Directory: `data/ionosphere/`  
    (provided in repository/not provided in repository)  

- ### WDBC
    Data link: https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic  
    Directory: `data/wdbc/`  
    (provided in repository/not provided in repository)  

- ### australian
    Data link: https://archive.ics.uci.edu/dataset/143/statlog+australian+credit+approval  
    Directory: `data/australian/`  
    (provided in repository/not provided in repository)  

- ### WBC
    Data link: https://archive.ics.uci.edu/dataset/15/breast+cancer+wisconsin+original  
    Directory: `data/wbc/`  
    (provided in repository/not provided in repository)  

- ### diabetes-f
    Data link: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database  
    Directory: `data/diabetes_f/`  
    (provided in repository/not provided in repository)  
    **Instructions**: After downloading the file change it's name from `diabetes.csv` to `diabetes_f.csv` 

- ### german
    Data link: https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data  
    Directory: `data/german`  
    (provided in repository/not provided in repository)  

- ### IPD
    Data link: https://www.timeseriesclassification.com/description.php?Dataset=ItalyPowerDemand  
    Directory: `data/ipd`  
    (provided in repository/not provided in repository)  
    Instructions: Download the dataset from the link, and place the files `ItalyPowerDemand_TEST.txt` and `ItalyPowerDemand_TRAIN.txt` inside the directory.   

- ### svmguide3
    Data link: https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary.html#svmguide3  
    Directory: `data/svmguide3`  
    (provided in repository/not provided in repository)  

- ### kr-vs-kp
    Data link: https://archive.ics.uci.edu/dataset/22/chess+king+rook+vs+king+pawn  
    Directory: `data/krvskp`  
    (provided in repository/not provided in repository)  

- ### spambase
    Data link: https://archive.ics.uci.edu/dataset/94/spambase  
    Directory: `data/spambase`  
    (provided in repository/not provided in repository)  

- ### spamassasin
    Data link: https://spamassassin.apache.org/old/publiccorpus/  
    Directory: `data/spamassasin`  
    (provided in repository/not provided in repository) 

<p align="center">
Medium Datsets
</p> 
<hr>

- ### magic04
    Data link: https://archive.ics.uci.edu/dataset/159/magic+gamma+telescope  
    Directory: `data/magic04`  
    (provided in repository/not provided in repository)  

- ### imdb
    Data link: https://ai.stanford.edu/~amaas/data/sentiment/  
    Directory: `data/imdb`  
    (provided in repository/not provided in repository)  

- ### a8a
    Data link: https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary.html#a8a  
    Directory: `data/a8a`  
    (provided in repository/not provided in repository)  

<p align="center">
Large Datsets
</p>   
<hr>

- ### diabets_us
    Data link: Supplementary Material at https://www.hindawi.com/journals/bmri/2014/781670/#supplementary-materials  
    Directory: `data/diabetes_us`  
    (provided in repository/not provided in repository)  

- ### SUSY
    Data link: https://archive.ics.uci.edu/dataset/279/susy  
    Directory: `data/susy`  
    (provided in repository/not provided in repository)  

- ### HIGGS
    Data link: https://archive.ics.uci.edu/dataset/280/higgs  
    Directory: `data/higgs`  
    (provided in repository/not provided in repository) 

## Raw Data Transformation
Some of the data sets need to be cleaned and processesed before they can be used in the models for inference. Details of how to process those datasets are given below.

- Spamassasin
    - Download the files form the link provided and unzip them.  
    - Use the sctipt `Code\DataCode\DataPreparation\data_spamassasin_conversion.py` to clean the data.
    - Modify the 'path' variable at line 13 to the path of the directory where the unzipped files are located.  
    - The data will automatically be saved in the appropriate directory.

- IMDB  
    - Download the files form the link provided and unzip them.  
    - Use the sctipt `Code\DataCode\DataPreparation\data_imdb_conversion.py` to clean the data.
    - Modify the 'data_path' variable at line 10 to the path of the directory where the unzipped files are located.  
    - The data will automatically be saved in the appropriate directory.

- Diabetes_us  
    - After downloading the dataset from the provided link, follow the instructions at https://www.hindawi.com/journals/bmri/2014/781670/#supplementary-materials to prepare it for analysis

## Dataset Preparation
### Variable P
For synthetic datasets, we varied the availability of each auxiliary input feature independently by a uniform distribution of probability $p$, i.e., each auxilairy feature is available for $100p\%$. For more information about this, follow paper - Aux-Net (https://link.springer.com/chapter/10.1007/978-3-031-30105-6_46)

## Files
To run the models, see `Code/main.py`. After running a model on a certain dataset, run `Code/read_results.py` to display and save the evaluation in csv format.  

## Control Parameters

For **main.py** file, 
1. `seed` : Seed value  
_default_ = 2023

2. `type`: The type of the experiment. If type is basefeatures then please provide the number of base feature using --nbasefeat.
    If type is noassumption then please provide either the imputation or dummy feature details.
    _default_="noassumption", type=str,  
    _choices_ = ["noassumption", "basefeatures"]

<p align="center">
Data Variables
</p>
<hr>

3. `dataname`: The name of the dataset  
_default_ = "wpbc"  
_choices_ = ["all", "synthetic", "crowdsense_c5", "crowdsense_c3" "spamassasin", "imdb", "diabetes_us", "higgs", "susy", "a8a" "magic04", "spambase", "krvskp", "svmguide3", "ipd", "german" "diabetes_f", "wbc", "australian", "wdbc", "ionosphere", "wpbc"]

4. `syndatatype`: The type to create suitable synthetic dataset  
    _default_ = "variable_p"

5. `probavailable`: The probability of each feature being available to create synthetic data  
    _default_ = 0.5, type = float

<p align="center">
Base feature argument
</p>
<hr>

6. `nbasefeat`: The number of base feature. This code considers the first nbasefeat as the base features.
    _default_ = 0, type = int

<p align="center">
Method Variables
</p>
<hr>

7. `ifimputation`: If some features needs to be imputed  
    _default_ = False
    
8. `imputationtype`: The type of imputation technique to create base features  
    _default_ = 'forwardfill'  
    _choices_ = ['forwardfill', 'forwardmean', 'zerofill']

9. `nimputefeat`: The number of imputation features  
    _default_ = 2   

10. `ifdummyfeat`: If some dummy features needs to be created  
_default_ = False

11. `dummytype`: The type of technique to create dummy base features  
default = 'standardnormal'

12. `ndummyfeat`: The number of dummy features to create'  
    _default_ = 1    

13. `nruns`: The number of times a method should runs (For navie Bayes, it would be 1 because it is a deterministic method)  
_default_ = 5  

For **read_results.py** file,
1. `type`: The type of the experiment  
    _default_ ="noassumption"  
    _choices_ = ["noassumption", "basefeatures"]  

2. `dataname`: The name of the dataset  
    _default_ = "wpbc"  
    _choices_ = ["synthetic", "real", "crowdsense_c5", "crowdsense_c3", "spamassasin", "imdb", "diabetes_us", "higgs", "susy", "a8a", "magic04", "spambase", "krvskp", "svmguide3", "ipd", "german", "diabetes_f", "wbc", "australian", "wdbc", "ionosphere", "wpbc"]

3. `probavailable`: The probability of each feature being available to create synthetic data  
    _default_ = 0.5

## Dependencies
1. numpy
2. torch
3. pandas
4. random
5. tqdm
6. os
7. pickle

## Running the code

To run the models, change the control parameters accordingly in the **main.py** file and run
```
python Code/main.py
```

1. To run the code by the assigning the first 2 features as base features, do
```
python Code/main.py --type basefeatures --dataname ipd --nbasefeat 2
```

2. To run the code without any assumption (as these models were modified from their original implementation to support the absence of (previously required) base-feature), we have two options:
    - Imputing some features and consider them as base feature
        ```
        python Code/main.py --type noassumption --dataname ipd --ifimputation True --imputationtype forwardfill --nimputefeat 2
        ```
    - Making dummy features and consider them as base feature
        ```
        python Code/main.py --type noassumption --dataname ipd --ifdummyfeat True --dummytype standardnormal --ndummyfeat 2
        ```
<hr>

To read the results and save them in .csv format, run **read_results.py** with appropriate control parameters.
```
python Code/read_results.py --type basefeatures --dataname ipd
```
