from django.core.management.base import BaseCommand
from todos.models import Todo
from django.utils import timezone

class Command(BaseCommand):
    help = 'Creates sample todo items'

    def handle(self, *args, **kwargs):
        todos = [
            {'title': '買い物リストを作成する', 'completed': False},
            {'title': '部屋の掃除をする', 'completed': True},
            {'title': '本を読む', 'completed': False},
            {'title': '運動する', 'completed': False},
            {'title': '日記を書く', 'completed': True},
        ]

        for todo_data in todos:
            todo = Todo.objects.create(
                title=todo_data['title'],
                completed=todo_data['completed'],
                created_at=timezone.now()
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created todo: {todo.title}')
            ) 