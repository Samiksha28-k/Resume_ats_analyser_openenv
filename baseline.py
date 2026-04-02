from inference import predict

def run_baseline():

    sample_input = {
        "resume_text": "python machine learning",
        "job_description": "python deep learning"
    }

    result = predict(sample_input)

    print("Baseline Score:", result)

if __name__ == "__main__":
    run_baseline()
