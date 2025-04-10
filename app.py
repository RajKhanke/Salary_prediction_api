from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import uvicorn

# Initialize FastAPI app
app = FastAPI(title="Salary Prediction API")

# Load the pre-trained model (ensure that 'salary.pkl' is in the same directory)
model = joblib.load("salary.pkl")

# Complete encoding dictionaries used during training
gender_encoding = {
    'Female': 0,
    'Male': 1
}

education_encoding = {
    "Bachelor's": 0,
    "Master's": 1,
    "PhD": 2
}

job_title_encoding = {
    'Account Manager': 0,
    'Accountant': 1,
    'Administrative Assistant': 2,
    'Business Analyst': 3,
    'Business Development Manager': 4,
    'Business Intelligence Analyst': 5,
    'CEO': 6,
    'Chief Data Officer': 7,
    'Chief Technology Officer': 8,
    'Content Marketing Manager': 9,
    'Copywriter': 10,
    'Creative Director': 11,
    'Customer Service Manager': 12,
    'Customer Service Rep': 13,
    'Customer Service Representative': 14,
    'Customer Success Manager': 15,
    'Customer Success Rep': 16,
    'Data Analyst': 17,
    'Data Entry Clerk': 18,
    'Data Scientist': 19,
    'Digital Content Producer': 20,
    'Digital Marketing Manager': 21,
    'Director': 22,
    'Director of Business Development': 23,
    'Director of Engineering': 24,
    'Director of Finance': 25,
    'Director of HR': 26,
    'Director of Human Capital': 27,
    'Director of Human Resources': 28,
    'Director of Marketing': 29,
    'Director of Operations': 30,
    'Director of Product Management': 31,
    'Director of Sales': 32,
    'Director of Sales and Marketing': 33,
    'Event Coordinator': 34,
    'Financial Advisor': 35,
    'Financial Analyst': 36,
    'Financial Manager': 37,
    'Graphic Designer': 38,
    'HR Generalist': 39,
    'HR Manager': 40,
    'Help Desk Analyst': 41,
    'Human Resources Director': 42,
    'IT Manager': 43,
    'IT Support': 44,
    'IT Support Specialist': 45,
    'Junior Account Manager': 46,
    'Junior Accountant': 47,
    'Junior Advertising Coordinator': 48,
    'Junior Business Analyst': 49,
    'Junior Business Development Associate': 50,
    'Junior Business Operations Analyst': 51,
    'Junior Copywriter': 52,
    'Junior Customer Support Specialist': 53,
    'Junior Data Analyst': 54,
    'Junior Data Scientist': 55,
    'Junior Designer': 56,
    'Junior Developer': 57,
    'Junior Financial Advisor': 58,
    'Junior Financial Analyst': 59,
    'Junior HR Coordinator': 60,
    'Junior HR Generalist': 61,
    'Junior Marketing Analyst': 62,
    'Junior Marketing Coordinator': 63,
    'Junior Marketing Manager': 64,
    'Junior Marketing Specialist': 65,
    'Junior Operations Analyst': 66,
    'Junior Operations Coordinator': 67,
    'Junior Operations Manager': 68,
    'Junior Product Manager': 69,
    'Junior Project Manager': 70,
    'Junior Recruiter': 71,
    'Junior Research Scientist': 72,
    'Junior Sales Representative': 73,
    'Junior Social Media Manager': 74,
    'Junior Social Media Specialist': 75,
    'Junior Software Developer': 76,
    'Junior Software Engineer': 77,
    'Junior UX Designer': 78,
    'Junior Web Designer': 79,
    'Junior Web Developer': 80,
    'Marketing Analyst': 81,
    'Marketing Coordinator': 82,
    'Marketing Manager': 83,
    'Marketing Specialist': 84,
    'Network Engineer': 85,
    'Office Manager': 86,
    'Operations Analyst': 87,
    'Operations Director': 88,
    'Operations Manager': 89,
    'Principal Engineer': 90,
    'Principal Scientist': 91,
    'Product Designer': 92,
    'Product Manager': 93,
    'Product Marketing Manager': 94,
    'Project Engineer': 95,
    'Project Manager': 96,
    'Public Relations Manager': 97,
    'Recruiter': 98,
    'Research Director': 99,
    'Research Scientist': 100,
    'Sales Associate': 101,
    'Sales Director': 102,
    'Sales Executive': 103,
    'Sales Manager': 104,
    'Sales Operations Manager': 105,
    'Sales Representative': 106,
    'Senior Account Executive': 107,
    'Senior Account Manager': 108,
    'Senior Accountant': 109,
    'Senior Business Analyst': 110,
    'Senior Business Development Manager': 111,
    'Senior Consultant': 112,
    'Senior Data Analyst': 113,
    'Senior Data Engineer': 114,
    'Senior Data Scientist': 115,
    'Senior Engineer': 116,
    'Senior Financial Advisor': 117,
    'Senior Financial Analyst': 118,
    'Senior Financial Manager': 119,
    'Senior Graphic Designer': 120,
    'Senior HR Generalist': 121,
    'Senior HR Manager': 122,
    'Senior HR Specialist': 123,
    'Senior Human Resources Coordinator': 124,
    'Senior Human Resources Manager': 125,
    'Senior Human Resources Specialist': 126,
    'Senior IT Consultant': 127,
    'Senior IT Project Manager': 128,
    'Senior IT Support Specialist': 129,
    'Senior Manager': 130,
    'Senior Marketing Analyst': 131,
    'Senior Marketing Coordinator': 132,
    'Senior Marketing Director': 133,
    'Senior Marketing Manager': 134,
    'Senior Marketing Specialist': 135,
    'Senior Operations Analyst': 136,
    'Senior Operations Coordinator': 137,
    'Senior Operations Manager': 138,
    'Senior Product Designer': 139,
    'Senior Product Development Manager': 140,
    'Senior Product Manager': 141,
    'Senior Product Marketing Manager': 142,
    'Senior Project Coordinator': 143,
    'Senior Project Manager': 144,
    'Senior Quality Assurance Analyst': 145,
    'Senior Research Scientist': 146,
    'Senior Researcher': 147,
    'Senior Sales Manager': 148,
    'Senior Sales Representative': 149,
    'Senior Scientist': 150,
    'Senior Software Architect': 151,
    'Senior Software Developer': 152,
    'Senior Software Engineer': 153,
    'Senior Training Specialist': 154,
    'Senior UX Designer': 155,
    'Social Media Manager': 156,
    'Social Media Specialist': 157,
    'Software Developer': 158,
    'Software Engineer': 159,
    'Software Manager': 160,
    'Software Project Manager': 161,
    'Strategy Consultant': 162,
    'Supply Chain Analyst': 163,
    'Supply Chain Manager': 164,
    'Technical Recruiter': 165,
    'Technical Support Specialist': 166,
    'Technical Writer': 167,
    'Training Specialist': 168,
    'UX Designer': 169,
    'UX Researcher': 170,
    'VP of Finance': 171,
    'VP of Operations': 172,
    'Web Developer': 173
}


# Define Pydantic model for input (allows Swagger UI to display fields)
class SalaryInput(BaseModel):
    Age: int
    Gender: str
    Education_Level: str
    Job_Title: str
    Years_of_Experience: int


@app.get("/")
def read_root():
    return {"message": "Welcome to the Salary Prediction API!"}


@app.post("/predict")
def predict_salary(input_data: SalaryInput):
    # Validate numeric fields
    if input_data.Age < 0 or input_data.Years_of_Experience < 0:
        raise HTTPException(status_code=400,
                            detail="Age and Years_of_Experience must be 0 or positive.")

    # Validate categorical fields
    if input_data.Gender not in gender_encoding:
        raise HTTPException(status_code=400, detail="Invalid Gender provided.")
    if input_data.Education_Level not in education_encoding:
        raise HTTPException(status_code=400, detail="Invalid Education_Level provided.")
    if input_data.Job_Title not in job_title_encoding:
        raise HTTPException(status_code=400, detail="Invalid Job_Title provided.")

    # Encode the input data based on training encoding dictionaries
    gender_encoded = gender_encoding[input_data.Gender]
    education_encoded = education_encoding[input_data.Education_Level]
    job_encoded = job_title_encoding[input_data.Job_Title]

    # Prepare DataFrame with expected column names and order
    df = pd.DataFrame({
        'Age': [input_data.Age],
        'Gender': [gender_encoded],
        'Education Level': [education_encoded],
        'Job Title': [job_encoded],
        'Years of Experience': [input_data.Years_of_Experience]
    })

    # Predict salary using the loaded model
    prediction = model.predict(df)[0]

    return {
        "message": "Salary prediction successful",
        "predicted_salary_rs": f"Rs {prediction:,.2f}"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
