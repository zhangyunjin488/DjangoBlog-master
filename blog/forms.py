import logging

from django import forms
from haystack.forms import SearchForm


logger = logging.getLogger(__name__)


class BlogSearchForm(SearchForm):
    querydata = forms.CharField(required=True)

    def search(self):
        datas = super(BlogSearchForm, self).search()
        if not self.is_valid():
            return self.no_query_found()

        if self.cleaned_data['querydata']:
            logger.info(self.cleaned_data['querydata'])
        return datas


from django import forms
from .models import Article, Category, Tag

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'category', 'tags']  # 允许用户编辑的字段
        widgets = {
            'body': forms.Textarea(attrs={'class': 'markdown-editor'}),  # 可集成Markdown编辑器
        }