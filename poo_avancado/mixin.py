class HtmlToStringMixin:
    def __str__(self):
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')</strong>')


            