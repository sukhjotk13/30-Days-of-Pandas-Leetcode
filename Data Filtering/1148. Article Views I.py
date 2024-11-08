import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df=views[views['author_id']==views['viewer_id']]
    df1=df[['author_id']].drop_duplicates().rename(columns={'author_id':'id'})
    return df1.sort_values(by='id',ascending=True,inplace=False) 
