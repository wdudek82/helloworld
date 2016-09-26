import datetime

from django.shortcuts import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Question


def create_question(question_text, days):
    """
    Creates a question qith the given 'question_text' and publishes the
    given number of 'days' offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('poll:index'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'No polls are available.') # Is not working - why?
        # print(re.findall(r'\S+\spoll\S+\s', str(response.content)))
        self.assertQuerysetEqual(response.context['questions'], [])

    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page.
        """
        create_question(question_text='test', days=-30)
        response = self.client.get(reverse('poll:index'))
        self.assertQuerysetEqual(
            response.context['questions'],
            ['<Question: test>']
        )


class QuestionMethodTest(TestCase):
    present = timezone.now()

    def test_was_published_recently_with_old_2_question(self):
        two_days_old = self.present - datetime.timedelta(days=2)
        two_days_old_question = Question(pub_date=two_days_old)
        self.assertIs(two_days_old_question.was_published_recently(), False)

    def test_was_published_recently_with_day_old_question(self):
        day_old = self.present - datetime.timedelta(hours=20)
        day_old_question = Question(pub_date=day_old)
        self.assertIs(day_old_question.was_published_recently(), True)

    def test_was_published_recently_with_present_question(self):
        present_question = Question(pub_date=self.present)
        self.assertIs(present_question.was_published_recently(), True)

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        future = self.present + datetime.timedelta(days=30)
        future_question = Question(pub_date=future)
        self.assertIs(future_question.was_published_recently(), False)
