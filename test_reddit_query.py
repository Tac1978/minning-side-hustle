import unittest
from reddit_query import format_reddit_query, REDDIT_QUERY_TEMPLATE


class TestRedditQuery(unittest.TestCase):

    def test_format_reddit_query_basic(self):
        """Ensure market segment is correctly substituted into the query template."""
        market_segment = "Herbal Remedies"
        result = format_reddit_query(market_segment)
        self.assertIn('"Herbal Remedies"', result)
        self.assertTrue(result.startswith('"Herbal Remedies" ('))
        self.assertTrue(result.endswith(')'))

    def test_format_reddit_query_whitespace_stripping(self):
        """Ensure leading/trailing whitespace is stripped from input."""
        result = format_reddit_query("  Alternative Medicine   ")
        self.assertTrue(result.startswith('"Alternative Medicine" ('))

    def test_format_reddit_query_empty_raises_value_error(self):
        """Ensure empty or whitespace-only strings raise ValueError."""
        with self.assertRaises(ValueError):
            format_reddit_query("")

        with self.assertRaises(ValueError):
            format_reddit_query("   ")

    def test_format_reddit_query_template_structure(self):
        """Ensure query includes key search parameters from FRAMEWORK.md."""
        result = format_reddit_query("Kettlebell Workouts")
        self.assertIn("site:reddit.com", result)
        self.assertIn("inurl:comments|inurl:thread", result)
        self.assertIn('"pain point"', result)
        self.assertIn('"my biggest struggle"', result)


if __name__ == "__main__":
    unittest.main()
