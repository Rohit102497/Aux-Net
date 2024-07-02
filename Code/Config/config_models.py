# Model Configs
import numpy as np
from Utils.utils import dummy_feat, impute_data

# --------- Aux-Net ------------
def config_auxnet(data_name):
    config_dict = {}

    params_list = {
        "wpbc":        {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [.001]},
        "ionosphere":  {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [.001]},
        "wdbc":        {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [.01]},
        "australian":  {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [.01]},
        "wbc":         {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [.001]},
        "diabetes_f":  {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [.05]},
        "crowdsense_c3":{"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [0.001]},
        "crowdsense_c5":{"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [0.001]},
        "german":      {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [.001]},
        "ipd":         {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [.001]},
        "svmguide3":   {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [.1]},
        "krvskp":      {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [.001]},
        "spambase":    {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [.005]},
        "spamassasin": {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [0.01]},
        "magic04":     {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [.5]},
        "imdb":        {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [0.01]},
        "a8a":         {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [0.01]},
        "diabetes_us": {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [0.05]},
        "susy":        {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [0.05]},
        "higgs":       {"no_of_base_layers": [5], "no_of_end_layers": [5], "nodes_in_each_layer": [50], 
                        "b": [0.99], "s": [0.2], "lr": [0.05]},
    }
    
    config_dict = params_list[data_name]

    return config_dict