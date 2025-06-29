from transformers import pipeline

def generate_summary(text):
    from transformers import pipeline
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    summary = summarizer(text[:1024], max_length=120, min_length=30, do_sample=False)
    return summary[0]['summary_text']
