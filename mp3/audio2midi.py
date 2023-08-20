from basic_pitch.inference import predict_and_save

def convert_mp3_to_midi(mp3_file, output_directory):
  """Converts an MP3 file to a MIDI file and saves it to the specified output directory.

  Args:
    mp3_file: The path to the MP3 file to convert.
    output_directory: The path to the output directory where the MIDI file will be saved.
  """

  predict_and_save(
      mp3_file,
      output_directory,
      True,
      False,
      False,
      False)

if __name__ == "__main__":
  # Get the path to the MP3 file to convert.
  # get all the mp3 files in this directory
    import os
    mp3_file = []
    for file in os.listdir("../mp3"):
        if file.endswith(".mp3"):
            mp3_file.append(os.path.join("../mp3", file))
    print(mp3_file)


  # Get the path to the output directory where the MIDI file will be saved.
    output_directory = "../midi/"

  # Convert the MP3 file to a MIDI file and save it to the output directory.
    convert_mp3_to_midi(mp3_file, output_directory)
