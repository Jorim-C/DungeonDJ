from gradio_client import Client

HF_TOKEN="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"
client = Client("sanchit-gandhi/musicgen-streaming",hf_token=HF_TOKEN)
result = client.predict(
		text_prompt="80s pop track with synth and instrumentals",
		audio_length_in_s=15,
		play_steps_in_s=1.5,
		seed=5,
		api_name="/predict"
)
print(result)