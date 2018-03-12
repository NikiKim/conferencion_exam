
from django.db import models
from django.utils import timezone


class Speakers(models.Model):
    speakers_name = models.CharField(max_length=200)  # имя спикера
    about_speakers = models.TextField()  # имя описание спикера
    models.ForeignKey('self', on_delete=models.CASCADE, )  # ключ спикера , который ссылается на себя и не задействован

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.speakers_name


class Reports(models.Model):
    reports_name = models.CharField(max_length=200)
    speakers = models.ForeignKey(Speakers, related_name='speakers',  on_delete=models.CASCADE,)
    description = models.TextField()

    created_date = models.DateTimeField(
        default=timezone.now)

    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):     # метод публикации для записи
        self.published_date = timezone.now()
        self.save()

    def __str__(self):    # метод возращения имени
        return self.reports_name


# Связь многое-к-одному - ForeignKey.on_delete
#Когда объект, на который ссылается ForeignKey, удаляется,
#Django эмулирует поведение SQL правил, указанных в аргументе on_delete.
#Например, если ваше поле ForeignKey может содержать NULL и вы хотите, чтобы
#оно устанавливалось в NULL после удаления связанного объекта:CASCADE
#Каскадное удаление. Django эмулирует поведение SQL правила
#ON DELETE CASCADE и так же удаляет объекты, связанные через ForeignKey.


#ForeignKey.related_name
# Название, используемое для обратной связи от связанной модели.
# Также значение по умолчанию для related_query_name
# (название обратной связи используемое при фильтрации результата запроса).