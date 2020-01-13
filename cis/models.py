from django.db import models


class Land(models.Model):
    title = models.CharField('заголовок на главной', max_length=100)
    sub_title = models.CharField('меньший заголовок главной', max_length=100)
    text = models.TextField('текст на главной')
    picture = models.ImageField('Картинка на главной', upload_to='ecoc/photos/')
    title_second = models.CharField('заголовок третьей сноски', max_length=100)
    title_head = models.CharField('заголовок третьей сноски 1', max_length=100)
    sub_line = models.CharField('строка sub', max_length=100)
    about_line = models.CharField('строка с описанием ', max_length=100)
    title_head1 = models.CharField('заголовок третьей сноски 2', max_length=100)
    sub_line1 = models.CharField('строка sub', max_length=100)
    about_line1 = models.CharField('строка с описанием ', max_length=100)
    title_head2 = models.CharField('заголовок третьей сноски 3', max_length=100)
    sub_line2 = models.CharField('строка sub', max_length=100)
    about_line2 = models.CharField('строка с описанием ', max_length=100)
    title_1 = models.CharField('заголовок первой сноски', max_length=100)
    slider = models.ImageField('Картинка слайдер 1', upload_to='ecoc/photos/')
    text_slider = models.TextField('надпись под картинкой-слайдером 1')
    slider1 = models.ImageField('Картинка слайдер 2', upload_to='ecoc/photos/')
    text_slider1 = models.TextField('надпись под картинкой-слайдером 2')
    slider2 = models.ImageField('Картинка слайдер 3', upload_to='ecoc/photos/')
    text_slider2 = models.TextField('надпись под картинкой-слайдером 3')
    slider3 = models.ImageField('Картинка слайдер 4', upload_to='ecoc/photos/')
    text_slider3 = models.TextField('надпись под картинкой-слайдером 4')
    slider4 = models.ImageField('Картинка слайдер 5', upload_to='ecoc/photos/')
    text_slider4 = models.TextField('надпись под картинкой-слайдером 5')
    slider5 = models.ImageField('Картинка слайдер 6', upload_to='ecoc/photos/')
    text_slider5 = models.TextField('надпись под картинкой-слайдером 6')
    title_2 = models.CharField('заголовок второй сноски', max_length=100)
    text1 = models.TextField('надпись второй сноски1')
    picture_big = models.ImageField('Большая картинка вторая сноска', upload_to='ecoc/photos/')
    text2 = models.TextField('надпись второй сноски2')
    picture_little = models.FileField('первая маленькая картинка, вторая сноска', upload_to='ecoc/photos/')
    text3 = models.TextField('надпись второй сноски2')
    picture_little1 = models.FileField('вторая маленькая картинка, вторая сноска', upload_to='ecoc/photos/')
    text4 = models.TextField('надпись второй сноски2')
    picture_little2 = models.FileField('третья маленькая картинка, вторая сноска', upload_to='ecoc/photos/')
    title_3 = models.CharField('Заголовок вопрос-ответ', max_length=100)
    title_4 = models.CharField('Заголовок заказа', max_length=100)


class Shop(models.Model):
    link_url = models.URLField('ссылка на магазин', null=True, blank=True)
    image_for = models.ImageField('картинка партнера', null=True, blank=True, upload_to='ecoc/photos/')
    event = models.CharField('event', null=True, blank=True, max_length=100)


class Faq(models.Model):
    question = models.TextField('Вопрос')
    answer = models.TextField('Ответ')
