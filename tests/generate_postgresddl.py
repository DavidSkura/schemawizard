"""
  Dave Skura
"""

from schemawizard_package.schemawizard import schemawiz

postgres_ddl = schemawiz('tesla.csv').guess_postgres_ddl('my_postgres_table1')

print(postgres_ddl)

