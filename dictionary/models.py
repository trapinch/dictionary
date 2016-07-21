from django.db import models

class Language(models.Model):
    language = models.CharField(max_length=5, primary_key=True)
    alphabet = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.language)

class Word(models.Model):
    language   = models.ForeignKey(Language, on_delete=models.CASCADE)
    id_word    = models.IntegerField()
    term       = models.CharField(max_length=30)
    definition = models.CharField(max_length=150)
    category   = models.CharField(max_length=30)
    stage      = models.CharField(max_length=1, default='n')

    def __str__(self):
        return "({0} - {1}) {2}: {3}".format(self.id_word, self.language, self.term, self.definition)

"""
####Sample

Word
  | id | id_word | language | id_word | term    | definition | category |
  | -- | ------- | -------- | ------- | ----    | ---------- | -------- |
  | 01 | 01      | pt_br    | 01      | olá     | ...        | ...      | 
  | 02 | 01      | es_es    | 01      | hello   | ...        | ...      |

Language

  | language |           alphabet          |
  | -------- | --------                    |
  | pt-br    | abcdefghijklmnopqrstuvwxyz  |
  | en-us    | abcdefghijklmnopqrstuvwxyz  |
  | es-es    | abcdefghijklmnñopqrstuvwxyz |
"""
