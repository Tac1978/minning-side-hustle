import unittest
from Pain_Point_Extractor import format_pain_point_extractor_prompt, format_reddit_query


class TestPainPointExtractor(unittest.TestCase):

    def test_format_reddit_query(self):
        """Ensure search query is formatted properly."""
        query = format_reddit_query("Herbal Remedies")
        self.assertIn('"Herbal Remedies"', query)
        self.assertIn("site:reddit.com", query)

    def test_format_pain_point_extractor_prompt(self):
        """Ensure prompt template formats and appends Reddit data correctly."""
        sample_data = "I tried 5 different remedies and none of them worked."
        prompt = format_pain_point_extractor_prompt(sample_data)

        self.assertIn("Pain Point Extractor", prompt)
        self.assertIn("Market Research Analyst", prompt)
        self.assertIn("Include the Reddit data below:", prompt)
        self.assertTrue(prompt.endswith(sample_data))

    def test_format_pain_point_extractor_prompt_empty_raises(self):
        """Ensure empty reddit data raises ValueError."""
        with self.assertRaises(ValueError):
            format_pain_point_extractor_prompt("")

        with self.assertRaises(ValueError):
            format_pain_point_extractor_prompt("   ")


if __name__ == "__main__":
    unittest.main()
