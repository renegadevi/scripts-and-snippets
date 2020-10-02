# ffmpeg

## Get file information
```sh
ffmpeg -i iphone.mov -hide_banner
ffprobe -i iphone.mov -hide_banner
```

## Extract audio from video
```bash
ffmpeg -i input.mp4 -f mp3 -vn output.mp3
```

## "Compress" video
```bash
ffmpeg -i input.mp4 -vcodec h264 -acodec mp2 output.mp4
```

## Remove audio from video
```bash
ffmpeg -i input.mp4 -an output.mp4
```

## Trim audio after 3 min
```bash
ffmpeg -t 180 -i input.mp3 -acodec copy output.mp3
```

## Mix video with audio
```bash
ffmpeg -i input.mp3 -i input.mp4 output.mp4
```

## Resize a video
```bash
ffmpeg -i input.mp4 -vf scale=1280:720 output.mp4
```

## Split video into frames
```bash
ffmpeg -i video.flv frame_%04d.jpg
```

## Convert image into a 30 sec video
```bash
ffmpeg -loop 1 -i img_%03d.jpg -c:v libx264 -t 30 -pix_fmt yuv420p out.mp4
```

**Batch example**
```bash
for i in *.png; do ffmpeg -loop 1 -i "$i" -c:v libx264 -t 5 -pix_fmt yuv420p "${i%.*}.mp4"; done
```

## Upscale and letterbox/pillarbox a video to 1080p

```bash
ffmpeg -i input.mp4 -vf "scale=(iw*sar)*min(1920/(iw*sar)\,1080/ih):ih*min(1920/(iw*sar)\,1080/ih), 1920:1080:(1920-iw*min(1920/iw\,1080/ih))/2:(1080-ih*min(1920/iw\,1080/ih))/2" output_1080p.mp4
```


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
ffmpeg -y -i input.mov -vcodec wmv2 -qscale:v 3 -b 10000k output.wmv
```

# ffplay

## Play a video on repeat
```sh
ffplay -loop 0 movie.mp4
```

## Play a video in specific size
```sh
ffplay -x 480 -y 360 movie.mp4
```

## Play a video borderless and screen position
```sh
ffplay -noborder -left 0 -top 0 movie.mp4
```
