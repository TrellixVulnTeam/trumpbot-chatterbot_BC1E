# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import logging
from chatterbot.trainers import ChatterBotCorpusTrainer

chatterbot = ChatBot('ALICE' , storage_adapter='chatterbot.storage.MongoDatabaseAdapter' ,
                     logic_adapters=[ "chatterbot.logic.MathematicalEvaluation" , "chatterbot.logic.TimeLogicAdapter" ,
	                     {"import_path":                      "chatterbot.logic.BestMatch" ,
		                     "response_selection_method":     "chatterbot.response_selection.get_first_response" ,
		                     "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance"} ,
	                     {'import_path':         'chatterbot.logic.LowConfidenceAdapter' , 'threshold': 0.50 ,
		                     'default_response': 'I am sorry, but I do not understand.'} ,
	                     {'import_path':    'chatterbot.logic.SpecificResponseAdapter' , 'input_text': 'Help me!' ,
		                     'output_text': 'Ok, here is a link: http://google.co.in'} ] ,
                     filters=[ 'chatterbot.filters.RepetitiveResponseFilter' ] ,
                     input_adapter='chatterbot.input.TerminalAdapter' ,
                     output_adapter='chatterbot.output.TerminalAdapter' , database='chatterbot-database')
# chatterbot.trainer.export_for_training('./export.json')
chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train('chatterbot.corpus.english' , )
print('Type something to begin...')

while True:
	try:
		bot_input = chatterbot.get_response(None)
	
	# Press ctrl-c or ctrl-d on the keyboard to exit
	except (KeyboardInterrupt , EOFError , SystemExit):
		break
