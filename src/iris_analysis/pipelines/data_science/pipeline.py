from kedro.pipeline import Pipeline,node
from .Nodes.preprocess import limit_data_size 
from .Nodes.preprocess import rename_columns 
from .Nodes.preprocess import clean_data

def Process_pipeline():
    return Pipeline(
        [
            node(
                func = limit_data_size,
                inputs = ["tripData" , "params:limit_size"],
                # input = ["tripData" , "parametrs"],    parameters["limit_size"]
                outputs="yellow_tripDataLimited",
                name="limit_data_size"
            ),
             node(
                func = rename_columns,
                inputs = ["yellow_tripDataLimited"],
                 #input = ["yellow_tripData" , "parametrs"],    parameters["limit_size"]
                outputs="yellow_tripDataRenamed",
                 name="rename_columns"
            ),
              node(
                func = clean_data,
                inputs = ["yellow_tripData", "params:maxLat", "params:maxLong"],
                # input = ["yellow_tripData" , "parametrs"],    parameters["limit_size"]
                outputs="yellow_tripDataCleaned",
                 name="clean_data"
           ),

        ]
    )