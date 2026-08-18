import unittest
from segmentation import MARKET_DATA, format_segmentation, filter_segmentation, get_segmentation_output


class TestSegmentation(unittest.TestCase):

    def test_core_markets_exist(self):
        """Ensure all three core markets are present in the taxonomy."""
        expected_markets = {"Health", "Wealth", "Relationships"}
        self.assertEqual(set(MARKET_DATA.keys()), expected_markets)

    def test_hierarchy_depth_and_structure(self):
        """Ensure all branches follow Core Market -> Category -> Subcategory -> Niche -> List of Sub-Niches."""
        for market, categories in MARKET_DATA.items():
            self.assertIsInstance(categories, dict, f"Categories in {market} should be a dict")
            self.assertTrue(len(categories) > 0, f"Market {market} has no categories")

            for cat, subcategories in categories.items():
                self.assertIsInstance(subcategories, dict, f"Subcategories in {cat} should be a dict")
                self.assertTrue(len(subcategories) > 0, f"Category {cat} has no subcategories")

                for subcat, niches in subcategories.items():
                    self.assertIsInstance(niches, dict, f"Niches in {subcat} should be a dict")
                    self.assertTrue(len(niches) > 0, f"Subcategory {subcat} has no niches")

                    for niche, subniches in niches.items():
                        self.assertIsInstance(subniches, list, f"Sub-niches in {niche} should be a list")
                        self.assertTrue(len(subniches) > 0, f"Niche {niche} has no sub-niches")
                        for subniche in subniches:
                            self.assertIsInstance(subniche, str)

    def test_entries_uniqueness(self):
        """Ensure all entries across categories, subcategories, niches, and sub-niches are unique."""
        all_entries = set()

        def check_and_add(entry):
            self.assertNotIn(entry, all_entries, f"Duplicate entry found: {entry}")
            all_entries.add(entry)

        for market, categories in MARKET_DATA.items():
            for cat, subcategories in categories.items():
                check_and_add(cat)
                for subcat, niches in subcategories.items():
                    check_and_add(subcat)
                    for niche, subniches in niches.items():
                        check_and_add(niche)
                        for subniche in subniches:
                            check_and_add(subniche)

    def test_formatting_output(self):
        """Ensure format_segmentation produces correct bullet indentation."""
        formatted = format_segmentation({"Health": {"Fitness": {"Cardio": {"Running": ["Marathon"]}}}})
        expected = (
            "- Health\n"
            "  - Fitness\n"
            "    - Cardio\n"
            "      - Running\n"
            "        - Marathon"
        )
        self.assertEqual(formatted, expected)

    def test_filter_focused_query(self):
        """Test filtering by query."""
        res = filter_segmentation("Alternative Medicine")
        self.assertIn("Health", res)
        self.assertIn("Physical Health & Fitness", res["Health"])
        self.assertIn("Alternative Medicine", res["Health"]["Physical Health & Fitness"])
        # Should not include unrelated core markets
        self.assertNotIn("Wealth", res)
        self.assertNotIn("Relationships", res)

    def test_get_segmentation_output_no_match(self):
        """Test output when query matches nothing."""
        output = get_segmentation_output("nonexistent_query_xyz")
        self.assertIn("No market segmentation found matching query", output)


if __name__ == "__main__":
    unittest.main()
