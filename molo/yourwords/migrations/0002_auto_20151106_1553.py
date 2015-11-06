# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import molo.core.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks
import django.db.models.deletion
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0002_add_verbose_names'),
        ('wagtailredirects', '0002_add_verbose_names'),
        ('wagtailimages', '0006_add_verbose_names'),
        ('wagtailsearch', '0002_add_verbose_names'),
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('yourwords', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YourWordsCompetition',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('description', models.TextField(null=True, blank=True)),
                ('content', wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title')), (b'paragraph', molo.core.blocks.MarkDownBlock()), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label=b'Item'))), (b'numbered_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label=b'Item'))), (b'page', wagtail.wagtailcore.blocks.PageChooserBlock())], null=True, blank=True)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
                ('terms_and_conditions_link_page', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailcore.Page', help_text=b'Link to terms and conditions page', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RenameModel(
            old_name='CompetitionEntry',
            new_name='YourWordsCompetitionEntry',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='image',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='terms_and_conditions_link_page',
        ),
        migrations.DeleteModel(
            name='Competition',
        ),
    ]