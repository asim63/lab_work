# labapp/tests.py - Asim Poudel | Roll No: 8
from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Note

class NoteModelTest(TestCase):

    def test_notes_can_be_created(self):
        """Test that a note can be created successfully."""
        note = Note.objects.create(
            title="Test Note - Asim Poudel Roll 8",
            content="This is a valid note content."
        )
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(note.title,
                         "Test Note - Asim Poudel Roll 8")
        self.assertEqual(note.content,
                         "This is a valid note content.")
        print("PASS: test_notes_can_be_created - Asim Poudel | Roll: 8")

    def test_error_occurs_if_description_is_less_than_10_chars_long(self):
        """Test that ValidationError is raised for short content."""
        note = Note(
            title="Short Note",
            content="Short"
        )
        with self.assertRaises(ValidationError) as context:
            note.full_clean()
        self.assertIn(
            "Description must be at least 10 characters long.",
            str(context.exception)
        )
        print("PASS: test_error_short_description - Asim Poudel | Roll: 8")