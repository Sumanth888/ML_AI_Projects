from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/Restaurant_NPSR')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-515689466979-515189897137-519125179840-240081663ada58624d95e2b2f3953420', #app verification token
							'xoxb-515689466979-519694357124-vDcPqQESgeVJnnaYTu7AUoEH', # bot verification token
							'7V5Ow7RuJpZgVfh9rewdI79u', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5005, '/', input_channel))