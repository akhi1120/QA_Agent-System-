# generate_test_cases.py
import os
import json
import re
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client safely
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_transcript(filename="transcript.txt"):
    """Read transcript from file"""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def generate_test_cases(transcript):
    """Generate test cases using AI"""
    prompt = f"""
    You are QAgenie, an AI that creates test cases from videos.
    Create a JSON array of test cases where each test case has:
    - title: Test name
    - description: What we're testing
    - steps: Array of steps
    - expected: Expected result
    - type: functional/edge/accessibility

    Return ONLY valid JSON. Do not include any additional text or markdown formatting.

    Video transcript:
    {transcript}
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    
    return response.choices[0].message.content

def extract_json(content):
    """Extract JSON from the AI response"""
    try:
        # Try to find JSON in markdown code blocks
        json_match = re.search(r'```json\n(.*?)\n```', content, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(1))
        
        # Try to find raw JSON
        json_match = re.search(r'(\[\s*\{.*?\}\s*\])', content, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(1))
        
        # Try direct parse as last resort
        return json.loads(content)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        print("Raw content received:")
        print(content)
        return None

def save_test_cases(content, filename="test_cases.json"):
    """Save test cases to file"""
    test_cases = extract_json(content)
    if not test_cases:
        print("No valid test cases could be extracted")
        return
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(test_cases, f, indent=2)
    print(f"Saved {len(test_cases)} test cases to {filename}")

if __name__ == "__main__":
    transcript = read_transcript()
    if transcript:
        test_cases = generate_test_cases(transcript)
        save_test_cases(test_cases)
    else:
        print("No transcript found. Please run data_ingestion.py first.")