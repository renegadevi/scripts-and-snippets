# ffmpeg

## Batch convert MKV to MP4 with re-encode audio
```sh
for f in *.mkv;do ffmpeg -i "$f" -c:v copy -c:a aac -b:a 256k -strict -2 "${f%mkv}mp4";done
```

## Batch convert MKV to MP4 without re-encode audio
```sh
for f in *.mkv;do ffmpeg -i "$f" -c copy "${f%mkv}mp4";done;rm *.mkv
```

## Convert MOV to WMV
```sh
ffmpeg -y -i myfile.mov -vcodec wmv2 -qscale:v 3 -b 10000k mynewfile.wmv
```
