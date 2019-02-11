// Embed video and loop
//
// Solution by Michael Evensen
// https://gist.github.com/michaelevensen/9fe5e9e985846dff3196a73e0556970c


import AVKit
import AVFoundation

class ViewController: UIViewController {
    
    @IBOutlet weak var videoOverlayView: UIView!
    @IBOutlet weak var videoView: UIView!
    
    var player: AVPlayer?

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Load video resource
        if let videoUrl = Bundle.main.url(forResource: "video_file_name", withExtension: "mp4") {
            
            // Init video
            self.player = AVPlayer(url: videoUrl)
            self.player?.isMuted = true
            self.player?.actionAtItemEnd = .none
            
            // Add player layer
            let playerLayer = AVPlayerLayer(player: player)
            playerLayer.videoGravity = AVLayerVideoGravityResizeAspectFill
            playerLayer.frame = view.frame
            
            // Add video layer
            self.videoView.layer.addSublayer(playerLayer)
            
            // Play video
            self.player?.play()
            
            // Observe end
            NotificationCenter.default.addObserver(self,
                selector: #selector(playerItemDidReachEnd),
                name: NSNotification.Name.AVPlayerItemDidPlayToEndTime,
                object: self.player?.currentItem
            )
        }
    }
    
    // MARK: - Loop video when ended.
    func playerItemDidReachEnd(notification: NSNotification) {
        self.player?.seek(to: kCMTimeZero)
        self.player?.play()
    }
}
