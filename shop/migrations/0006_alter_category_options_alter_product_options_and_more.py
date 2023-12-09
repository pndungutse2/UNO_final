# Generated by Django 5.0a1 on 2023-12-09 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveIndex(
            model_name='category',
            name='shop_catego_name_289c7e_idx',
        ),
        migrations.RemoveIndex(
            model_name='product',
            name='shop_produc_id_f21274_idx',
        ),
        migrations.RemoveIndex(
            model_name='product',
            name='shop_produc_name_a2070e_idx',
        ),
        migrations.RemoveIndex(
            model_name='product',
            name='shop_produc_created_ef211c_idx',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]
