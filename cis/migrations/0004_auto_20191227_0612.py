# Generated by Django 2.2.4 on 2019-12-26 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cis', '0003_auto_20191227_0534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
            ],
        ),
        migrations.RemoveField(
            model_name='land',
            name='faq_answer',
        ),
        migrations.RemoveField(
            model_name='land',
            name='faq_answer1',
        ),
        migrations.RemoveField(
            model_name='land',
            name='faq_answer2',
        ),
        migrations.RemoveField(
            model_name='land',
            name='faq_answer3',
        ),
        migrations.RemoveField(
            model_name='land',
            name='faq_answer4',
        ),
        migrations.RemoveField(
            model_name='land',
            name='faq_answer5',
        ),
        migrations.RemoveField(
            model_name='land',
            name='faq_answer6',
        ),
        migrations.RemoveField(
            model_name='land',
            name='faq_answer7',
        ),
        migrations.RemoveField(
            model_name='land',
            name='faq_question',
        ),
        migrations.RemoveField(
            model_name='land',
            name='faq_question1',
        ),
        migrations.RemoveField(
            model_name='land',
            name='faq_question2',
        ),
        migrations.RemoveField(
            model_name='land',
            name='faq_question3',
        ),
        migrations.RemoveField(
            model_name='land',
            name='faq_question4',
        ),
        migrations.RemoveField(
            model_name='land',
            name='faq_question5',
        ),
        migrations.RemoveField(
            model_name='land',
            name='faq_question6',
        ),
        migrations.RemoveField(
            model_name='land',
            name='faq_question7',
        ),
    ]
