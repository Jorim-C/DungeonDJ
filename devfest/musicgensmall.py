from transformers import pipeline
import scipy
import sounddevice as sd
import scipy.io.wavfile as wav


# synthesiser = pipeline("text-to-audio", "facebook/musicgen-small")

# music = synthesiser("lo-fi music with a soothing melody", forward_params={"do_sample": True})

music_file_path = "musicgen_out.wav"
# scipy.io.wavfile.write(music_file_path, rate=music["sampling_rate"], data=music["audio"])


from transformers import AutoProcessor, MusicgenForConditionalGeneration

processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")

with open("reader.txt", "r") as file:
    text = file.readline()

inputs = processor(
    text=text,
    padding=True,
    return_tensors="pt",
)

audio_values = model.generate(**inputs, max_new_tokens=256)

#from IPython.display import Audio

#sampling_rate = model.config.audio_encoder.sampling_rate
#Audio(audio_values[0].numpy(), rate=sampling_rate)

sampling_rate = model.config.audio_encoder.sampling_rate
scipy.io.wavfile.write("musicgen_out.wav", rate=sampling_rate, data=audio_values[0, 0].numpy())

# Load WAV file
rate, data = wav.read(music_file_path)

# Play audio
sd.play(data, rate)
sd.wait()  # Wait until the sound finishes playing