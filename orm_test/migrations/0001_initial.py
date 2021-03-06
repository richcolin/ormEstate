# Generated by Django 2.1.4 on 2020-03-25 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('caption', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Class_grade',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('gname', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm_test.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=32)),
                ('gender', models.CharField(max_length=32)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm_test.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('tname', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='score',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm_test.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm_test.Teacher'),
        ),
        migrations.AddField(
            model_name='class',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm_test.Class_grade'),
        ),
        migrations.AddField(
            model_name='class',
            name='teachers',
            field=models.ManyToManyField(to='orm_test.Teacher'),
        ),
    ]
