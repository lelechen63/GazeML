"""Video (file) data source for gaze estimation."""
import os
import time

import cv2 

from .frames import FramesSource


class Image(FramesSource):
    """Image frame grabbing and preprocessing."""

    def __init__(self, image_path, **kwargs):
        """Create queues and threads to read and preprocess data."""
        self._short_name = 'Image'

        assert os.path.isfile(image_path)
        self._image_path = image_path

        # Call parent class constructor
        super().__init__(staging=False, **kwargs)

    # def frame_generator(self):
    #     """Read frame from image path."""
    #     return cv2.imread(self._image_path)
       
    def frame_read_job(self):
        """Read frame from video (without skipping)."""
        before_frame_read = time.time()
        bgr = cv2.imread(self._image_path)
        after_frame_read = time.time()
    
        with self._read_mutex:
            self._frame_read_queue.put((before_frame_read, bgr, after_frame_read))
