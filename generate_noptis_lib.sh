# Requires dependencies python3.10, yapf, pip and xsdata[cli,lxml,soap]
python noptis_fixer.py  --schema-path static/original --destination static/fixed --destination-lib static.noptis --make-pretty
