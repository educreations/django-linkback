from .widgets import ForeignKeyRawIdWithLinkWidget


class LinkBackMixin(object):
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        kwargs['widget'] = ForeignKeyRawIdWithLinkWidget(db_field.rel, self.admin_site)
        return db_field.formfield(**kwargs)
