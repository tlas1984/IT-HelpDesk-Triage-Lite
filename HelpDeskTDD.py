# Assignment # Course: Software Engineering
# System: IT Help Desk Triage Lite
# Group: Group 6
#
# Group Members:
# Tracie Laster
# Jedidiah Money

import unittest
from datetime import datetime


# Simple Help Desk System used for testing
class HelpDeskSystem:

    def __init__(self):
        # Simple list used as ticket storage
        self.tickets = []

    # SR-03: Assign priority based on category and urgency
    def create_ticket(self, category, issue_info, urgency):

        # Category base values from refined SR-03 logic
        category_values = {
            "Network": 3,
            "Software": 2,
            "Hardware": 2,
            "General": 1
        }

        # Urgency modifier from refined priority logic
        urgency_values = {
            "High": 1,
            "Low": 0
        }

        # Calculate numeric priority instead of returning hardcoded text only
        priority = category_values.get(category, 1) + urgency_values.get(urgency, 0)

        # Create ticket data so tests can validate actual system behavior
        ticket = {
            "category": category,
            "issue_info": issue_info,
            "urgency": urgency,
            "priority": priority,
            "timestamp": datetime.now()
        }

        self.tickets.append(ticket)

        return "Incident created", priority

    # SR-04 / SR-07: Check whether two ticket descriptions are duplicates
    def detect_duplicate(self, existing_ticket, new_ticket):
        return existing_ticket.lower() == new_ticket.lower()

    # SR-06: Update ticket status using valid status values
    def update_status(self, status):
        valid_statuses = ["Open", "In Progress", "Resolved"]

        if status in valid_statuses:
            return status

        return "Invalid status"

    # SR-07: Assign queue based on ticket category
    def assign_queue(self, category):
        if category == "Network":
            return "Network Support"

        return "General Support"

    # SR-08: Generate report only for supported formats
    def generate_report(self, output_format):
        valid_formats = ["pdf", "xlsx", "csv"]

        if output_format.lower() in valid_formats:
            return "Report generated"

        return "Invalid report format"


class TestHelpDeskSystem(unittest.TestCase):

    # Setup runs before every test
    def setUp(self):
        self.system = HelpDeskSystem()

    # Test Case: SR03 Priority Assignment (Happy Path)
    # Purpose: Verify High urgency with Network category assigns highest priority score
    # Traceability: (SR-03, PY-PRIORITY-01)
    def test_SR03_priority_assignment_happy(self):

        message, priority = self.system.create_ticket(
            "Network",
            "Internet down",
            "High"
        )

        self.assertEqual(message, "Incident created")
        self.assertEqual(priority, 4)

    # Test Case: SR03 Priority Assignment (Edge Case)
    # Purpose: Verify Low urgency with General category assigns lowest priority score
    # Traceability: (SR-03, PY-PRIORITY-01)
    def test_SR03_priority_assignment_edge(self):

        message, priority = self.system.create_ticket(
            "General",
            "Slow internet",
            "Low"
        )

        self.assertEqual(message, "Incident created")
        self.assertEqual(priority, 1)

    # Test Case: SR04/SR07 Duplicate Detection (Happy Path)
    # Purpose: Verify matching ticket descriptions can be identified as duplicates
    # Traceability: (SR-07, PY-VALID-01)
    def test_SR04_duplicate_detection_happy(self):

        result = self.system.detect_duplicate(
            "Internet down",
            "Internet down"
        )

        self.assertTrue(result)

    # Test Case: SR04/SR07 Duplicate Detection (Edge Case)
    # Purpose: Verify different ticket descriptions are not duplicates
    # Traceability: (SR-07, PY-VALID-01)
    def test_SR04_duplicate_detection_edge(self):

        result = self.system.detect_duplicate(
            "Internet down",
            "Printer not working"
        )

        self.assertFalse(result)

    # Test Case: SR06 Status Update (Happy Path)
    # Purpose: Verify valid ticket status can be updated
    # Traceability: (SR-06, PY-TIME-01)
    def test_SR06_status_update_happy(self):

        status = self.system.update_status("Resolved")

        self.assertEqual(status, "Resolved")

    # Test Case: SR06 Status Update (Edge Case)
    # Purpose: Verify invalid status values are rejected
    # Traceability: (SR-06, PY-TIME-01)
    def test_SR06_status_update_edge(self):

        status = self.system.update_status("Closed")

        self.assertEqual(status, "Invalid status")

    # Test Case: SR07 Queue Assignment (Happy Path)
    # Purpose: Verify Network tickets go to Network Support
    # Traceability: (SR-07, PY-VALID-01)
    def test_SR07_queue_assignment_happy(self):

        queue = self.system.assign_queue("Network")

        self.assertEqual(queue, "Network Support")

    # Test Case: SR07 Queue Assignment (Edge Case)
    # Purpose: Verify non-Network categories go to General Support
    # Traceability: (SR-07, PY-VALID-01)
    def test_SR07_queue_assignment_edge(self):

        queue = self.system.assign_queue("Hardware")

        self.assertEqual(queue, "General Support")

    # Test Case: SR08 Report Generation (Happy Path)
    # Purpose: Verify system generates a report for a valid format
    # Traceability: (SR-08, PY-OUTPUT-02)
    def test_SR08_report_generation_happy(self):

        report_status = self.system.generate_report("pdf")

        self.assertEqual(report_status, "Report generated")

    # Test Case: SR08 Report Generation (Edge Case)
    # Purpose: Verify invalid report format is rejected
    # Traceability: (SR-08, PY-OUTPUT-02)
    def test_SR08_report_generation_edge(self):

        report_status = self.system.generate_report("doc")

        self.assertEqual(report_status, "Invalid report format")


if __name__ == "__main__":
    unittest.main()