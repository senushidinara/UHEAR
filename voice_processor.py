import boto3

transcribe = boto3.client('transcribe')

def process_voice(audio_url):
    job_name = "uhear_job"
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': audio_url},
        MediaFormat='mp3',
        LanguageCode='en-US'
    )
    # Wait & fetch transcript (simplified)
    result = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    transcript_url = result['TranscriptionJob']['Transcript']['TranscriptFileUri']
    # download & parse
    return "User transcript text"
