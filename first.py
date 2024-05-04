from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from youtube_transcript_api import YouTubeTranscriptApi as yta

import time
import sys
import json
import os

def main():
    if len(sys.argv) == 2:
        channelId = f"https://www.youtube.com/@{sys.argv[1]}/videos"
        if get_videos_links(channelId) == "SUCCESS":
            with open("videos.json","r") as videos:
                datas = json.load(videos)
                for data in datas:
                    try:
                        create_transcript(data['title'],data['vidId'])
                    except:
                        pass
    else:
        print("Please use the correct input")

def create_transcript(title,videoId):
    transcript_full = yta.get_transcript(videoId)
    if not os.path.exists('transcripts'):
        os.makedirs('transcripts')
    else:
        with open(f"transcripts/{title}.txt","w") as title:
            for transcript in transcript_full:
                title.write(transcript["text"] + "\n\n")

def get_videos_links(channelId):
    url = channelId
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    # driver = webdriver.Edge()
    driver.get(url)
    time.sleep(10)

    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height

    videoLinks = []

    try:
        for e in WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div#details'))):
            title = e.find_element(By.CSS_SELECTOR,'a#video-title-link').get_attribute('title')
            vurl = e.find_element(By.CSS_SELECTOR,'a#video-title-link').get_attribute('href')
            vidId = vurl.split("v=")[1]
            videoLinks.append({
                'video_url':vurl,
                'title':title,
                'vidId':vidId,
                })
            # videoLinks.append(vurl)
    except:
        pass

    with open("videos.json","w") as trace:
        json.dump(videoLinks,trace)
    driver.quit()
    return ("SUCCESS")


if __name__ == "__main__":
    main()