import pandas as pd

# Convert JSON data to pandas DataFrame
def process_user_preferences(user_preferences_data,job_posts_data):
    # print(job_posts_data)
    candidate_df = pd.DataFrame(user_preferences_data)
    candidate_df.head()
    job_posts_df = pd.DataFrame(job_posts_data)
    job_posts_df.head()

# Initialize an empty dictionary to store the results
    result_data = {}

# Iterate over each candidate's preferences
    for _, candidate_row in candidate_df.iterrows():
        user_id = candidate_row["userId"]
        user_locations = set(candidate_row["locations"])
        user_experience_level = candidate_row["experienceLevel"]

    # Find matching job posts for the candidate's experience level and location
    matching_jobs = []
    for _, job_row in job_posts_df.iterrows():
        job_id = job_row["jobId"]
        job_location = job_row["jobLocation"]
        job_experience_level = job_row["jobExperienceLevel"]

        if user_experience_level == job_experience_level and any(
            location in user_locations for location in job_location.split(", ")
        ):
            matching_jobs.append(job_id)

    # Append the user ID and matching job IDs to the result dictionary
    result_data[user_id] = matching_jobs

# Create a DataFrame from the result dictionary
    matched_1_df = pd.DataFrame(result_data.items(), columns=["userId", "jobIds"])

    return matched_1_df
