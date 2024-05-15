import pandas as pd
from sklearn.metrics import jaccard_score

def match_skills(user_preferences_data,job_posts_data):
    result_data = {}
    candidate_df = pd.DataFrame(user_preferences_data)
    candidate_df.head()
    job_posts_df = pd.DataFrame(job_posts_data)
    job_posts_df.head()
    
    result_data = {}

    # Iterate over each candidate's preferences
    for _, candidate_row in candidate_df.iterrows():
        user_id = candidate_row['userId']
        user_locations = set(candidate_row['locations'])
        user_experience_level = candidate_row['experienceLevel']

        # Find matching job posts for the candidate's experience level and location
        matching_jobs = []
        for _, job_row in job_posts_df.iterrows():
            job_id = job_row['jobId']
            job_location = job_row['jobLocation']
            job_experience_level = job_row['jobExperienceLevel']

            if user_experience_level == job_experience_level and any(location in user_locations for location in job_location.split(', ')):
                matching_jobs.append(job_id)

        # Append the user ID and matching job IDs to the result dictionary
        result_data[user_id] = matching_jobs

    # Create a DataFrame from the result dictionary
    matched_1_df = pd.DataFrame(result_data.items(), columns=['userId', 'jobIds'])

     

    # Sample data for demonstration
    abc_df = matched_1_df
    # print(abc_df)

    candidate_df = pd.DataFrame(user_preferences_data)
    job_posts_df = pd.DataFrame(job_posts_data)

    # Function to calculate Jaccard similarity score
    def calculate_similarity(user_skills, job_skills):
        intersection_size = len(user_skills.intersection(job_skills))
        union_size = len(user_skills.union(job_skills))
        return intersection_size / union_size if union_size > 0 else 0

    # Initialize an empty list to store the results
    result_data = []

    # Iterate through each row in abc_df
    for index, row in abc_df.iterrows():
        user_id = row['userId']
        matched_job_ids = set()
        
        # Get user's skills
        user_skills = set(candidate_df[candidate_df['userId'] == user_id]['skills'].iloc[0])
        
        # Iterate through each job ID associated with the current user
        for job_id in row['jobIds']:
            # Get job's skills
            job_skills = set(job_posts_df[job_posts_df['jobId'] == int(job_id)]['jobSkills'].iloc[0])
            
            # Calculate Jaccard similarity score
            score = calculate_similarity(user_skills, job_skills)
            
            # If score is positive, add the job ID to the result list
            if score > 0:
                matched_job_ids.add(job_id)
        
        # Add a row to the result DataFrame
        result_data.append({'userId': user_id, 'jobIds': matched_job_ids})

    # Create a DataFrame from the result list
    result_df = pd.DataFrame(result_data)
    # print(result_df)
    return result_df