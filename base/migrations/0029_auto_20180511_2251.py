# Generated by Django 2.0.4 on 2018-05-11 22:51

import base.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_auto_20180511_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendedpage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading_block', wagtail.core.blocks.StructBlock((('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('level', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'Überschrift 1'), ('h2', 'Überschrift 2'), ('h3', 'Überschrift 3'), ('h4', 'Überschrift 4')], required=False))))), ('text_block', wagtail.core.blocks.RichTextBlock()), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Einbetten externer Inhalte wie Viedeos.', icon='media')), ('link_block', wagtail.core.blocks.StreamBlock((('url', wagtail.core.blocks.URLBlock()), ('page', wagtail.core.blocks.PageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())))), ('image_block', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('caption', wagtail.core.blocks.CharBlock(classname='caption', required=True)), ('description', wagtail.core.blocks.TextBlock(classname='description')), ('author', wagtail.core.blocks.CharBlock(classname='author', required=True)), ('license', wagtail.core.blocks.CharBlock(classname='license', required=True)), ('link', wagtail.core.blocks.StreamBlock((('url', wagtail.core.blocks.URLBlock()), ('page', wagtail.core.blocks.PageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock()))))))), ('columns', wagtail.core.blocks.StreamBlock((('column_block', wagtail.core.blocks.StructBlock((('max_width', wagtail.core.blocks.IntegerBlock(required=False)), ('body', wagtail.core.blocks.StreamBlock((('heading_block', wagtail.core.blocks.StructBlock((('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('level', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'Überschrift 1'), ('h2', 'Überschrift 2'), ('h3', 'Überschrift 3'), ('h4', 'Überschrift 4')], required=False))))), ('text_block', wagtail.core.blocks.RichTextBlock()), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Einbetten externer Inhalte wie Viedeos.', icon='media')), ('link_block', wagtail.core.blocks.StreamBlock((('url', wagtail.core.blocks.URLBlock()), ('page', wagtail.core.blocks.PageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())))), ('image_block', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('caption', wagtail.core.blocks.CharBlock(classname='caption', required=True)), ('description', wagtail.core.blocks.TextBlock(classname='description')), ('author', wagtail.core.blocks.CharBlock(classname='author', required=True)), ('license', wagtail.core.blocks.CharBlock(classname='license', required=True)), ('link', wagtail.core.blocks.StreamBlock((('url', wagtail.core.blocks.URLBlock()), ('page', wagtail.core.blocks.PageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock()))))))))))))),))), ('carousel', wagtail.core.blocks.StreamBlock((('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('caption', wagtail.core.blocks.CharBlock(classname='caption', required=True)), ('description', wagtail.core.blocks.TextBlock(classname='description')), ('author', wagtail.core.blocks.CharBlock(classname='author', required=True)), ('license', wagtail.core.blocks.CharBlock(classname='license', required=True)), ('link', wagtail.core.blocks.StreamBlock((('url', wagtail.core.blocks.URLBlock()), ('page', wagtail.core.blocks.PageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock()))))))), ('slide', wagtail.core.blocks.StreamBlock((('heading_block', wagtail.core.blocks.StructBlock((('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('level', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'Überschrift 1'), ('h2', 'Überschrift 2'), ('h3', 'Überschrift 3'), ('h4', 'Überschrift 4')], required=False))))), ('text_block', wagtail.core.blocks.RichTextBlock()), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Einbetten externer Inhalte wie Viedeos.', icon='media')), ('link_block', wagtail.core.blocks.StreamBlock((('url', wagtail.core.blocks.URLBlock()), ('page', wagtail.core.blocks.PageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())))), ('image_block', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('caption', wagtail.core.blocks.CharBlock(classname='caption', required=True)), ('description', wagtail.core.blocks.TextBlock(classname='description')), ('author', wagtail.core.blocks.CharBlock(classname='author', required=True)), ('license', wagtail.core.blocks.CharBlock(classname='license', required=True)), ('link', wagtail.core.blocks.StreamBlock((('url', wagtail.core.blocks.URLBlock()), ('page', wagtail.core.blocks.PageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock()))))))))))))), ('gallery', wagtail.core.blocks.ListBlock(base.blocks.ImageBlock))), blank=True, verbose_name='Page Body'),
        ),
    ]
