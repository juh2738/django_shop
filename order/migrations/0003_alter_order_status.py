# Generated by Django 4.0.5 on 2022-09-04 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_memo_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('대기중', '대기중'), ('결제대기', '결제대기중'), ('결제완료', '결제완료'), ('환불', '환불')], default='대기중', max_length=32, verbose_name='상태'),
        ),
    ]
