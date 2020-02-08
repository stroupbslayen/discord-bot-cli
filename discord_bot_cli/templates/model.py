model = '''
"""{name} Model."""

from bot.database import Model


class {name}(Model):
    """{name} Model."""

    __table__ = '{name_plural}'

'''
