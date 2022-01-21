from kedro.pipeline import Pipeline,node
from .nodes.model import split_data
from .nodes.model import vectorize_text 
from .nodes.model import train_model
from .nodes.model import evaluate_model



def create_pipeline(**kwargs):
    
    return Pipeline(
        [
            node(
                split_data,
                inputs=['processed_data', 'parameters'],
                outputs=['X_train', 'X_test', 'y_train', 'y_test']
            ),
            node(
                vectorize_text,
                inputs=['X_train', 'X_test', 'parameters'],
                outputs=['X_train_vec', 'X_test_vec']
            ),
            node(
                train_model,
                inputs=['X_train_vec', 'y_train', 'parameters'],
                outputs='model'
            ),
            node(
                evaluate_model,
                inputs=['X_test_vec', 'y_test', 'model'],
                outputs=None
            )
        ]
    )