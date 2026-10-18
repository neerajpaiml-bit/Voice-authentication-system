import librosa
import numpy as np
import parselmouth


# Function to extract features
def extract_voice_features(filename):
    # Load audio
    y, sr = librosa.load(filename, sr=22050)

    # 1. Fundamental Frequency (F0)/Pitch
    f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'), sr=sr)
    f0_mean = np.nanmean(f0)  # Mean pitch, ignoring NaNs
    f0_std = np.nanstd(f0)  # Standard deviation

    # 2. Formants (using parselmouth/Praat)
    sound = parselmouth.Sound(filename)
    formant = sound.to_formant_burg()  # Burg method for formant estimation
    f1 = formant.get_value_at_time(1, sound.duration / 2)  # F1 at midpoint
    f2 = formant.get_value_at_time(2, sound.duration / 2)  # F2
    f3 = formant.get_value_at_time(3, sound.duration / 2)  # F3

    # 3. Timbre/Spectral Features
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_mean = np.mean(mfccs, axis=1)  # Mean MFCCs
    spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
    chroma = np.mean(librosa.feature.chroma_stft(y=y, sr=sr), axis=1)  # Mean chroma
    zcr = np.mean(librosa.feature.zero_crossing_rate(y))

    # 4. Jitter & Shimmer (using parselmouth)
    point_process = parselmouth.praat.call(sound, "To PointProcess (periodic, cc)", 75, 600)  # For voiced parts
    jitter_local = parselmouth.praat.call(point_process, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)
    shimmer_local = parselmouth.praat.call([sound, point_process], "Get shimmer (local)", 0, 0, 0.0001, 0.02, 1.3, 1.6)

    # Return all features as a dictionary
    features = {
        "F0_Mean": f0_mean,
        "F0_Std": f0_std,
        "Formant_F1": f1,
        "Formant_F2": f2,
        "Formant_F3": f3,
        "MFCC_Mean": mfcc_mean.tolist(),  # List for easy printing
        "Spectral_Centroid": spectral_centroid,
        "Chroma_Mean": chroma.tolist(),
        "Zero_Crossing_Rate": zcr,
        "Jitter_Local": jitter_local,
        "Shimmer_Local": shimmer_local
    }
    return features


# Main program
if __name__ == "__main__":
    filename = "input.wav"  # Update this to your file path

    try:
        features = extract_voice_features(filename)
        print("Extracted Voice Features:")
        for key, value in features.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error: {e}. Ensure the file exists and is a valid WAV.")