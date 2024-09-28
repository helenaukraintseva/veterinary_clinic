from django.db import models


class PetGenders(models.TextChoices):
    BOY = 'boy', 'Мальчик'
    GIRL = 'girl', 'Девочка'


class EmployeePositions(models.TextChoices):
    VETERINARIAN = 'veterinarian', 'Ветеринар'
    SURGEON = 'surgeon', 'Хирург'
    RADIOLOGIST = 'radiologist', 'Рентгенолог'
    DENTIST = 'dentist', 'Стоматолог'
    NURSE = 'nurse', 'Медсестра'
    ASSISTANT = 'assistant', 'Ассистент'
    ADMINISTRATOR = 'administrator', 'Администратор'


class PetSpecies(models.TextChoices):
    DOG = 'dog', 'Собака'
    CAT = 'cat', 'Кошка'


class Services(models.TextChoices):
    GENERAL_CHECKUP = 'GC', 'Общий осмотр'
    VACCINATION = 'VC', 'Вакцинация'
    DENTAL_CARE = 'DC', 'Стоматологическая помощь'
    SURGERY = 'SG', 'Хирургия'
    EMERGENCY = 'EM', 'Неотложная помощь'
    GROOMING = 'GR', 'Груминг'
    NUTRITIONAL_COUNSELING = 'NC', 'Консультация по питанию'
    BEHAVIORAL_TRAINING = 'BT', 'Поведенческая коррекция'


class ServicesDescriptions(models.TextChoices):
    GC = 'Общий осмотр включает проверку здоровья питомца, измерение температуры, осмотр глаз, ушей и шерсти.',
    VC = 'Вакцинация направлена на профилактику различных инфекционных заболеваний.',
    DC = 'Стоматологическая помощь включает чистку зубов и лечение стоматологических заболеваний.',
    SG = 'Хирургические операции, включая стерилизацию, удаление опухолей и другие процедуры.',
    EM = 'Неотложная помощь для экстренных случаев и тяжелых травм.',
    GR = 'Груминг включает стрижку, мытье и уход за шерстью питомца.',
    NC = 'Консультация по питанию поможет подобрать правильный рацион для вашего питомца.',
    BT = 'Поведенческая коррекция помогает улучшить поведение питомца, включая тренировки и обучение.'
