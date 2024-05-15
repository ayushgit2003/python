import pandas as pd


# Convert JSON data to pandas DataFrame
def match_career_goals(user_preferences_data, job_posts_data):
    print(job_posts_data)
    candidate_df = pd.DataFrame(user_preferences_data)
    candidate_df.head()
    job_posts_df = pd.DataFrame(job_posts_data)
    job_posts_df.head()

    skill_to_job_titles = {
        "Python": [
            "Web Developer",
            "Backend Developer",
            "Data Analyst",
            "Data Scientist",
        ],
        "Java": ["Web Developer", "Backend Developer", "Android Development"],
        "C++": ["Software Engineer", "Game Developer"],
        "JavaScript": ["Web Developer", "Frontend Developer", "Full Stack Developer"],
        "SQL": ["Database Administrator", "Data Analyst", "Data Scientist"],
        "HTML": ["Web Developer", "UI/UX Designer"],
        "CSS": ["Web Developer", "UI/UX Designer"],
        "React": ["Frontend Developer", "Full Stack Developer"],
        "Angular": ["Frontend Developer", "Full Stack Developer"],
        "Node.js": ["Backend Developer", "Full Stack Developer"],
        "Ruby": ["Web Developer", "Backend Developer"],
        "PHP": ["Web Developer", "Backend Developer"],
        "Swift": ["iOS Development"],
        "Kotlin": ["Android Development"],
        "Objective-C": ["iOS Development"],
        "Android Development": ["Mobile Developer"],
        "iOS Development": ["Mobile Developer"],
        "React Native": ["Mobile Developer"],
        "Flutter": ["Mobile Developer"],
        "Vue.js": ["Frontend Developer", "Full Stack Developer"],
        "MongoDB": ["Database Administrator", "Full Stack Developer"],
        "MySQL": ["Database Administrator", "Full Stack Developer"],
        "PostgreSQL": ["Database Administrator", "Full Stack Developer"],
        "SQLite": ["Database Administrator", "Mobile Developer"],
        "Firebase": ["Full Stack Developer", "Mobile Developer"],
        "Machine Learning": ["Data Scientist", "Machine Learning Engineer"],
        "Deep Learning": ["Data Scientist", "Machine Learning Engineer"],
        "Natural Language Processing": ["Data Scientist", "Machine Learning Engineer"],
        "Computer Vision": ["Data Scientist", "Machine Learning Engineer"],
        "Data Analysis": ["Data Analyst", "Data Scientist"],
        "Data Visualization": ["Data Analyst", "Data Scientist"],
        "Statistical Analysis": ["Data Analyst", "Data Scientist"],
        "Big Data": ["Big Data Engineer", "Data Scientist"],
        "Cloud Computing": ["Cloud Architect", "DevOps Engineer"],
        "AWS": ["Cloud Architect", "DevOps Engineer"],
        "Azure": ["Cloud Architect", "DevOps Engineer"],
        "Google Cloud": ["Cloud Architect", "DevOps Engineer"],
        "Docker": ["DevOps Engineer"],
        "Kubernetes": ["DevOps Engineer"],
        "CI/CD": ["DevOps Engineer"],
        "Git": ["Software Engineer", "DevOps Engineer"],
        "GitHub": ["Software Engineer", "DevOps Engineer"],
        "Bitbucket": ["Software Engineer", "DevOps Engineer"],
        "JIRA": ["Project Manager"],
        "Confluence": ["Project Manager"],
        "Agile Methodologies": ["Project Manager", "Software Engineer"],
        "Scrum": ["Project Manager", "Software Engineer"],
        "Kanban": ["Project Manager", "Software Engineer"],
        "Lean Startup": ["Product Manager"],
        "UX/UI Design": ["UI/UX Designer"],
        "TensorFlow": ["Machine Learning Engineer", "Data Scientist"],
        "PyTorch": ["Machine Learning Engineer", "Data Scientist"],
        "Scikit-learn": ["Machine Learning Engineer", "Data Scientist"],
        "Pandas": ["Data Analyst", "Data Scientist"],
        "NumPy": ["Data Analyst", "Data Scientist"],
        "Matplotlib": ["Data Analyst", "Data Scientist"],
        "Seaborn": ["Data Analyst", "Data Scientist"],
        "Keras": ["Machine Learning Engineer", "Data Scientist"],
        "Scrapy": ["Web Developer", "Backend Developer"],
        "Selenium": ["Web Developer", "Backend Developer", "QA Engineer"],
        "Flask": ["Web Developer", "Backend Developer"],
        "Django": ["Web Developer", "Backend Developer"],
        "Spring": ["Java Developer", "Backend Developer"],
        "Hibernate": ["Java Developer", "Backend Developer"],
        "JUnit": ["Java Developer", "Backend Developer"],
        "Mockito": ["Java Developer", "Backend Developer"],
        "JUnit": ["Java Developer", "Backend Developer"],
        "JUnit": ["Java Developer", "Backend Developer"],
        "Express.js": ["Node.js Developer", "Backend Developer"],
        "Hadoop": ["Big Data Engineer", "Data Scientist"],
        "Spark": ["Big Data Engineer", "Data Scientist"],
        "Hive": ["Big Data Engineer", "Data Analyst", "Data Scientist"],
        "Kafka": ["Big Data Engineer", "Data Engineer"],
        "MapReduce": ["Big Data Engineer", "Data Engineer"],
        "Flume": ["Big Data Engineer", "Data Engineer"],
        "Tableau": ["Data Analyst", "Data Scientist"],
        "Power BI": ["Data Analyst", "Data Scientist"],
        "Looker": ["Data Analyst", "Data Scientist"],
        "Jupyter": ["Data Analyst", "Data Scientist"],
        "Elasticsearch": ["DevOps Engineer", "Backend Developer"],
        "Logstash": ["DevOps Engineer"],
        "Kibana": ["DevOps Engineer"],
        "Terraform": ["DevOps Engineer"],
        "Ansible": ["DevOps Engineer"],
        "Chef": ["DevOps Engineer"],
        "Prometheus": ["DevOps Engineer"],
        "Grafana": ["DevOps Engineer"],
        "Nagios": ["DevOps Engineer"],
        "Splunk": ["DevOps Engineer"],
        "Prometheus": ["DevOps Engineer"],
        "Grafana": ["DevOps Engineer"],
        "Nagios": ["DevOps Engineer"],
        "Splunk": ["DevOps Engineer"],
        "SonarQube": ["DevOps Engineer"],
        "Jenkins": ["DevOps Engineer"],
        "TeamCity": ["DevOps Engineer"],
        "Bamboo": ["DevOps Engineer"],
        "CircleCI": ["DevOps Engineer"],
        "Travis CI": ["DevOps Engineer"],
        "CodeDeploy": ["DevOps Engineer"],
        "CloudFormation": ["DevOps Engineer"],
        "SaltStack": ["DevOps Engineer"],
        "Puppet": ["DevOps Engineer"],
        "ELK Stack": ["DevOps Engineer"],
        "Nginx": ["DevOps Engineer", "Backend Developer"],
        "Apache": ["DevOps Engineer", "Backend Developer"],
        "IIS": ["DevOps Engineer", "Backend Developer"],
        "HAProxy": ["DevOps Engineer", "Backend Developer"],
        "Postman": ["QA Engineer", "API Developer"],
        "Swagger": ["API Developer"],
        "SOAP": ["API Developer"],
        "RESTful": ["API Developer"],
        "GraphQL": ["API Developer"],
        "RESTAssured": ["API Developer"],
        "JMeter": ["Performance Engineer", "QA Engineer"],
        "LoadRunner": ["Performance Engineer", "QA Engineer"],
        "React.js": ["Frontend Developer", "Full Stack Developer"],
        "Vue.js": ["Frontend Developer", "Full Stack Developer"],
        "Angular.js": ["Frontend Developer", "Full Stack Developer"],
        "jQuery": ["Frontend Developer"],
        "Bootstrap": ["Frontend Developer"],
        "Sass": ["Frontend Developer"],
        "LESS": ["Frontend Developer"],
        "Webpack": ["Frontend Developer"],
        "Gulp": ["Frontend Developer"],
        "Grunt": ["Frontend Developer"],
        "Next.js": ["Frontend Developer", "Full Stack Developer"],
        "Nuxt.js": ["Frontend Developer", "Full Stack Developer"],
        "Flutter": ["Mobile Developer"],
        "React Native": ["Mobile Developer"],
        "Swift": ["iOS Developer"],
        "Kotlin": ["Android Developer"],
        "Objective-C": ["iOS Developer"],
        "JavaFX": ["Desktop Application Developer"],
        "Electron": ["Desktop Application Developer"],
        "PyQt": ["Desktop Application Developer"],
        "Tkinter": ["Desktop Application Developer"],
        "WPF": ["Desktop Application Developer"],
        "Unity": ["Game Developer"],
        "Unreal Engine": ["Game Developer"],
        "OpenGL": ["Game Developer"],
        "DirectX": ["Game Developer"],
        "Blender": ["3D Artist", "Game Developer"],
        "Maya": ["3D Artist", "Game Developer"],
        "ZBrush": ["3D Artist", "Game Developer"],
        "AutoCAD": ["CAD Designer"],
        "SolidWorks": ["CAD Designer"],
        "CATIA": ["CAD Designer"],
        "Revit": ["BIM Modeler"],
        "ArchiCAD": ["BIM Modeler"],
        "MicroStation": ["BIM Modeler"],
        "SketchUp": ["3D Modeler"],
        "3ds Max": ["3D Modeler"],
        "Rhino": ["3D Modeler"],
        "InDesign": ["Graphic Designer"],
        "Illustrator": ["Graphic Designer"],
        "Photoshop": ["Graphic Designer"],
        "Premiere Pro": ["Video Editor"],
        "After Effects": ["Video Editor"],
        "Final Cut Pro": ["Video Editor"],
        "DaVinci Resolve": ["Video Editor"],
        "Audacity": ["Audio Engineer"],
        "Pro Tools": ["Audio Engineer"],
        "Logic Pro": ["Audio Engineer"],
        "FL Studio": ["Audio Engineer"],
        "Ableton Live": ["Audio Engineer"],
        "MATLAB": ["Scientist", "Engineer"],
        "R": ["Data Analyst", "Data Scientist"],
        "Octave": ["Scientist", "Engineer"],
        "LabVIEW": ["Scientist", "Engineer"],
        "Stata": ["Economist", "Statistician"],
        "SPSS": ["Statistician"],
        "SAS": ["Statistician"],
        "MiniTab": ["Statistician"],
        "JMP": ["Statistician"],
    }

    def preprocess_job_post_data(job_posts_df):
        job_titles_to_ids = {}  # Dictionary to store job titles and associated job IDs
        for index, row in job_posts_df.iterrows():
            job_id = row["jobId"]
            job_title = row["jobTitle"]
            if job_title not in job_titles_to_ids:
                job_titles_to_ids[job_title] = (
                    set()
                )  # Initialize set of job IDs for each job title
            job_titles_to_ids[job_title].add(job_id)
        return job_titles_to_ids

    def find_matching_jobs(candidate_df, job_posts_df):
        user_to_job_ids = {}  # Dictionary to store user ID and associated job IDs
        job_titles_to_ids = preprocess_job_post_data(job_posts_df)

        for index, user in candidate_df.iterrows():
            user_id = user["userId"]
            user_to_job_ids[user_id] = set()  # Initialize set of job IDs for each user

            # Split skills and convert to set for efficient lookup
            user_skills = set(user["skills"])
            user_experience_level = user["experienceLevel"]
            user_locations = set(user["locations"])

            # Match skills with the skills in the skill_to_job_titles dictionary
            for skill in user_skills:
                # Check job titles associated with the skill
                associated_job_titles = user["jobTitles"]
                # Check if any job title associated with the skill exists in the job post data
                for job_title in associated_job_titles:
                    if job_title in job_titles_to_ids:
                        # Check if the job post matches user's experience level and location
                        for job_id in job_titles_to_ids[job_title]:
                            job_post = job_posts_df[
                                job_posts_df["jobId"] == job_id
                            ].iloc[0]
                            if (
                                job_post["jobExperienceLevel"] == user_experience_level
                                and job_post["jobLocation"] in user_locations
                            ):
                                user_to_job_ids[user_id].add(job_id)

        # Convert the dictionary to a DataFrame
        matched_jobs_df = pd.DataFrame(
            user_to_job_ids.items(), columns=["userId", "jobIds"]
        )

        return matched_jobs_df

    # Example usage
    matched_jobs_df = find_matching_jobs(candidate_df, job_posts_df)
    return matched_jobs_df
