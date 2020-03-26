from django.db import models

# Create your models here.
# 学生
class Student(models.Model):
    sid=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=32)
    gender=models.CharField(max_length=32)
    class_id=models.ForeignKey(to="Class",on_delete=models.CASCADE)

# 班级
class Class(models.Model):
    cid=models.AutoField(primary_key=True)
    caption=models.CharField(max_length=32)
    grade=models.ForeignKey(to="Class_grade",on_delete=models.CASCADE)
    teachers=models.ManyToManyField(to="Teacher")

# 年级
class Class_grade(models.Model):
    gid=models.AutoField(primary_key=True)
    gname=models.CharField(max_length=32)

# 课程
class Course(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=32)
    teacher=models.ForeignKey(to="Teacher",on_delete=models.CASCADE)

# 老师
class Teacher(models.Model):
    tid=models.AutoField(primary_key=True)
    tname=models.CharField(max_length=32)


#成绩
class Score(models.Model):
    sid=models.AutoField(primary_key=True)
    student=models.ForeignKey(to="Student",on_delete=models.CASCADE)
    course=models.ForeignKey(to="Course",on_delete=models.CASCADE)
    score=models.IntegerField()