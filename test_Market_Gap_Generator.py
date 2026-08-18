import unittest
from Market_Gap_Generator import (
    format_market_gap_generator_prompt,
    run_framework_pipeline
)


class TestMarketGapGenerator(unittest.TestCase):

    def test_format_market_gap_generator_prompt(self):
        """Ensure market gap generator prompt is correctly formatted."""
        sample_pain_points = "Users struggle to find digestive-friendly herbal teas."
        prompt = format_market_gap_generator_prompt(sample_pain_points)

        self.assertIn("Market Gap Generator", prompt)
        self.assertIn("Business Opportunity Strategist", prompt)
        self.assertIn("Solution Frameworks to Apply", prompt)
        self.assertTrue(prompt.endswith(sample_pain_points))

    def test_format_market_gap_generator_prompt_empty_raises(self):
        """Ensure empty pain points summary raises ValueError."""
        with self.assertRaises(ValueError):
            format_market_gap_generator_prompt("")

        with self.assertRaises(ValueError):
            format_market_gap_generator_prompt("   ")

    def test_run_framework_pipeline(self):
        """Ensure run_framework_pipeline integrates all framework steps."""
        results = run_framework_pipeline("Herbal Remedies", "I struggle with insomnia.")

        self.assertEqual(results["segment_query"], "Herbal Remedies")
        self.assertIn("Health", results["segmentation_output"])
        self.assertIn("Herbal Remedies", results["segmentation_output"])
        self.assertIn('"Herbal Remedies"', results["reddit_query"])
        self.assertIsNotNone(results["pain_point_extractor_prompt"])
        self.assertIn("I struggle with insomnia.", results["pain_point_extractor_prompt"])

    def test_run_framework_pipeline_empty_query_raises(self):
        """Ensure empty query in pipeline raises ValueError."""
        with self.assertRaises(ValueError):
            run_framework_pipeline("")


if __name__ == "__main__":
    unittest.main()
