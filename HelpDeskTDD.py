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

        category_values = {
            "Network": 3,
            "Software": 2,
            "Hardware": 2,
            "General": 1
        }

        urgency_values = {
            "High": 1,
            "Low": 0
        }

        priority = category_values.get(category, 1) + urgency_values.get(urgency, 0)

        ticket = {
            "category": category,
            "issue_info": issue_info,
            "urgency": urgency,
            "priority": priority,
            "timestamp": datetime.now()
        }

        self.tickets.append(ticket)

        return "Incident created", priority

    # SR-04 / SR-07: Duplicate detection
    def detect_duplicate(self, existing_ticket, new_ticket):
        return existing_ticket.lower() == new_ticket.lower()

    # SR-06: Status update
    def update_status(self, status):
        valid_statuses = ["Open", "In Progress", "Resolved"]

        if status in valid_statuses:
            return status

        return "Invalid status"

    # SR-07: Queue assignment
    def assign_queue(self, category):
        if category == "Network":
            return "Network Support"

        return "General Support"

    # SR-08: Report generation
    def generate_report(self, output_format):
        valid_formats = ["pdf", "xlsx", "csv"]

        if output_format.lower() in valid_formats:
            return "Report generated"

        return "Invalid report format"


# ===== 🔥 DEMO RUN (ADD THIS FOR PRESENTATION) =====
def demo_run():
    system = HelpDeskSystem()

    print("=== DEMO: Creating Ticket ===")
    message, priority = system.create_ticket("Network", "Internet down", "High")
    print(f"Message: {message}")
    print(f"Priority Score: {priority}")

    print("\n=== DEMO: Assigning Queue ===")
    queue = system.assign_queue("Network")
    print(f"Assigned Queue: {queue}")

    print("\n=== DEMO: Duplicate Check ===")
    duplicate = system.detect_duplicate("Internet down", "Internet down")
    print(f"Duplicate Found: {duplicate}")

    print("\n=== DEMO: Status Update ===")
    status = system.update_status("Resolved")
    print(f"Updated Status: {status}")


class TestHelpDeskSystem(unittest.TestCase):

    def setUp(self):
        self.system = HelpDeskSystem()

    def test_SR03_priority_assignment_happy(self):
        message, priority = self.system.create_ticket(
            "Network",
            "Internet down",
            "High"
        )

        self.assertEqual(message, "Incident created")
        self.assertEqual(priority, 4)

    def test_SR03_priority_assignment_edge(self):
        message, priority = self.system.create_ticket(
            "General",
            "Slow internet",
            "Low"
        )

        self.assertEqual(message, "Incident created")
        self.assertEqual(priority, 1)

    def test_SR04_duplicate_detection_happy(self):
        result = self.system.detect_duplicate(
            "Internet down",
            "Internet down"
        )

        self.assertTrue(result)

    def test_SR04_duplicate_detection_edge(self):
        result = self.system.detect_duplicate(
            "Internet down",
            "Printer not working"
        )

        self.assertFalse(result)

    def test_SR06_status_update_happy(self):
        status = self.system.update_status("Resolved")
        self.assertEqual(status, "Resolved")

    def test_SR06_status_update_edge(self):
        status = self.system.update_status("Closed")
        self.assertEqual(status, "Invalid status")

    def test_SR07_queue_assignment_happy(self):
        queue = self.system.assign_queue("Network")
        self.assertEqual(queue, "Network Support")

    def test_SR07_queue_assignment_edge(self):
        queue = self.system.assign_queue("Hardware")
        self.assertEqual(queue, "General Support")

    def test_SR08_report_generation_happy(self):
        report_status = self.system.generate_report("pdf")
        self.assertEqual(report_status, "Report generated")

    def test_SR08_report_generation_edge(self):
        report_status = self.system.generate_report("doc")
        self.assertEqual(report_status, "Invalid report format")


if __name__ == "__main__":
    demo_run()   # 👈 THIS CREATES YOUR LIVE DEMO OUTPUT
    print("\n--- Running Tests ---\n")
    unittest.main()
