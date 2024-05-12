import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models

PROJECT_ID = "vsauce1"
LOCATION = "europe-west3"

def generate(filename):
	vertexai.init(
		project=PROJECT_ID,
		location=LOCATION
	)
	model = GenerativeModel(model_name="gemini-1.0-pro-vision-001")
	with open(filename,"r") as texts:
		responses = model.generate_content(
			"Summarize this text into 5 bullet points of fun facts" + texts.read(),
			generation_config=generation_config,
			safety_settings=safety_settings,
			stream=True,
		)
		for response in responses:
			try:
				with open("funfacts.txt","a") as funfact:
						funfact.write(response.text)
			except:
				print("ups explicit stuffs here")
				continue

generation_config = {
"max_output_tokens": 1600,
"temperature": 0.4,
"top_p": 0.4,
"top_k": 32,
}

safety_settings = {
generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
}

with open("filenames.txt","r") as filenames:
	for f in filenames:
		generate('transcripts/' + f.strip('\n'))