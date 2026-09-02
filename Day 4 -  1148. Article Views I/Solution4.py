import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where author_id is equal to viewer_id
    df = views[views['author_id'] == views['viewer_id']]
    
    # Extract unique author_ids and drop duplicates
    df = df[['author_id']].drop_duplicates()
    # Rename column to 'id'
    df = df.rename(columns={'author_id': 'id'})
    
    # Sort by 'id' in ascending order
    df = df.sort_values(by='id', ascending=True)
    
    return df

