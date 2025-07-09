import { test, expect } from '@playwright/test';

test('Create Interview with Job Description', async ({ page }) => {
  await page.goto('https://your-app-url.com');
  // Implement steps from your JSON
  await page.getByLabel('Job Description').fill('Sample job description');
  await page.getByRole('button', { name: 'Generate Questions' }).click();
  await expect(page.getByText('Interview created successfully')).toBeVisible();
});

