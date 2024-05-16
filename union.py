from pymongo import MongoClient
from bson.objectid import ObjectId
import pandas as pd
from all_match import all_match

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

    # print("Combined DataFrame:")
    # print(combined_df)

    # Connect to MongoDB
    client = MongoClient("mongodb+srv://ayush:user@cluster0.f2dpvrq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client['test']  # Change 'your_database' to your actual database name
    collection = db['results']  # Change 'your_collection' to your actual collection name

    # Convert DataFrame to dictionary and update MongoDB
    records = combined_df.to_dict(orient='records')
    for record in records:
        user_id = record['userId']
        existing_doc = collection.find_one({"userId": user_id})

        # If user document already exists, update it
        if existing_doc:
            new_job_ids = list(record['jobIds'])  # Convert jobIds from set to list
            collection.update_one(
                
                {"_id": existing_doc["_id"]},
                {"$addToSet": {"jobIds": {"$each": new_job_ids}}}
            )
        else:
            # Otherwise, insert a new document
            record['jobIds'] = list(record['jobIds'])  # Convert jobIds from set to list
            collection.insert_one(record)

    print("Combined DataFrame stored in MongoDB.")
