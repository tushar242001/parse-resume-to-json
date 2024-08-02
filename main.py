import openai
import json

# Set up your OpenAI API key
openai.api_key = 'your-api-key'

# Define the resume text
resume_text = """
[Insert Resume Here]
"""

# Define the prompt
prompt = f"""
Please parse the following resume and provide the information in JSON format. The JSON should include the following fields: "Name", "Contact Information", "Education", "Experience", "Skills", and "Projects". 

Here is the resume:

{resume_text}
"""

# Call the OpenAI API with the prompt
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  max_tokens=1000
)

# Extract the JSON from the response
parsed_resume = response.choices[0].text.strip()

# Convert the extracted text to JSON
resume_json = json.loads(parsed_resume)

# Print the JSON
print(json.dumps(resume_json, indent=2))
