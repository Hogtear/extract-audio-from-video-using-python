import moviepy.editor


video = moviepy.editor.VideoFileClip("your-video.mp4")

# se o seu vídeo está na mesma pasta onde o seu arquivo python está, você pode escrever o nome diretamente
# caso contrário você precisa colocar o "path" do arquivo de vídeo.

audio = video.audio
audio.write_audiofile("extractedaudio.mp3")