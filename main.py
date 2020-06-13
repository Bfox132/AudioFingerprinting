def main():
    import audalign as ad
    import time

    # TODO: autosaver?
    # TODO: New fingerprint algorithm
    # TODO: Not double add files
    # TODO: Document
    # TODO: Add uniquehashes and filename fields

    ada = ad.Audalign("all_audio.json")
    # ada.write_processed_file("ResearchMaher/FraserSUB.mov", "processed_audio/FraserSUB.wav")
    t = time.time()
    # ada.fingerprint_file("audio_files/TestAudio/Rachel.mp4")
    # ada.fingerprint_directory("audio_files")
    t = time.time() - t
    print(f"It took {t} seconds to complete.")
    print(f"Total fingerprints: {ada.total_fingerprints}")
    print(
        f"Number of fingerprinted files: {len(ada.fingerprinted_files)} : {len(ada.file_names)}"
    )

    # ada.save_fingerprinted_files("all_audio.json")
    ada.plot("audio_files/TestAudio/Paige.MOV")
    print(ada.recognize("audio_files/TestAudio/Rachel.mp4"))


if __name__ == "__main__":
    main()
