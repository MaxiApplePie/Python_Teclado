from unittest import TestCase
from printer import Printer, PrinterError


class TestPrinter(TestCase):
    def setUp(self):
        self.printer = Printer(pages_per_s=2.0, capacity=300)

    def test_print_with_capacity(self):
        message = self.printer.print(25)
        self.assertEqual('Printer 25 pages in 12.50 seconds', message)

    def test_print_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(301)

    def test_print_exact_capacity(self):
        self.printer.print(self.printer._capacity)

    def test_printer_speed(self):
        pages = 10
        expected = 'Printer 10 pages in 5.00 seconds'
        result = self.printer(pages)
        self.assertEqual(result, expected)




