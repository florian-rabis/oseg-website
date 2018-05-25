import collections

from django.template.loader import render_to_string
from django.core.exceptions import NON_FIELD_ERRORS

from wagtail.core.blocks import StreamBlock, CharBlock, ChoiceBlock, RichTextBlock, IntegerBlock, StructBlock, TextBlock, PageChooserBlock, URLBlock, ListBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from django.core.paginator import Page
from pydoc import classname
from wagtail.documents.blocks import DocumentChooserBlock


class HeadingBlock(StructBlock):
    heading_text = CharBlock(classname="title", required=True)
    level = ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('h1', 'Überschrift 1'),
        ('h2', 'Überschrift 2'),
        ('h3', 'Überschrift 3'),
        ('h4', 'Überschrift 4')
    ], blank=True, required=False)
    
    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"
        
class LinkBlock(StreamBlock):
    url = URLBlock()
    page = PageChooserBlock()
    document = DocumentChooserBlock()
    
    
    class Meta:
        classname = "link-block"
        max_num = 1

        
class ImageBlock(StructBlock):
    image = ImageChooserBlock(icon="image")
    caption = CharBlock(classname="caption", required=True)
    description = TextBlock(classname="description")
    author = CharBlock(classname="author", required=True)
    license = CharBlock(classname="license", required=True)
    link = LinkBlock(required=False)
    
    class Meta:
        icon = "image"
#        template = "blocks/image_block.html"
        classname = "image-block"

class BaseStreamBlock(StreamBlock):
    heading_block = HeadingBlock()
    text_block = RichTextBlock()
    embed_block = EmbedBlock(
        help_text='Einbetten externer Inhalte wie Viedeos.',
        icon="media"
    )
    link_block = LinkBlock()
    image_block = ImageBlock()

class ColumnBlock(StructBlock):
    max_width = IntegerBlock(required=False)
    body = BaseStreamBlock()
    
        
    class Meta:
        template = "blocks/column_block.html"
    
class ColumnsBlock(StreamBlock):
    column_block = ColumnBlock()
    
    class Meta:
        template = "blocks/columns_block.html"
        classname = "columns-block"
        
    def render_form(self, value, prefix='', errors=None):
        error_dict = {}
        if errors:
            if len(errors) > 1:
                # We rely on StreamBlock.clean throwing a single
                # StreamBlockValidationError with a specially crafted 'params'
                # attribute that we can pull apart and distribute to the child
                # blocks
                raise TypeError('StreamBlock.render_form unexpectedly received multiple errors')
            error_dict = errors.as_data()[0].params

        # value can be None when the StreamField is in a formset
        if value is None:
            value = self.get_default()
        # drop any child values that are an unrecognised block type
        valid_children = [child for child in value if child.block_type in self.child_blocks]

        list_members_html = [
            self.render_list_member(child.block_type, child.value, "%s-%d" % (prefix, i), i,
                                    errors=error_dict.get(i), id=child.id)
            for (i, child) in enumerate(valid_children)
        ]

        return render_to_string('wagtailadmin/block_forms/stream.html', {
            'prefix': prefix,
            'list_members_html': list_members_html,
            'child_blocks': sorted(self.child_blocks.values(), key=lambda child_block: child_block.meta.group),
            'header_menu_prefix': '%s-before' % prefix,
            'block_errors': error_dict.get(NON_FIELD_ERRORS),
            'classname': self.meta.classname
        })

class SlideBlock(BaseStreamBlock):
    image_block = ImageBlock(classname="d-block w-100")
    
    class Meta:
        template = "blocks/carousel-item_block.html"

class CarouselBlock(StreamBlock):
    slide_block = SlideBlock()
    
    class Meta:
        template = "blocks/carousel_block.html"
        
class GalleryBlock(StreamBlock):
    image_block = ImageBlock()

class ExtBaseStreamBlock(BaseStreamBlock):
    columns_block = ColumnsBlock()
    carousel_block = CarouselBlock()
    gallery_block = GalleryBlock()

    
     