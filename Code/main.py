#--------------Libraries--------------#
import os
import argparse
import random
import numpy as np
import sys
import pickle
# sys.path.append('/code/DataCode/')
path_to_result = os.getcwd() + "/results/" 

#--------------Import Functions--------------#
from Utils import utils
from DataCode import data_load
from Models.run_auxnet import run_auxnet
from Config import config_models

#--------------All Variables--------------#
if __name__ == '__main__':
    __file__ = os.path.abspath('')
    parser = argparse.ArgumentParser()

    parser.add_argument('--seed', default=2023, type=int, help='Seeding Number')
    parser.add_argument('--type', default="noassumption", type=str,
                        choices = ["noassumption", "basefeatures"], 
                        help='The type of the experiment. If type is basefeatures then please provide the number \
                        of base feature using --nbasefeat. \
                        If type is noassumption then please provide either the imputation or dummy feature details.')
    
    # Data Variables
    parser.add_argument('--dataname', default = "wpbc", type = str,
                        choices = ["all", "synthetic", "crowdsense_c5", "crowdsense_c3", "spamassasin", "imdb", "diabetes_us", "higgs", "susy", "a8a", "magic04", 
                                   "spambase", "krvskp", "svmguide3", "ipd", "german", 
                                   "diabetes_f", "wbc", "australian", "wdbc", "ionosphere", "wpbc"],
                        help='The name of the data')
    parser.add_argument('--syndatatype', default = "variable_p", type = str,
                        help = "The type to create suitable synthetic dataset")
    parser.add_argument('--probavailable', default = 0.5, type = float,
                        help = "The probability of each feature being available to create synthetic data")
    
    # Base feature argument
    parser.add_argument('--nbasefeat', default=0, type = int,
                        help = "The number of base feature. This code considers the first nbasefeat as the base features.")

    # Aux-Net Method Variables
    parser.add_argument('--ifimputation', default = False, type = bool,
                        help = "If some features needs to be imputed")
    parser.add_argument('--imputationtype', default = 'forwardfill', type = str,
                        choices = ['forwardfill', 'forwardmean', 'zerofill'],
                        help = "The type of imputation technique to create base features")
    parser.add_argument('--nimputefeat', default = 2, type = int,
                        help = "The number of imputation features")    
    parser.add_argument('--ifdummyfeat', default = False, type = bool,
                        help = "If some dummy features needs to be created")
    parser.add_argument('--dummytype', default = 'standardnormal', type = str,
                        help = "The type of technique to create dummy base features")
    parser.add_argument('--ndummyfeat', default = 1, type = int,
                        help = "The number of dummy features to create")    
    parser.add_argument('--nruns', default = 5, type =  int,
                        help = "The number of times a method should runs.")

    args = parser.parse_args()

    seed = args.seed
    type = args.type
    data_name = args.dataname
    syn_data_type = args.syndatatype
    p_available = args.probavailable
    if_imputation = args.ifimputation
    imputation_type = args.imputationtype
    n_impute_feat = args.nimputefeat
    if_dummy_feat = args.ifdummyfeat
    dummy_type = args.dummytype
    n_dummy_feat = args.ndummyfeat
    n_runs = args.nruns
    n_base_feat = args.nbasefeat

    data_name_list= []
    if data_name == "all":
        data_name_list= ["crowdsense_c5", "crowdsense_c3", "spamassasin", "imdb", 
                        "diabetes_us", "higgs", "susy", "a8a", "magic04", 
                        "spambase", "krvskp", "svmguide3", "ipd", "german", 
                        "diabetes_f", "wbc", "australian", "wdbc", "ionosphere", "wpbc"]
    elif data_name == "synthetic":
        data_name_list= ["wpbc", "ionosphere", "wdbc", "australian", "wbc", "diabetes_f", "german", "ipd", 
                         "svmguide3", "krvskp", "spambase", "magic04", "a8a", "susy", "higgs"] 
    else:
        data_name_list = [data_name]
    
    for data_name in data_name_list:
        print("Data Name:", data_name)
        
        result_addr = path_to_result + type + "/auxnet/" + data_name

        data_type = "Synthetic"
        if data_name in ["imdb", "diabetes_us", "spamassasin", "naticusdroid", "crowdsense_c3", "crowdsense_c5"]:
            data_type = "Real"
        
        param_dict = {"type": type, "data_name": data_name, "data_type": data_type,
                "seed": seed,
                "syn_data_type": syn_data_type,
                "p_available": p_available,
                "if_imputation": if_imputation, "imputation_type": imputation_type,
                "n_impute_feat": n_impute_feat, "if_dummy_feat": if_dummy_feat,
                "dummy_type": dummy_type, "n_dummy_feat": n_dummy_feat, "n_runs": n_runs,
                "nbasefeat": n_base_feat
                }
        #--------------SeedEverything--------------#
        utils.seed_everything(seed)

        #--------------Load Data wrt Variables--------------#
        if data_type == "Synthetic":
            if type == "basefeatures":
                X, Y, X_base, X_haphazard, mask = data_load.data_load_synthetic(data_name, syn_data_type, 
                                                        p_available, True, n_base_feat)
                print(X_base.shape, X_haphazard.shape, X.shape)
            else:
                X, Y, X_haphazard, mask = data_load.data_load_synthetic(data_name, syn_data_type, 
                                                        p_available, False, n_base_feat)
            result_addr = result_addr + "_prob_" + str(int(p_available*100)) + ".data"
        else:
            X, Y, X_haphazard, mask = data_load.data_load_real(data_name)
            result_addr = result_addr + ".data"
        
        print(X.shape, Y.shape, X_haphazard.shape, mask.shape, mask.shape[0]*mask.shape[1] - np.sum(mask), np.sum(Y))

        #--------------Model Configs--------------#
        param_dict["config"] = config_models.config_auxnet(data_name)
        if type != "basefeatures":
            if if_imputation:
                X_base, X_haphazard, mask = utils.prepare_data_imputation(X_haphazard, mask, imputation_type, n_impute_feat)
            if if_dummy_feat:
                X_base = utils.dummy_feat(X_haphazard.shape[0], n_dummy_feat, dummy_type = "standardnormal")
        
        print(param_dict)
        #--------------Run Model--------------#
        result = run_auxnet(X_base, X_haphazard, mask, Y, n_runs, param_dict["config"])
        print(result)
        result_dict = {"params": param_dict, "results": result}

        #--------------Store results and all variables--------------#
        
        with open(result_addr, 'wb') as file: 
            pickle.dump(result_dict, file) 