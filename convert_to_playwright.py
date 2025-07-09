def step_to_code(step: str) -> str:
    step = step.lower()
    if "job description" in step:
        return 'await page.getByLabel("Job Description").fill("Sample JD");'
    elif "ai suggests questions" in step:
        return 'await page.getByRole("button", { name: "Generate Questions" }).click();'
    elif "customize questions" in step:
        return 'await page.getByLabel("Question 1").fill("Updated question");'
    elif "establish interview" in step:
        return 'await page.getByRole("button", { name: "Create Interview" }).click();'
    else:
        return f'// TODO: Implement "{step}"'

def generate_playwright_test(test_case):
    steps_code = "\n  ".join([step_to_code(step) for step in test_case["steps"]])
    return f"""
test('{test_case["title"]}', async ({{ page }}) => {{
  await page.goto('https://your-app-url.com');
  {steps_code}
  await expect(page).toContainText('{test_case["expected"]}');
}});
"""