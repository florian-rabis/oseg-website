from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, MultiFieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel

from base.blocks import ExtBaseStreamBlock



class ExtendedPage(Page):
    body = StreamField(
        ExtBaseStreamBlock(), verbose_name="Page Body", blank=True
    )
    
    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]