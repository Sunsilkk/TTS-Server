import requests
import pyaudio

url = "http://127.0.0.1:5050/tts"
headers = {"Accept": "audio/wav", "Content-Type": "application/json"}
data = {
    "sessionId": 1234,
    "voice": "en-f-1",
    "text": "Hello, how are you? My name is Sunsilk and it's nice to meet you.",
    "seed": 5678,
}

# Define PyAudio stream parameters
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=24000,
                output=True)

# Make a request to the server to get the audio stream
with requests.post(url, headers=headers, json=data, stream=True) as response:
    if response.status_code == 200:
        # Stream the audio in real-time
        for chunk in response.iter_content(chunk_size=16384):
            if chunk:
                stream.write(chunk)
    else:
        print(f"Error: {response.status_code}")

# Stop and close the stream
stream.stop_stream()
stream.close()
p.terminate()
