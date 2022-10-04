# Generated by Django 3.2.4 on 2022-04-15 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='confirm',
        ),
        migrations.AlterField(
            model_name='order',
            name='courier_status',
            field=models.CharField(blank=True, choices=[('Заказ принят', 'Accepted'), ('Еду за заказом', 'Pick Up'), ('Забрал заказ', 'Picked Up'), ('Доставляю', 'Delivering'), ('Заказ доставлен', 'Delivered'), ('Отменить заказ', 'Cancel'), ('Подтвердить заказ', 'Confirm')], max_length=255, verbose_name='Статусы курьера'),
        ),
    ]
