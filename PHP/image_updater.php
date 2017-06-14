<?php
/**
 * Image updater
 *
 * Used as a simple cache to only update the background once a day, whenever
 * $duration value is exceeded from the log file, update image contents and save
 * timestamp to a log file.
 *
 * @param   int     $duration
 * @param   string  $log_file
 * @param   string  $image_file
 * @param   string  $source
 */
function updateImage($duration, $log_file, $image_file, $source) {

    // If there's no log file, create one
    if (!file_exists($log_file)) {
        touch($log_file);
    }

    // If there's no image file, create one
    if (!file_exists($image_file)) {
        touch($image_file);
    }

    // Get last runtime
    $last_run = file_get_contents($log_file);

    // Update image and log file if duration has exceed duration
    if (time() - $last_run >= $duration) {

        // Try to put contents/update image and log file
        try {
            file_put_contents($image_file, file_get_contents($source));
            file_put_contents($log_file, time());
        }
        catch (Exception $e) {
            echo $e->getMessage();
        }
    }

}

updateImage(
    $duration   = 86400,
    $log_file   = 'time.log',
    $image_file = 'bg.jpg',
    $source     = 'https://source.unsplash.com/category/nature'
);