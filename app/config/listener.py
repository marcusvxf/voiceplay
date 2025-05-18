import sounddevice as sd
import queue
import json
import threading
import os
from app.use_cases.use_cases import start, stop, next
from vosk import Model, KaldiRecognizer

model = Model(os.environ.get("VOSK_FILE_LOCATION", "./vosk-model-small-en-us-0.15"))
q = queue.Queue()
stop_event = threading.Event()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def listen():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        rec = KaldiRecognizer(model, 16000)
        while not stop_event.is_set():
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                texto = result.get("text", "")
                print("Você disse:", texto)

                if "start" in texto or "play" in texto:
                    start()
                elif "pause" in texto or "stop" in texto:
                    stop()
                elif "move" in texto or "next" in texto:
                    next()

def start_listening():
    stop_event.clear()
    listener_thread = threading.Thread(target=listen)
    listener_thread.start()

def stop_listening():
    stop_event.set()

if __name__ == "__main__":
    start_listening()

