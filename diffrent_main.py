from extract_R import extract_voice_features
from compare import compare_voice_features

registered_file = "initial.wav"
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
