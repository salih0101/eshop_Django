# Generated by Django 4.2 on 2023-04-28 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_shoppingcart'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('total_for_product', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.product')),
            ],
        ),
        migrations.DeleteModel(
            name='ShoppingCart',
        ),
    ]