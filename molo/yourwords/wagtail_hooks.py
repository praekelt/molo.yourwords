from django.http import HttpResponse
from django.views.generic import View
from import_export import resources
from molo.yourwords.admin import YourWordsCompetitionAdmin
from molo.yourwords.models import YourWordsCompetitionEntry, \
    YourWordsCompetition
from wagtailmodeladmin.options import ModelAdmin, wagtailmodeladmin_register, \
    ModelAdminGroup
from wagtailmodeladmin.views import IndexView


class ModelAdminTemplate(IndexView):
    def get_template_names(self):
        return 'admin/yourwords/model_admin_template.html'


class YourWordsEntriesResource(resources.ModelResource):
    class Meta:
        model = YourWordsCompetitionEntry
        exclude = ('id', '_convert', 'article_page')


class YourWordEntriesExport(View):
    model = YourWordsCompetitionEntry
    list_filter = ['competition__slug']

    def get(self, request, *args, **kwargs):
        dataset = YourWordsEntriesResource().export(YourWordsCompetitionEntry
                                                    .objects.filter())
        response = HttpResponse(dataset.csv, content_type="csv")
        response['Content-Disposition'] = \
            'attachment; filename=yourwordsentries.csv'
        return response


class YourWordsEntriesModelAdmin(ModelAdmin):
    model = YourWordsCompetitionEntry
    menu_label = 'Entries'
    menu_icon = 'edit'
    index_view_class = ModelAdminTemplate
    add_to_settings_menu = False
    list_display = ['story_name', 'user', 'hide_real_name',
                    'submission_date', 'is_read', 'is_shortlisted',
                    'is_winner', '_convert']

    list_filter = ['competition__slug']

    search_fields = ('story_name',)

    def _convert(self, obj, *args, **kwargs):
        if obj.article_page:
            return (
                '<a href="/admin/pages/%d/edit/">Article Page</a>' %
                obj.article_page.id)
        return (
            '<a href="/django-admin/yourwords/yourwordscompetitionentry'
            '/%d/convert/" class="addlink">Convert to article</a>' %
            obj.id)

    _convert.allow_tags = True
    _convert.short_description = ''


class YourWordsModelAdmin(ModelAdmin, YourWordsCompetitionAdmin):
    model = YourWordsCompetition
    menu_label = 'Competitions'
    menu_icon = 'doc-full'
    add_to_settings_menu = False
    list_display = ['entries', 'start_date', 'end_date', 'status',
                    'number_of_entries']

    search_fields = ('story_name',)


class YourWordsAdminGroup(ModelAdminGroup):
    menu_label = 'YourWords'
    menu_icon = 'folder-open-inverse'
    menu_order = 400
    items = (YourWordsEntriesModelAdmin, YourWordsModelAdmin)


wagtailmodeladmin_register(YourWordsAdminGroup)
