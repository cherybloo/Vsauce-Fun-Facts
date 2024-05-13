<a name="top"></a>

<h1 align="center">
:brain: Vsauce's Fun Facts Web Extension :brain:
<h3> A web browser extension with all vsauce's fun facts </h3>
</h1>

<br/>

> [!IMPORTANT]
> This web extension has been tested on:
> - Firefox 125.0.3
> - Brave 1.65.132

> [!NOTE]
> The JSON Endpoint can be used, but it will be updated pretty soon!
> The Endpoint: https://raw.githubusercontent.com/cherybloo/Vsauce-Fun-Facts/main/funfact.json

# HOW TO USE?
1. Clone this git repository
   ```markdown
   git clone https://github.com/cherybloo/Vsauce-Fun-Facts.git
   ```
2. Follow the instructions below based on your web browswer
   | <img src="https://upload.wikimedia.org/wikipedia/commons/6/68/Brave_logo.svg" height="50"> | <img src="https://brave.com/static-assets/images/firefox-logo.svg" height="50"/>|
   |---|---|
   | 1. Go to `Settings` > `Extensions` > `Load unpacked` | 1. Type `about:debugging` on the search bar |
   |2. Locate to where the git repository saved | 2. Click on `This Firefox` > `Load Temporary Add-on...`|
   |3. Select the `extensions` folder| 3. Locate to where the git repository saved > `extensions` folder|
   ||4. Select the `manifest.json` file|

# Files Explained
## 1. bulletpoints.py
This python script is to convert all the youtube transcripts from the `transcripts folder` into a useful bullet point that then could be converted into a JSON file for the web extension. I utilized the power of [Vertex AI](https://cloud.google.com/generative-ai-studio?hl=en) to generate all of the bullet points and saved the responses into a txt file.
#### External ibrary used:
- google-cloud-aiplatform

## 2. convert.py
This is a simple script to convert the clean txt file into JSON file.
- [ ] Merge `convert.py` to `bulletpoints.py`

## 3. transcripts.py
This particular script combines all my skills in web scraping, saving files into a different folder, and also cleaning up some responses
#### External libraries used:
- selenium
- webdriver-manager
- youtube-transcript-api
