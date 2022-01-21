from kedro.pipeline import node, Pipeline
from .nodes.preprocess import clean_raw_data, preprocess_data, normalize_tweets

def create_pipeline(**kwargs):
    
    return Pipeline(
        [
            node(
                clean_raw_data,
                inputs='tweet_data',
                outputs='cleaned_data'
            ),
            node(
                preprocess_data,
                inputs='cleaned_data',
                outputs='processed_data'
            ),
            node(
                 normalize_tweets,
                inputs="processed_data",
                outputs="normalized_data"
               
            ),
        ]
    ) 