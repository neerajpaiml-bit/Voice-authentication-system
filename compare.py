import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

# --------- Utility functions ---------

def normalize_scalar(a, b):
    """Convert distance to similarity score (0–1)"""
    return 1 / (1 + abs(a - b))


def cosine_sim(vec1, vec2):
    vec1 = np.array(vec1).reshape(1, -1)
    vec2 = np.array(vec2).reshape(1, -1)
    return cosine_similarity(vec1, vec2)[0][0]


# --------- Main comparison function ---------

def compare_voice_features(features1, features2):
    scores = {}

    # Scalar features
    scalar_keys = [
        "F0_Mean", "F0_Std",
        "Formant_F1", "Formant_F2", "Formant_F3",
        "Spectral_Centroid",
        "Zero_Crossing_Rate",
        "Jitter_Local",
        "Shimmer_Local"
    ]

    for key in scalar_keys:
        scores[key] = normalize_scalar(features1[key], features2[key])

    # Vector features
    scores["MFCC_Similarity"] = cosine_sim(features1["MFCC_Mean"], features2["MFCC_Mean"])
    scores["Chroma_Similarity"] = cosine_sim(features1["Chroma_Mean"], features2["Chroma_Mean"])

    # Final similarity score
    final_score = np.mean(list(scores.values()))

    return final_score, scores
if __name__ == "__main__":
    from extract_features import extract_voice_features
    from compare_voices import compare_voice_features

    registered_file = "registered.wav"
    input_file = "input.wav"

    features_registered = extract_voice_features(registered_file)
    features_input = extract_voice_features(input_file)

    final_score, detailed_scores = compare_voice_features(features_registered, features_input)

    print("\n🔍 Voice Comparison Results")
    print("-" * 30)

    for k, v in detailed_scores.items():
        print(f"{k}: {v:.3f}")

    print("\n✅ Final Similarity Score:", round(final_score, 3))

    if final_score > 0.75:
        print("🎉 SAME SPEAKER (Voice Matched)")
    else:
        print("❌ DIFFERENT SPEAKER")
