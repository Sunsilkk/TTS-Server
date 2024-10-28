import requests

url = "http://127.0.0.1:5050/tts"
headers = {"Accept": "audio/wav", "Content-Type": "application/json"}
data = {
    "sessionId": 1234,
    "voice": "en-f-1",
    "text": "Apple Intelligence will be available in beta on all iPhone 16 models, iPhone 15 Pro, iPhone 15 Pro Max, iPad mini (A17 Pro), and iPad and Mac models with M1 and later, with Siri and device language set to US",
    "seed": 5678,
}

with requests.post(url, headers=headers, json=data, stream=True) as response:
    if response.status_code == 200:
        with open("output.wav", "wb") as f:
            for chunk in response.iter_content(
                chunk_size=16384
            ):  # Match server chunk size
                if chunk:
                    f.write(chunk)
        print("Audio saved to output.wav")
    else:
        print(f"Error: {response.status_code}")
