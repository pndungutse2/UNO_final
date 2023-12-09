# Generated by Django 5.0a1 on 2023-11-02 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_category_id_alter_product_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.RenameIndex(
            model_name='product',
            new_name='shop_produc_id_f21274_idx',
            old_fields=('id', 'slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='shop_catego_name_289c7e_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name'], name='shop_produc_name_a2070e_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['-created'], name='shop_produc_created_ef211c_idx'),
        ),
    ]
