import pandas as pd
from all_match import all_match
from pymongo import MongoClient

def union(items, jobs):
    matched_result = all_match(items, jobs)

    # Create DataFrames
    df1 = pd.DataFrame(matched_result["user"])
    df2 = pd.DataFrame(matched_result["skills"])
    df3 = pd.DataFrame(matched_result["goals"])

    # Initialize a dictionary to store the combined results
    combined_result = {'userId': [], 'jobIds': []}

    # Get unique user IDs from all DataFrames
    all_user_ids = set(df1['userId']).union(set(df2['userId'])).union(set(df3['userId']))

    # Iterate through unique user IDs and take the union of job IDs from all DataFrames
    for user_id in all_user_ids:
        job_ids_1 = set()
        job_ids_2 = set()
        job_ids_3 = set()

        if user_id in df1['userId'].values:
            job_ids_1 = df1[df1['userId'] == user_id]['jobIds'].iloc[0]

        if user_id in df2['userId'].values:
            job_ids_2 = df2[df2['userId'] == user_id]['jobIds'].iloc[0]

        if user_id in df3['userId'].values:
            job_ids_3 = df3[df3['userId'] == user_id]['jobIds'].iloc[0]

        combined_job_ids = set(job_ids_1).union(job_ids_2).union(job_ids_3)

        combined_result['userId'].append(user_id)
        combined_result['jobIds'].append(combined_job_ids)

    # Create a new DataFrame with the combined results
    combined_df = pd.DataFrame(combined_result)

    print("Combined DataFrame:")
    print(combined_df)
    
    client = MongoClient("mongodb+srv://ayush:user@cluster0.f2dpvrq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client['test']  # Change 'your_database' to your actual database name
    collection = db['results']  # Change 'your_collection' to your actual collection name

    # Convert DataFrame to dictionary and insert into MongoDB
    records = combined_df.to_dict(orient='records')
    for record in records:
        record['jobIds'] = list(record['jobIds'])  # Convert jobIds from set to list
    collection.insert_many(records)

    print("Combined DataFrame stored in MongoDB.")