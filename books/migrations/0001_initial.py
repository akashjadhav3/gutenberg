# Generated by Django 4.0.4 on 2022-04-22 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_year', models.SmallIntegerField(blank=True, null=True)),
                ('death_year', models.SmallIntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('download_count', models.PositiveIntegerField(blank=True, null=True)),
                ('gutenberg_id', models.PositiveIntegerField(unique=True)),
                ('media_type', models.CharField(max_length=16)),
                ('title', models.CharField(blank=True, max_length=1024, null=True)),
                ('authors', models.ManyToManyField(to='books.author')),
            ],
        ),
        migrations.CreateModel(
            name='Bookshelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mime_type', models.CharField(max_length=32)),
                ('url', models.CharField(max_length=256)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='bookshelves',
            field=models.ManyToManyField(to='books.bookshelf'),
        ),
        migrations.AddField(
            model_name='book',
            name='languages',
            field=models.ManyToManyField(to='books.language'),
        ),
        migrations.AddField(
            model_name='book',
            name='subjects',
            field=models.ManyToManyField(to='books.subject'),
        ),
    ]
