# Open Progress

Map election promises from coalition agreements/action plans to debates in parliamentary bodies to show real progress of governance based on actual data. This is the fork of [Guardians of Governance](http://www.praxis.ee/tood/valitsemise-valvurid/) ([in developer portfolio](http://pixel.ee/teema/valitsemise-valvurid)) to make the process (in large part) automatic.

![Guardians of Governance screenshot](https://github.com/infoaed/openprogress/blob/master/valvurid.jpg)

Team:

* Gea, Ailan — outstanding citizens (coalition agreement analysis & finetuning keywords/searches)
* Artur, Ilja, Andrus — programmers (from back end to front end and back)
* Märt — data scraper (actually just idling around and preparing for the pitches)

Prototype:

* http://gov.infoaed.ee

Roadmap:

* Detect/formalise keywords of coalition agreements/action plans of government for automatic search.
* Natural language analysis and categorisation of discussions in parliament (passing legal acts, information inquiries by opposition, press conferences, specialised commission protocols, document metadata, persons involved, results of voting etc).
* Visualise results using progress bars and display/highlight parts of text that the results are based on.

Details:

* Use data from Estonian parliament [demo API](https://aavik.riigikogu.ee/) and/or [data dumps](https://github.com/okestonia/opendata-issue-tracker/issues/60#issuecomment-294106882).
* Use [Vabamorf](https://github.com/estnltk/pyvabamorf) for basic natural language processing.
* Need data analysts, data visualisers plus some UX/scripting.

The pitch for [Garage48 Open & Big Data hackathon](http://garage48.org/events/balticopenbigdata2017):

* [Google Presentation](https://docs.google.com/presentation/d/1NdqRfQJ0I0RN7QnC_U9zdb1HfUPWep4qks-6D0_Yem4) // [PDF](https://github.com/infoaed/openprogress/blob/master/garage48-pitch.pdf)

This is first iteration to hack our democracy to open it up for more reasonable and measurable election promises.

The initial project was developed during 12h at [Demokratiahack](https://www.sitra.fi/tapahtumat/demokratiahack/).

* https://hackdash.org/projects/590c99334545fa01a8db1638
