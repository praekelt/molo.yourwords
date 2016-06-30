from django.http import HttpResponse
from import_export import resources
from molo.yourwords.admin import YourWordsCompetitionAdmin
from molo.yourwords.models import YourWordsCompetitionEntry, \
    YourWordsCompetition
from wagtailmodeladmin.options import ModelAdmin, wagtailmodeladmin_register, \
    ModelAdminGroup
from wagtailmodeladmin.views import IndexView


class YourWordsEntriesResource(resources.ModelResource):
    class Meta:
        model = YourWordsCompetitionEntry
        exclude = ('id', '_convert', 'article_page')


class ModelAdminTemplate(IndexView):
    def post(self, request, *args, **kwargs):
        list_filter = request.GET.get('competition__slug')

        dataset = YourWordsEntriesResource().export(
            YourWordsCompetitionEntry.objects.filter(
                competition__slug=list_filter
            ) if list_filter is not None else None)

        response = HttpResponse(dataset.csv, content_type="csv")
        response['Content-Disposition'] = \
            'attachment; filename=yourwords_entries.csv'
        return response

    def get_template_names(self):
        return 'admin/yourwords/model_admin_template.html'


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

    def entries(self, obj, *args, **kwargs):
        url = '/admin/modeladmin/yourwords/yourwordscompetitionentry/'
        return '<a href="%s?competition__slug=%s">%s</a>' % (
            url, obj.slug, obj)

    entries.allow_tags = True
    entries.short_description = 'Title'


class YourWordsAdminGroup(ModelAdminGroup):
    menu_label = 'YourWords'
    menu_icon = 'folder-open-inverse'
    menu_order = 400
    items = (YourWordsEntriesModelAdmin, YourWordsModelAdmin)


wagtailmodeladmin_register(YourWordsAdminGroup)
