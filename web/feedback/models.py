from django.db import models


# Create your models here.

# class Groups(models.Model):
#     pass


class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Questions(models.Model):
    question = models.TextField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Answers(models.Model):
    answer = models.IntegerField(
        null=False
    )
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer


#####################


class Feedback(models.Model):
    class Meta:
        verbose_name = "Отзывы об обучении"

    STATUS_CODE = (
        (0, "Не прочитано"),
        (1, "Принятно"),
        (2, "Отклонено"),
    )

    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        blank=True
    )

    text = models.CharField(
        max_length=1024,
        verbose_name="Текст сообщения"
    )

    rate = models.IntegerField(
        default=0,
        verbose_name="Оценка сообщения"
    )

    status = models.IntegerField(
        default=STATUS_CODE[0][0],
        verbose_name="Статус отзыва",
        choices=STATUS_CODE
    )

# class FeedbackMonthly(models.Model):
#     pass
