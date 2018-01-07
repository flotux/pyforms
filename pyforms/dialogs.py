from pyforms import conf

if conf.PYFORMS_MODE in ['GUI','GUI-OPENCSP']:
	from pyforms.gui.dialogs.csv_parser import CsvParserDialog


elif conf.PYFORMS_MODE in ['TERMINAL']:
	class CsvParserDialog(object): pass