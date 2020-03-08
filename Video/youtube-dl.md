# youtube-dl

## Download MP3 with highest quality
```sh
youtube-dl -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 URL
```


## Download MP4 with highest quality
```sh
youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4’ URL
```

## Create alias for simple use
For persistent use, add these lines to your shell file such as `.bash_profile`, `.zshrc` etc.
```sh
alias youtube-dl-mp3="youtube-dl -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0"
alias youtube-dl-mp4="youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'"
```


### How to batch download from a text file.
```sh
youtube-dl-mp3 $(<youtubelinks.txt)
youtube-dl-mp4 $(<youtubelinks.txt)
```
