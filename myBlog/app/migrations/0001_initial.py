# Generated by Django 2.1.4 on 2018-12-23 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=32)),
                ('comment_author_email', models.EmailField(max_length=32)),
                ('comment_author_IP', models.CharField(max_length=32)),
                ('comment_date', models.DateTimeField(auto_now=True)),
                ('comment_content', models.TextField()),
                ('comment_approved', models.BooleanField(default=False)),
                ('comment_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Comments')),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_url', models.CharField(max_length=128)),
                ('link_name', models.CharField(max_length=128)),
                ('link_description', models.CharField(max_length=1024)),
                ('link_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_data', models.DateTimeField(auto_now=True)),
                ('post_content', models.TextField()),
                ('post_title', models.CharField(max_length=128)),
                ('post_excerpt', models.TextField()),
                ('post_status', models.SmallIntegerField(choices=[(0, 'publish'), (1, 'auto-draft'), (2, 'inherit')])),
                ('comment_status', models.SmallIntegerField(choices=[(0, 'open'), (1, 'closed')])),
                ('post_modified', models.DateTimeField(auto_now_add=True)),
                ('post_type', models.SmallIntegerField(choices=[(0, '原创'), (1, '转载')])),
                ('menu_order', models.SmallIntegerField()),
                ('comment_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('slug', models.CharField(max_length=32, unique=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Terms')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('nicename', models.CharField(max_length=32, unique=True)),
                ('email', models.EmailField(max_length=32)),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('activation_key', models.CharField(max_length=128)),
                ('display_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='posts',
            name='terms',
            field=models.ManyToManyField(to='app.Terms'),
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_post_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Posts'),
        ),
    ]
