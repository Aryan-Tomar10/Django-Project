from django.test import TestCase
from django.urls import reverse
from .models import TASK


class TaskViewsTests(TestCase):
    def test_task_list_renders(self):
        task = TASK.objects.create(title='Test task')

        response = self.client.get(reverse('todo:task_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, task.title)

    def test_create_task(self):
        response = self.client.post(reverse('todo:task_create'), {
            'title': 'New task',
            'description': 'Task details',
        })

        self.assertRedirects(response, reverse('todo:task_list'))
        self.assertTrue(TASK.objects.filter(
            title='New task',
            description='Task details',
        ).exists())

    def test_create_task_requires_title(self):
        response = self.client.post(reverse('todo:task_create'), {
            'title': ' ',
            'description': 'Task details',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Title can not be empty.')
        self.assertTemplateUsed(response, 'todo/task_form.html')
        self.assertFalse(TASK.objects.exists())

    def test_update_task(self):
        task = TASK.objects.create(title='Old title', completed=True)

        response = self.client.post(
            reverse('todo:task_update', args=[task.pk]),
            {
                'title': 'Updated title',
                'description': 'Updated details',
                'completed': 'on',
            },
        )

        self.assertRedirects(response, reverse('todo:task_list'))
        task.refresh_from_db()
        self.assertEqual(task.title, 'Updated title')
        self.assertEqual(task.description, 'Updated details')
        self.assertTrue(task.completed)

    def test_delete_task(self):
        task = TASK.objects.create(title='Remove me')

        response = self.client.post(
            reverse('todo:task_delete', args=[task.pk]),
        )

        self.assertRedirects(response, reverse('todo:task_list'))
        self.assertFalse(TASK.objects.filter(pk=task.pk).exists())

    def test_toggle_task(self):
        task = TASK.objects.create(title='Toggle me')

        response = self.client.post(
            reverse('todo:task_toggle', args=[task.pk]),
        )

        self.assertRedirects(response, reverse('todo:task_list'))
        task.refresh_from_db()
        self.assertTrue(task.completed)
