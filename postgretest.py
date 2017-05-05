# -*- coding: utf-8 -*-

import psycopg2
import datetime

params = {
  'dbname': 'coalprog2',
  'user': 'postgres',
  'password': 'test',
}


conn = psycopg2.connect(**params)

print 'test'

cur = conn.cursor()

fromDate = datetime.date(2010, 1, 1) # Year, Month, Day
toDate = datetime.date(2011, 1, 1) # Year, Month, Day

cur.execute("""SELECT * from sonad""", (fromDate, toDate))

print cur.fetchall()

"""
syndmus - [('idsyndmus',), ('kuupaev',), ('loodud',), ('esineja',), ('tekst',), ('jrk',), ('must_steno',), ('link',), ('ems_id',), ('liik',), ('paevakord_id',), ('aeg_video_suhtes',), ('video_nahtav',), ('video_id',)]
p'evakord - [('idpaevakord',), ('kuupaev',), ('loodud',), ('pealkiri',), ('link',), ('idistung',), ('must_steno',), ('liik',), ('ems_id',), ('toimetatud',), ('aeg_video_suhtes',), ('video_id',)]
istung - [('idistung',), ('istungjark_cf',), ('riigikogu_cf',), ('kuupaev',), ('loodud',), ('kellaaeg',), ('must_steno',), ('lopetatud',), ('istunginfo',), ('videod_nahtavad',)]

"""

"""
1) Sõna tuumad leida
2) Koostada tabel, kus on indekseeritud sõnade esinemised. Esialgu kõigest loetud arv.
3) Töötada läbi syndmus andmebaas.
"""